import pytest
import json
# from confest import payload
@pytest.mark.django_db
def test_tasktodo_post(client, payload):
    register_response = client.post('http://127.0.0.1:8000/api/user/register/',payload)
    assert register_response.status_code==201
 
    headers = {
        'Authorization': f"Bearer {register_response.data['token']['access']}"
        }
   
    profile_response = client.get("http://127.0.0.1:8000/api/user/profile/", headers=headers)
    assert profile_response.status_code == 200
    
    #post method
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
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/10/"
    response = client.get(url)
    print("---------", response.data)
    print(response.status_code)
    assert response.status_code == 200
    print("......................")

    #main weekly report
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"
    post_data = {
        "title": "my title",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-15",
        "project":response.data['id']
    }
    post_response=client.post(post_url,post_data)
    print(post_response.status_code)
    assert post_response.status_code==201
    print("weeklyreport added success", post_response.status_code)
    print("......................")

    # main tasktodo
     # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/tasktodoapi/"
    post_data = {
        "description":"create model",
        "assignee":"Ankita",
        "report":9
    }
    post_response=client.post(post_url,post_data)
    print(post_response.status_code)
    assert post_response.status_code==201
    print("tasktodo added success", post_response.data)
    print("......................")

    # Fail post method
    fail_post_url = "http://127.0.0.1:8000/api/projectplan/tasktodoapi/"
    fail_post_data = {
        # "description":"create model",
        "assignee":"Ankita",
        "report":9
    }
    fail_post_response=client.post(fail_post_url,fail_post_data)
    print(fail_post_response.status_code)
    assert fail_post_response.status_code==400
    print("tasktodo added success", fail_post_response.data)
    print("......................")

    # get method
    get_url = "http://127.0.0.1:8000/api/projectplan/tasktodoapi/"
    get_response = client.get(get_url)
    print("get method for tasktodo---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

     # get by id
    get_url_id = "http://127.0.0.1:8000/api/projectplan/tasktodoapi/1/"
    get_response_id = client.get(get_url_id)
    print("get method for tasktodo by id---------", get_response_id.data)
    print(get_response_id.status_code)
    assert get_response_id.status_code == 200
    print("......................")

     #Fail get by id
    fail_get_url_id = "http://127.0.0.1:8000/api/projectplan/tasktodoapi/2/"
    fail_get_response_id = client.get(fail_get_url_id)
    print("fail get method for tasktodo by id---------", fail_get_response_id.data)
    print(fail_get_response_id.status_code)
    assert fail_get_response_id.status_code == 404
    print("......................")

    # put method
    put_url = "http://127.0.0.1:8000/api/projectplan/tasktodoapi/1/"
    put_data = {
       "description":"create model and database",
        "assignee":"Ankita",
        "report":9
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.status_code)
    assert put_response.status_code==200
    print("tasktodo update/put success", put_response.status_code)
    print("put method for tasktodo ---------", put_response.data)
    print("......................")

     #fail put method
    fail_put_url = "http://127.0.0.1:8000/api/projectplan/tasktodoapi/1/"
    fail_put_data = {
    #    "description":"create model and database",
        "assignee":"Ankita",
        "report":9
    }
    fail_put_response=client.put(fail_put_url,data=json.dumps(fail_put_data), content_type='application/json')
    print(fail_put_response.status_code)
    assert fail_put_response.status_code==400
    print("tasktodo update/put fail", fail_put_response.data)
    print("......................")

     #fail put by id method
    fail_by_id_put_url = "http://127.0.0.1:8000/api/projectplan/tasktodoapi/2/"
    fail_by_id_put_data = {
        "description":"create model and database",
        "assignee":"Ankita",
        "report":9
    }
    fail_by_id_put_response=client.put(fail_by_id_put_url,data=json.dumps(fail_by_id_put_data), content_type='application/json')
    print(fail_by_id_put_response.status_code)
    assert fail_by_id_put_response.status_code==404
    print("tasktodo update/put fail by id", fail_by_id_put_response.data)
    print("......................")

    # patch method
    patch_url = "http://127.0.0.1:8000/api/projectplan/tasktodoapi/1/"
    patch_data = {
       "description":"create model database",
        "assignee":"Ankita",
        "report":9
    }
    patch_response=client.patch(patch_url,data=json.dumps(patch_data), content_type='application/json')
    print(patch_response.status_code)
    assert patch_response.status_code==200
    print("tasktodo update/patch success",patch_response.status_code)
    print("patch method for tasktodo ---------", patch_response.data)
    print("......................")

    #fail patch method
    fail_patch_url = "http://127.0.0.1:8000/api/projectplan/tasktodoapi/1/"
    fail_patch_data = {
       "description":"create model database",
        "assignee":"Ankita",
        "report":""
    }
    fail_patch_response=client.patch(fail_patch_url,data=json.dumps(fail_patch_data), content_type='application/json')
    print("-=-=-=fail_patch_response-====-",fail_patch_response.status_code, fail_patch_response.data)
    assert fail_patch_response.status_code==400
    print("tasktodo update/patch fail",fail_patch_response.data)
    print("......................")

    #fail patch by id method
    fail_by_id_patch_url = "http://127.0.0.1:8000/api/projectplan/tasktodoapi/2/"
    fail_by_id_patch_data = {
       "description":"create model database",
        "assignee":"Ankita",
        "report":9
    }
    fail_by_id_patch_response=client.patch(fail_by_id_patch_url,data=json.dumps(fail_by_id_patch_data), content_type='application/json')
    print(fail_by_id_patch_response.status_code)
    assert fail_by_id_patch_response.status_code==404
    print("tasktodo update/patch fail",fail_by_id_patch_response.data)
    print("......................")


    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/tasktodoapi/1/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    print("......................")

    #fail delete method
    fail_delete_url ="http://127.0.0.1:8000/api/projectplan/tasktodoapi/2/"
    fail_delete_response =client.delete(fail_delete_url)
    assert fail_by_id_patch_response.status_code==404
    print("delete_response------",fail_delete_response.data)
    print("......................")
