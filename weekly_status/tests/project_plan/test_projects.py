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
    
    fail_post_dataa ={
        "project_name":"project1",
        "summary":"about project",
        "client_name":"PQR",
        "start_date":"2023-09-10",
        "end_date":"2023-09-12"
        }
    
    response =client.post(url, dataa)
    print(response.status_code)
    assert response.status_code==201
    print("profile added success", response.status_code)

    #Fail Post request projects
    fail_post_response =client.post(url, fail_post_dataa)
    assert fail_post_response.status_code==400
    print("fail post success", fail_post_response.status_code)
    
    # Get project by Id
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/7/"
    response = client.get(url)
    assert response.status_code == 200

    #Get by list
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/"
    list_response = client.get(url)
    print("list_response-=-=-=-",list_response.status_code, list_response.data)
    assert list_response.status_code == 200

    #fail Get request projects
    fail_get_url = "http://127.0.0.1:8000/api/projectplan/projectsapi/11/"
    fail_response = client.get(fail_get_url)
    assert fail_response.status_code == 404

    put_data = {
        "project_name": "project4",
        "summary": "test project",
        "manager_name": "XYZ",
        "client_name": "PQR",
        "start_date": "2023-09-10",
        "end_date": "2023-09-12",
        "user": f"{response.data['user']}"
    }
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/7/"
    put_response =client.put(url, data=json.dumps(put_data), content_type='application/json')
    print("put_response------",put_response.data, response.status_code)
    assert put_response.status_code == 200

    #PUT Fail 400 Bad request testcase

    put_fail_data = {
        #"project_name": "project4",
        "summary": "test project",
        "manager_name": "XYZ",
        "client_name": "PQR",
        "start_date": "2023-09-10",
        "end_date": "2023-09-12",
        "user": f"{response.data['user']}"
    }
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/7/"
    put_fail_response =client.put(url, data=json.dumps(put_fail_data), content_type='application/json')
    print("put_response---400---",put_fail_response.data, put_fail_response.status_code)
    assert put_fail_response.status_code == 400

    #Put fail not found 404 testcase
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/11/"
    put_fail_404_response =client.put(url, data=json.dumps(put_fail_data), content_type='application/json')
    print("put_response---404---",put_fail_404_response.data, put_fail_404_response.status_code)
    assert put_fail_404_response.status_code == 404

    #Patch Sucess 200 request
    patch_data = {
        "project_name": "project4",
        "summary": "test project patch",
        "manager_name": "DSC",
        "client_name": "PQR",
        "start_date": "2023-09-10",
        "end_date": "2023-09-12",
        "user": f"{response.data['user']}"
    }
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/7/"
    patch_response =client.patch(url, data=json.dumps(patch_data), content_type='application/json')
    print("patch_response------",patch_response.data, patch_response.status_code)
    assert patch_response.status_code == 200

    #patch 400 fail
    patch_fail_data = {
        "project_name": "",
        "summary": "test project patch",
        "manager_name": "",
        "client_name": "PQR",
        "start_date": "2023-09-10",
        "end_date": "2023-09-12",
        "user": f"{response.data['user']}"
    }
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/7/"
    patch_fail_response =client.patch(url, data=json.dumps(patch_fail_data), content_type='application/json')
    print("patch_fail 400response------",patch_fail_response.data, patch_fail_response.status_code)
    assert patch_fail_response.status_code == 400

    #Patch Not found 404
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/11/"
    patch_fail_response =client.patch(url, data=json.dumps(patch_fail_data), content_type='application/json')
    print("patch_fail 404response------",patch_fail_response.data, patch_fail_response.status_code)
    assert patch_fail_response.status_code == 404


    #Delete sucess 200
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/7/"
    delete_response =client.delete(url)
    print("delete_response------",delete_response.data)
    assert delete_response.status_code == 200

    #Delete fail 404 projects
    fail_url = "http://127.0.0.1:8000/api/projectplan/projectsapi/11/"
    delete_response =client.delete(fail_url)
    print("fail delete_response------",delete_response.data)
    assert delete_response.status_code == 404

    