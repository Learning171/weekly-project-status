import pytest

@pytest.fixture
def payload():
    print("getting payload from fixture function")
    payload = {
    "user_email" : "shu10@gmail.com",
    "user_name" : "Shubha", 
    "user_type" : "Project_manager",
    "password" : "pass1",
    "password2" : "pass1"
    }
    return payload


