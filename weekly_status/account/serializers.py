from rest_framework import serializers
from account.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import Util

class UserRegistartionSerializers(serializers.ModelSerializer):
    # we need confirm password field in registration request
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["user_email", "user_name", "user_type","password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    # validate password and confirm password are same or not.
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password dose not match")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(max_length=250)
    class Meta:
        model = User
        fields = ["user_email", "password"]

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 250, style = {"input_type": "password"}, write_only = True)
    password2 = serializers.CharField(max_length = 250, style = {"input_type": "password"}, write_only = True)
    class Meta:
        fields = ["password", "password2"]
    
    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password dose not match")
        user.set_password(password)
        user.save()
        return attrs
    
class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 255)
    class meta:
        fields = ["email"]
 
    def validate(self, attrs):
        email = attrs.get("email")
        if User. objects.filter(user_email=email).exists():
            user = User.objects.get(user_email = email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = "http://localhost:3000/api/user/reset/"+uid+"/"+token
            # Send Email
            body = "Click following link to reset your password " + link
            data = {
                "subject" : "Reset your Password",
                "body" : body,
                "to_email" : user.user_email
            }
            Util.send_email(data)
            return attrs
        else:
            raise ValueError("You are not registered user")
        
class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 250, style = {"input_type": "password"}, write_only = True)
    password2 = serializers.CharField(max_length = 250, style = {"input_type": "password"}, write_only = True)
    class Meta:
        fields = ["password", "password2"]
    
    def validate(self, attrs):
        try:
            password = attrs.get("password")
            password2 = attrs.get("password2")
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("Password and Confirm Password dose not match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id = id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValueError("Token is Valid or Expired")
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise ValueError("Token is Valid or Expired")
        
class UserLogoutSerializer(serializers.ModelSerializer):
    pass

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_email", "user_name", "is_active","user_type"]