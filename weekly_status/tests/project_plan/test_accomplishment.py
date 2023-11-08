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

    # get method accomplishment by list
    get_url = "http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/"
    get_response = client.get(get_url)
    print("accomplishment get 200",get_response.status_code, get_response.data)
    assert get_response.status_code == 200
    print("-=-----=-----=----=---=---=---=")

    # get method accomplishment by id
    get_url = "http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/1/"
    get_response = client.get(get_url)
    print("accomplishment get by id 200 ",get_response.status_code, get_response.data)
    assert get_response.status_code == 200
    print("-=-----=-----=----=---=---=---=")

    #get fail 404
    get_url = "http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/4/"
    get_response = client.get(get_url)
    print("accomplishment get fail 404 ",get_response.status_code, get_response.data)
    assert get_response.status_code == 404
    print("-=-----=-----=----=---=---=---=")


     # put method
    put_url = "http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/1/"
    put_data = {
            "Description":"non consistency",
            "report":1
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.status_code, put_response.data)
    assert put_response.status_code == 200
    print("accomplishment update success", put_response.status_code)
    print("......................")


    # put method 400 fail
    put_url = "http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/1/"
    put_data = {
            "Description":"non consistency",
            "report":""
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.status_code, put_response.data)
    assert put_response.status_code == 400
    print("accomplishment fail 400 success", put_response.status_code)
    print("......................")


    # put method 404 fail
    put_url = "http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/3/"
    put_data = {
            "Description":"non consistency",
            "report":1
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.status_code, put_response.data)
    assert put_response.status_code == 404
    print("accomplishment fail 404 success", put_response.status_code)
    print("......................")

    # patch method 200
    patch_url = "http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/1/"
    patch_data = {
         "Description":"understand",
         "report": 1
    }
    patch_response=client.patch(patch_url,data=json.dumps(patch_data), content_type='application/json')
    print(patch_response.status_code)
    assert patch_response.status_code == 200
    print("accomplishment patch  update success", patch_response.status_code)
    print("......................")

    # patch method 400
    patch_url = "http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/1/"
    patch_data = {
         "Description":"understand",
         "report": ""
    }
    patch_response=client.patch(patch_url,data=json.dumps(patch_data), content_type='application/json')
    print(patch_response.status_code)
    assert patch_response.status_code == 400
    print("accomplishment patch fail 400 success", patch_response.status_code)
    print("......................")

    # patch method 404
    patch_url = "http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/4/"
    patch_data = {
         "Description":"understand",
         "report": 1
    }
    patch_response=client.patch(patch_url,data=json.dumps(patch_data), content_type='application/json')
    print(patch_response.status_code)
    assert patch_response.status_code == 404
    print("accomplishment patch fail 404 success", patch_response.status_code)
    print("......................")


    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/1/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    assert delete_response.status_code == 200
    print("......................")

    # delete fail method
    delete_url ="http://127.0.0.1:8000/api/projectplan/accomplishmentsapi/4/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    assert delete_response.status_code == 404
    print("......................")

