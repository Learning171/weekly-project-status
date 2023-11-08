import pytest
import json

@pytest.mark.django_db
def test_weeklyreport(client, payload):
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

    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/11/"
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

    fail_post_data = {
        "title": "my title",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-15",
        "project":"",
    }
    #POST 201 success
    post_response=client.post(post_url,post_data)
    print(post_response.status_code)
    assert post_response.status_code==201
    print("weeklyreport added success", post_response.status_code)
    print("......................")

    #POST 400 Bad request
    fail_post_response=client.post(post_url,fail_post_data)
    print(fail_post_response.status_code)
    assert fail_post_response.status_code==400
    print("weeklyreport Post Fail 400", fail_post_response.status_code)
    print("......................")


    
    # get method

    get_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"
    get_response = client.get(get_url)
    print("get method for weeklyreport---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    # get by id
    get_url_id = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/10/"
    get_response_id = client.get(get_url_id)
    print("get method for weeklyreport by id---------", get_response_id.data)
    print(get_response_id.status_code)
    assert get_response_id.status_code == 200
    print("......................")

    #Get Fail 404 
    get_url_id = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/11/"
    get_fail_response = client.get(get_url_id)
    print("get method for weeklyreport by id Fail 404---------", get_fail_response.data)
    print(get_fail_response.status_code)
    assert get_fail_response.status_code == 404
    print("......................")

    # put method
    put_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/10/"
    put_data = {
        "title": "my title",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-20",
        "project":11
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.status_code)
    assert put_response.status_code==200
    print("weeklyreport update success", put_response.status_code)
    print("......................")

    # Fail 400 Bad request put method
    #put_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/7/"
    fail_put_data = {
        "title": "my title",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-20",
        "project":"",
    }
    fail_put_response=client.put(put_url,data=json.dumps(fail_put_data), content_type='application/json')
    print(fail_put_response.status_code)
    assert fail_put_response.status_code == 400
    print("weeklyreport update fail 400 success", fail_put_response.status_code)
    print("......................")

    # Fail 404 not found put method
    put_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/12/"
    fail_put_404_data = {
        "title": "my title",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-20",
        "project":11,
    }
    fail_put_404_response=client.put(put_url,data=json.dumps(fail_put_404_data), content_type='application/json')
    print(fail_put_404_response.data)
    assert fail_put_404_response.status_code == 404
    print("weeklyreport update fail 404 success", fail_put_404_response.status_code)
    print("......................")

    #Patch 200 sucess weeklyreport
    patch_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/10/"
    patch_data = {
        "title": "patch request",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-20",
        "project":11
    }
    patch_200_response=client.patch(patch_url,data=json.dumps(patch_data), content_type='application/json')
    print(patch_200_response.status_code)
    assert patch_200_response.status_code==200
    print("weeklyreport patch 200 update success", patch_200_response.status_code)
    print("......................")

    #Patch 400 Bad request sucess weeklyreport
    fail_patch_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/10/"
    fail_patch_data = {
        "title": "patch request",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-20",
        "project":"",
    }
    patch_fail_400_response=client.patch(fail_patch_url,data=json.dumps(fail_patch_data), content_type='application/json')
    print(patch_fail_400_response.status_code)
    assert patch_fail_400_response.status_code == 400
    print("weeklyreport patch fail bad 400 update success", patch_fail_400_response.status_code)
    print("......................")

    ##Patch 404 Bad request sucess weeklyreport
    fail_patch_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/12/"
    fail_patch_data = {
        "title": "patch request",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-20",
        "project":10,
    }
    patch_fail_404_response=client.patch(fail_patch_url,data=json.dumps(fail_patch_data), content_type='application/json')
    print(patch_fail_404_response.status_code)
    assert patch_fail_404_response.status_code == 404
    print("weeklyreport patch fail bad 404 update success", patch_fail_404_response.status_code)
    print("......................")

    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/weeklyreportapi/10/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    assert delete_response.status_code == 200
    print("......................")

    # delete 404 not found fail
    delete_fail_404_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/13/"
    fail_404_response = client.delete(delete_fail_404_url)
    print("-=-===- delete 404-=-=-=",fail_404_response.status_code, fail_404_response.data)
    assert fail_404_response.status_code == 404