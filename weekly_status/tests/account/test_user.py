import pytest
from account.serializers import UserRegistartionSerializers
from rest_framework import serializers 


@pytest.mark.django_db
def test_register_user(client, payload):
    print("testing Starts here")

    user_register_response = client.post("http://127.0.0.1:8000/api/user/register/", payload)
    data = user_register_response.data
    assert user_register_response.status_code == 201


    data1 = {"user_email" : payload['user_email'], "password":payload['password']}
    login_response = client.post("http://127.0.0.1:8000/api/user/login/", data=data1)
    assert login_response.status_code == 200
    print("user login successfull")
    
    #Fail login password
    
    fail_data= {"user_email" : "xyz@gmail.com", "password":"mypass"}
    fail_login_response = client.post("http://127.0.0.1:8000/api/user/login/", data=fail_data)
    assert fail_login_response.status_code == 400
    print("fail_login_response")

    headers = {
        'Authorization': f"Bearer {user_register_response.data['token']['access']}"
    }

    profile_response = client.get("http://127.0.0.1:8000/api/user/profile/", headers=headers)
    assert profile_response.status_code == 200
    print("user profile successfull")

    data2 = {'password':"paas2",'password2':"paas2"}
    password_change_response = client.post("http://127.0.0.1:8000/api/user/changepassword/", headers=headers, data=data2)
    assert password_change_response.status_code == 201
    print("user password change successfull")

    data2 = {'password':"paas2",'password2':"paas1"}

    fali_validation_response = client.post("http://127.0.0.1:8000/api/user/changepassword/", headers=headers, data=data2)
    assert fali_validation_response.status_code == 400
    print("user password change Error")

    # account app line no 7 test case
    data2 = {'password':"paas2",'password2':"paas1"}
    with pytest.raises(serializers.ValidationError) as errorinfo:
        UserRegistartionSerializers.validate(data2, data2)

    assert str(errorinfo.value) == f"[ErrorDetail(string='Password and Confirm Password dose not match', code='invalid')]"

    # with pytest.raises(serializers.ValidationError) as errorinfo:
    #     UserPasswordResetSerializer.validate(data2, data2)

    # assert str(errorinfo.value) == f"[ErrorDetail(string='Password and Confirm Password dose not match', code='invalid')]"
    # data1 = {"user_email" : payload['user_email'], "password":payload['password']}
    # login_response = client.post("http://127.0.0.1:8000/api/user/logout/", data=data1)
    # assert login_response.status_code == 200
    # print("user logout successfull")