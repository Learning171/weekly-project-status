import pytest
import json

@pytest.mark.django_db
def test_accomplishment(client, payload):
    register_response = client.post('http://127.0.0.1:8000/api/user/register/',payload)
    assert register_response.status_code==201
    
    headers = {
        'Authorization': f"Bearer {register_response.data['token']['access']}"
        }
    
    profile_response = client.get("http://127.0.0.1:8000/api/user/profile/", headers=headers)
    assert profile_response.status_code == 200

    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/"

    dataa ={
        "project_name":"project1",
        "summary":"about project",
        "user":profile_response.data['id'],
        "manager_name":"XYZ",
        "client_name":"PQR",
        "start_date":"2023-09-10",
        "end_date":"2023-09-12"
        }

    response =client.post(url, dataa)
    print(response.data)
    assert response.status_code==201
    print("Project added success", response.status_code)
    print("......................")

    # get method

    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/1/"
    get_response = client.get(url)
    print("---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    #main weekly report

    # post method

    post_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"

    post_data = {
        "title": "my title",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-15",
        "project":get_response.data['id']
    }

    #POST 201 success
    post_response=client.post(post_url,post_data)
    print(post_response.status_code)
    assert post_response.status_code==201
    print("weeklyreport added success", post_response.status_code)
    print("......................")

    #post accomplishment 201
    post_url = "http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/"

    post_data = {
        "report" : 1,
        "Description": "test post accomplishment"
    }
    post_response_accomplishment = client.post(post_url, post_data)
    print(post_response_accomplishment.status_code)
    assert post_response_accomplishment.status_code==201
    print("accomplishment added success", post_response_accomplishment.status_code)
    print("......................")

    #post fail accomplishment 400
    post_fail_url = "http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/"

    post_fail_data = {
        "report" : "",
        "Description": "test post accomplishment"
    }
    post_response_accomplishment_fail400 = client.post(post_fail_url, post_fail_data)
    print(post_response_accomplishment_fail400.status_code)
    assert post_response_accomplishment_fail400.status_code == 400
    print("accomplishment fail 400 success", post_response_accomplishment_fail400.status_code)
    print("......................")
