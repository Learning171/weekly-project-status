import pytest
import json
# from confest import payload
@pytest.mark.django_db
def test_accomplishmnet_post(client, payload):
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
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/2/"
    get_response = client.get(url)
    print("---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    #main weekly report
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"
    post_data = {
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-15",
        "project":get_response.data['id']
    }
    post_response=client.post(post_url,post_data)
    print(post_response.status_code)
    assert post_response.status_code==201
    print("weeklyreport added success", post_response.status_code)
    print("......................")


    #main assumption
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/assumptionsapi/"
    post_data = {
         "assumption":"consistency",
        "report":2
    }
    post_response=client.post(post_url,post_data)
    print(post_response.status_code)
    assert post_response.status_code==201
    print("assumption added success", post_response.status_code)
    print("......................")

    # post fail method
    fail_post_url = "http://127.0.0.1:8000/api/projectplan/assumptionsapi/"
    fail_post_data = {
        #  "assumption":"consistency",
        "report":2
    }
    fail_post_response=client.post(fail_post_url,fail_post_data)
    print(fail_post_response.status_code)
    assert fail_post_response.status_code == 400
    print("assumption fail success", fail_post_response.status_code)
    print("......................")

    # get method
    get_url = "http://127.0.0.1:8000/api/projectplan/assumptionsapi/"
    get_response = client.get(get_url)
    print("get method for assumption---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    # get by id
    get_url_id = "http://127.0.0.1:8000/api/projectplan/assumptionsapi/1/"
    get_response_id = client.get(get_url_id)
    print("get method for assumption by id---------", get_response_id.data)
    print(get_response_id.status_code)
    assert get_response_id.status_code == 200
    print("......................")

    # get fail by id
    fail_get_url_id = "http://127.0.0.1:8000/api/projectplan/assumptionsapi/2/"
    fail_get_response_id = client.get(fail_get_url_id)
    print("get method for assumption fail by id---------", fail_get_response_id.data)
    print(fail_get_response_id.status_code)
    assert fail_get_response_id.status_code == 404
    print("......................")

    # put method
    put_url = "http://127.0.0.1:8000/api/projectplan/assumptionsapi/1/"
    put_data = {
            "assumption":"non consistency",
            "report":2
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.status_code)
    assert put_response.status_code==200
    print("assumption update success", put_response.status_code)
    print("......................")

     # put fail method
    fail_put_url = "http://127.0.0.1:8000/api/projectplan/assumptionsapi/1/"
    fail_put_data = {
            "assumption":"non consistency",
            # "report":1
    }
    fail_put_response=client.put(fail_put_url,data=json.dumps(fail_put_data), content_type='application/json')
    print(fail_put_response.status_code)
    assert fail_put_response.status_code == 400
    print("assumption update fail", fail_put_response.data)
    print("......................")

    # put fail by id method
    fail_by_id_put_url = "http://127.0.0.1:8000/api/projectplan/assumptionsapi/2/"
    fail_by_id_put_data = {
            "assumption":"non consistency",
            "report":2
    }
    fail_by_id_put_response=client.put(fail_by_id_put_url,data=json.dumps(fail_by_id_put_data), content_type='application/json')
    print(fail_by_id_put_response.status_code)
    assert fail_by_id_put_response.status_code==404
    print("assumption update fail by id", fail_by_id_put_response.data)
    print("......................")

    # patch method
    patch_url = "http://127.0.0.1:8000/api/projectplan/assumptionsapi/1/"
    patch_data = {
            "assumption":"my assumption",
            "report":2
    }
    patch_response=client.patch(patch_url,data=json.dumps(patch_data), content_type='application/json')
    assert patch_response.status_code==200
    print("assumption partial update success", patch_response.data)
    print("......................")

    # patch fail method
    failpatch_url = "http://127.0.0.1:8000/api/projectplan/assumptionsapi/1/"
    failpatch_data = {
            "assumption":"assumpton",
            "report":""
     }
    failpatch_response=client.patch(failpatch_url,data=json.dumps(failpatch_data), content_type='application/json')
    assert failpatch_response.status_code == 400
    print("assumption partial update fail", failpatch_response.data)
    print("......................")

    # patch fail by id method
    failpatch_by_id_url = "http://127.0.0.1:8000/api/projectplan/assumptionsapi/4/"
    failpatch_by_id_data = {
            "assumption":"assumpton",
            "report":2
     }
    failpatch_by_id_response=client.patch(failpatch_by_id_url,data=json.dumps(failpatch_by_id_data), content_type='application/json')
    assert failpatch_by_id_response.status_code == 404
    print("assumption partial update fail by id", failpatch_by_id_response.data)
    print("......................")

    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/assumptionsapi/1/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    assert delete_response.status_code == 200
    print("......................")

    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/assumptionsapi/4/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    assert delete_response.status_code == 404
    print("......................")

