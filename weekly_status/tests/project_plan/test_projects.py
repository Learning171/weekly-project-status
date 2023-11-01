import json
import pytest

@pytest.mark.django_db
def test_project_post(client, payload):
    register_response = client.post('http://127.0.0.1:8000/api/user/register/',payload)
    assert register_response.status_code==201

    headers = {
        'Authorization': f"Bearer {register_response.data['token']['access']}"
        }
    
    profile_response = client.get("http://127.0.0.1:8000/api/user/profile/", headers=headers)
    print("user_id post",profile_response.data['id'])
    assert profile_response.status_code == 200
    # print("user profile succesfull")
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
    print(response.status_code)
    assert response.status_code==201
    print("profile added success", response.status_code)

    print("......................")

# get mwthod
@pytest.mark.django_db
def test_project_get(client, payload):
    register_response = client.post('http://127.0.0.1:8000/api/user/register/',payload)
    assert register_response.status_code==201

    headers = {
        'Authorization': f"Bearer {register_response.data['token']['access']}"
        }
    
    profile_response = client.get("http://127.0.0.1:8000/api/user/profile/", headers=headers)
    #print("user_id",profile_response.data['id'])
    assert profile_response.status_code == 200
    # print("user profile succesfull")
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
    dataa1 ={
        "project_name":"project2",
        "summary":"about project",
        "user":profile_response.data['id'],
        "manager_name":"XYZ",
        "client_name":"PQR",
        "start_date":"2023-09-10",
        "end_date":"2023-09-12"
        }

    response =client.post(url, dataa)
    response1 =client.post(url, dataa1)
    print(response.status_code)
    assert response.status_code==201
    print("Project added success", response.status_code)
    
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/3/"
    response = client.get(url)
    print("---------", response.data)
    print(response.status_code)
    assert response.status_code == 200

    put_data = {
        "project_name": "project4",
        "summary": "test project",
        "manager_name": "XYZ",
        "client_name": "PQR",
        "start_date": "2023-09-10",
        "end_date": "2023-09-12",
        "user": f"{response.data['user']}"
    }
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/3/"
    put_response =client.put(url, data=json.dumps(put_data), content_type='application/json')
    print("put_response------",put_response.data)

    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/3/"
    delete_response =client.delete(url)
    print("delete_response------",delete_response.data)
    