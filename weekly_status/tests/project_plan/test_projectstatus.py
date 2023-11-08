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

    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/7/"
    get_response = client.get(url)
    print("-----test_projecstatus_get----", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200


    # post method weekly report

    post_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"

    post_data = {
        "title": "my title",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-15",
        "project":get_response.data['id']
    }

    post_response=client.post(post_url,post_data)
    assert post_response.status_code==201
    print("weeklyreport added success", post_response.status_code)
    print("......................")

    get_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/6/"
    get_response = client.get(get_url)
    print("-=-=-=-=-=-=-=get weekly response issue-=-==-", get_response.data)
    assert get_response.status_code == 200
    
    # get method by list

    get_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"
    get_response = client.get(get_url)
    print("get_response project status", get_response.data)
    assert get_response.status_code == 200
    print("......................")

    # get by id
    get_url_id = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/6/"
    get_response_id = client.get(get_url_id)
    print("get_response_id",get_response_id.status_code)
    assert get_response_id.status_code == 200
    print("......................")


    #Project Status 201 Module
    project_status_post_url = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/"
    status_post_data = {
        "overall_last_week": "A",
        "overall_this_week": "A",
        "scope": "A",
        "schedule": "A",
        "cost": "A",
        "overall_health": "A",
        "report": 6
    }

    project_status_post_response=client.post(project_status_post_url,status_post_data)
    assert project_status_post_response.status_code==201
    print("project_status added success", project_status_post_response.status_code)
    print("......................")

    #Post Fail 400
    project_status_fail400_post_url = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/"
    fail_status_post_data = {
        "overall_last_week": "A",
        "overall_this_week": "A",
        "scope": "A",
        "schedule": "A",
        "cost": "A",
        "overall_health": "A",
        "report": "",
    }

    project_status_post_fail_response=client.post(project_status_fail400_post_url,fail_status_post_data)
    assert project_status_post_fail_response.status_code == 400
    print("project_status fail 400 success", project_status_post_fail_response.status_code)
    print("......................")

    project_status_get_url_id = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/1/"
    get_response_id = client.get(project_status_get_url_id)
    print("get method for projectstatus by id---------", get_response_id.data)
    print("get_response_id",get_response_id.status_code)
    assert get_response_id.status_code == 200
    print("......................")

    project_status_get_url_list = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/"
    get_response_list = client.get(project_status_get_url_list)
    print("get method for projectstatus by list---------", get_response_list.data)
    print("get_response_list",get_response_list.status_code)
    assert get_response_list.status_code == 200
    print("......................")

    #get fail 404 not exists
    project_status_get_url_id = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/6/"
    get_response_id = client.get(project_status_get_url_id)
    assert get_response_id.status_code == 404
    print("......................")

    #put 200 sucess
    project_status_put_url = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/1/"
    status_post_data = {
        "overall_last_week": "G",
        "overall_this_week": "A",
        "scope": "A",
        "schedule": "G",
        "cost": "A",
        "overall_health": "R",
        "report": 6
    }
    project_status_put_response=client.put(project_status_put_url,data=json.dumps(status_post_data), content_type='application/json')
    print(project_status_put_response.data)
    assert project_status_put_response.status_code==200
    print("project status update success", project_status_put_response.status_code)
    print("......................")

    #put fail 400 sucess
    project_status_fail_put_url = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/1/"
    status_fail400_data = {
        "overall_last_week": "G",
        "overall_this_week": "A",
        "scope": "A",
        "schedule": "G",
        "cost": "A",
        "overall_health": "R",
        "report": "",
    }
    project_status_put_fail_400_response=client.put(project_status_fail_put_url,data=json.dumps(status_fail400_data), content_type='application/json')
    print(project_status_put_fail_400_response.data)
    assert project_status_put_fail_400_response.status_code == 400
    print("project status fail 400 success", project_status_put_fail_400_response.status_code)
    print("......................")

    #put fail 404 sucess
    project_status_fail_put_url = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/12/"
    status_fail404_data = {
        "overall_last_week": "G",
        "overall_this_week": "A",
        "scope": "A",
        "schedule": "G",
        "cost": "A",
        "overall_health": "R",
        "report": 6,
    }
    project_status_put_fail_404_response=client.put(project_status_fail_put_url,data=json.dumps(status_fail404_data), content_type='application/json')
    print(project_status_put_fail_404_response.data)
    assert project_status_put_fail_404_response.status_code == 404
    print("project status fail 404 success", project_status_put_fail_404_response.status_code)
    print("......................")

    #patch 200 
    project_status_patch_url = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/1/"
    status_patch_data = {
        "overall_last_week": "G",
        "overall_this_week": "R",
        "scope": "A",
        "schedule": "R",
        "cost": "A",
        "overall_health": "R",
        "report": 6,
    }
    project_status_patch_response=client.patch(project_status_patch_url,data=json.dumps(status_patch_data), content_type='application/json')
    print(project_status_patch_response.data)
    assert project_status_patch_response.status_code == 200
    print("project status patch 200 success", project_status_patch_response.status_code)
    print("......................")

    #patch 400 bad request
    project_status_patch_fail400_url = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/1/"
    status_patch_fail_data = {
        "overall_last_week": "G",
        "overall_this_week": "R",
        "scope": "A",
        "schedule": "R",
        "cost": "A",
        "overall_health": "R",
        "report": "",
    }
    project_status_patch_fail400_response=client.patch(project_status_patch_fail400_url,data=json.dumps(status_patch_fail_data), content_type='application/json')
    print(project_status_patch_fail400_response.data)
    assert project_status_patch_fail400_response.status_code == 400
    print("project status patch 400 success", project_status_patch_fail400_response.status_code)
    print("......................")

    #patch 400 bad request
    project_status_patch_fail404_url = "http://127.0.0.1:8000/api/projectplan/projectstatusapi/13/"
    status_patch_fail_data = {
        "overall_last_week": "G",
        "overall_this_week": "R",
        "scope": "A",
        "schedule": "R",
        "cost": "A",
        "overall_health": "R",
        "report": 6,
    }
    project_status_patch_fail404_response=client.patch(project_status_patch_fail404_url,data=json.dumps(status_patch_fail_data), content_type='application/json')
    print(project_status_patch_fail404_response.data)
    assert project_status_patch_fail404_response.status_code == 404
    print("project status patch 400 success", project_status_patch_fail404_response.status_code)
    print("......................")


    #delete 200 sucess
    delete_url ="http://127.0.0.1:8000/api/projectplan/projectstatusapi/1/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    assert delete_response.status_code==200
    print("......................")

    #delete 404 sucess
    delete_fail_url ="http://127.0.0.1:8000/api/projectplan/projectstatusapi/15/"
    delete_fail404_response =client.delete(delete_fail_url)
    print("delete_response------",delete_fail404_response.data)
    assert delete_fail404_response.status_code == 404
    print("......................")

