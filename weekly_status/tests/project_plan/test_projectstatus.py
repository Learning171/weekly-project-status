import pytest
import json

@pytest.mark.django_db
def test_project_post(client, payload):
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
    print("projectstatus....", response.data)
    assert response.status_code==201
    print("Project added success", response.status_code)
    print("......................")

    # get method

    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/1/"
    response = client.get(url)
    assert response.status_code == 200
    print("......................")


    # post method weekly report

    post_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"

    post_data = {
        "title": "my title",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-15",
        "project":1
    }

    post_response=client.post(post_url,post_data)
    assert post_response.status_code==201
    print("weeklyreport added success", post_response.status_code)
    print("......................")
    
    # get method

    get_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"
    get_response = client.get(get_url)
    assert get_response.status_code == 200
    print("......................")

    # get by id
    get_url_id = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/1/"
    get_response_id = client.get(get_url_id)
    print("get_response_id",get_response_id.status_code)
    assert get_response_id.status_code == 200
    print("......................")


    #Project Status Module
    project_status_post_url = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/"
    status_post_data = {
        "id": 1,
        "overall_last_week": "A",
        "overall_this_week": "A",
        "scope": "A",
        "schedule": "A",
        "cost": "A",
        "overall_health": "A",
        "report": 1
    }

    project_status_post_response=client.post(project_status_post_url,status_post_data)
    assert project_status_post_response.status_code==201
    print("project_status added success", project_status_post_response.status_code)
    print("......................")

    project_status_get_url_id = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/1/"
    get_response_id = client.get(project_status_get_url_id)
    print("get method for projectstatus by id---------", get_response_id.data)
    print("get_response_id",get_response_id.status_code)
    assert get_response_id.status_code == 200
    print("......................")


    project_status_put_url = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/1/"
    status_post_data = {
        "id": 1,
        "overall_last_week": "G",
        "overall_this_week": "A",
        "scope": "A",
        "schedule": "G",
        "cost": "A",
        "overall_health": "R",
        "report": 1
    }
    project_status_put_response=client.put(project_status_put_url,data=json.dumps(status_post_data), content_type='application/json')
    print(project_status_put_response.data)
    assert project_status_put_response.status_code==200
    print("project status update success", project_status_put_response.status_code)
    print("......................")


    delete_url ="http://127.0.0.1:8000/api/projectplan/projectstatusapi/1/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    assert delete_response.status_code==200
    print("......................")

