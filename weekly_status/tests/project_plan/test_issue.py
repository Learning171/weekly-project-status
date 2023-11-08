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
    print("-=-====--=-=-=projectsapi-=-=-=-=-=-=-=",response.data)
    assert response.status_code==201
    print("Project added success", response.status_code)
    print("......................")
   
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/4/"
    get_response = client.get(url)
    print("-----test_projects_get----", get_response.data)
    print(get_response.status_code)
    assert response.status_code == 201

    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"
    post_data = {
        "title": "my title",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-15",
        "project":get_response.data['id']
    }
    post_response=client.post(post_url,post_data)
    print(post_response.data)
    assert post_response.status_code==201
    print("weeklyreport added success", post_response.status_code)
    print("......................")
    
    get_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/4/"
    get_response = client.get(get_url)
    print("-=-=-=-=-=-=-=get weekly response issue-=-==-", get_response.data)
    assert get_response.status_code == 200
    print("=---=-=-=-=-=-=-=-=---=-=-=-=-=-=")
    # main issue test case
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/issueapi/"
    post_data = {
        "issue_description":"kay value binding",
        "severity":"medium",
        "complexity":"project is complex",
        "impact":"bad",
        "responsible_party":"self",
        "RAGStatus":"A",
        "report":get_response.data['id']
    }
    post_response=client.post(post_url,post_data)
    assert post_response.status_code==201
    print("issue added success", post_response.data)
    print(post_response.status_code)
    print(".........-=-=-=-=-=-=.............")

    # Post fail
    fail_post_url = "http://127.0.0.1:8000/api/projectplan/issueapi/"
    fail_post_data = {
        "issue_description":"kay value binding",
        "severity":"medium",
        "complexity":"project is complex",
        "impact":"bad",
        "responsible_party":"self",
        "RAGStatus":"A",
        "report":""
    }
    fail_post_response=client.post(fail_post_url,fail_post_data)
    assert fail_post_response.status_code == 400
    print("issue added success", fail_post_response.data)
    print(fail_post_response.status_code)
    print(".........-=-=-=-=-=-=.............")

    # get method
    get_url ="http://127.0.0.1:8000/api/projectplan/issueapi/"
    get_response = client.get(get_url)
    print("get method for issue---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    # get method by id
    get_url ="http://127.0.0.1:8000/api/projectplan/issueapi/1/"
    get_response = client.get(get_url)
    print("get method for issue by id---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    # get method fail
    fail_get_url ="http://127.0.0.1:8000/api/projectplan/issueapi/3/"
    fail_get_response = client.get(fail_get_url)
    print("get method fail 404---------", fail_get_response.data)
    print(fail_get_response.status_code)
    assert fail_get_response.status_code == 404
    print("......................")

     # put method
    put_url = "http://127.0.0.1:8000/api/projectplan/issueapi/1/"
    put_data = {
        "issue_description":"project not on time",
        "severity":"high",
        "complexity":"project is complex",
        "impact":"bad",
        "responsible_party":"developers",
        "RAGStatus":"R",
        "report":4
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.data)
    assert put_response.status_code==200
    print("issue update success", put_response.status_code)
    print("......................")


    # patch method
    patch_url = "http://127.0.0.1:8000/api/projectplan/issueapi/1/"
    patch_data = {
        "issue_description":"project not on time",
        "severity":"high",
        "complexity":"project is complex",
        "impact":"bad",
        "responsible_party":"developers",
        "RAGStatus":"R",
        "report":4
    }
    patch_response=client.patch(patch_url,data=json.dumps(patch_data), content_type='application/json')
    print(patch_response.data)
    assert patch_response.status_code==200
    print("issue patch update success", patch_response.status_code)
    print("......................")

    # patch method fail 400
    fail_patch_url = "http://127.0.0.1:8000/api/projectplan/issueapi/1/"
    fail_patch_data = {
        "issue_description":"project not on time",
        "severity":"high",
        "complexity":"project is complex",
        "impact":"bad",
        "responsible_party":"developers",
        "RAGStatus":"R",
        "report":""
    }
    fail_patch_response=client.patch(fail_patch_url,data=json.dumps(fail_patch_data), content_type='application/json')
    print(fail_patch_response.data)
    assert fail_patch_response.status_code == 400
    print("issue 400 fail success", fail_patch_response.status_code)
    print("......................")

    # patch method fail 404
    fail404_patch_url = "http://127.0.0.1:8000/api/projectplan/issueapi/5/"
    fail404_patch_data = {
        "issue_description":"project not on time",
        "severity":"high",
        "complexity":"project is complex",
        "impact":"bad",
        "responsible_party":"developers",
        "RAGStatus":"R",
        "report":4
    }
    fail404_patch_response=client.patch(fail404_patch_url,data=json.dumps(fail404_patch_data), content_type='application/json')
    print(fail404_patch_response.data)
    assert fail404_patch_response.status_code == 404
    print("issue 404 fail success", fail_patch_response.status_code)
    print("......................")

    #put 400 bad request
    fail_put_url = "http://127.0.0.1:8000/api/projectplan/issueapi/1/"
    fail_put_data = {
        "issue_description":"project not on time",
        "severity":"high",
        "complexity":"project is complex",
        "impact":"bad",
        "responsible_party":"developers",
        "RAGStatus":"R",
        "report":""
    }
    fail_put_response=client.put(fail_put_url,data=json.dumps(fail_put_data), content_type='application/json')
    print(fail_put_response.data)
    assert fail_put_response.status_code == 400
    print("issue fail 400 success", put_response.status_code)
    print("......................")

    #put 404 not found request
    fail404_put_url = "http://127.0.0.1:8000/api/projectplan/issueapi/4/"
    fail404_put_data = {
        "issue_description":"project not on time",
        "severity":"high",
        "complexity":"project is complex",
        "impact":"bad",
        "responsible_party":"developers",
        "RAGStatus":"R",
        "report":4
    }
    fail404_put_response=client.put(fail404_put_url,data=json.dumps(fail404_put_data), content_type='application/json')
    print(fail404_put_response.data)
    assert fail404_put_response.status_code == 404
    print("issue fail 404 success", fail404_put_response.status_code)
    print("......................")

    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/issueapi/1/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    assert delete_response.status_code==200
    print("......................")

    # delete fail 404 method
    delete_fail404_url ="http://127.0.0.1:8000/api/projectplan/issueapi/3/"
    delete_fail404_response =client.delete(delete_fail404_url)
    print("delete_response------",delete_fail404_response.data)
    assert delete_fail404_response.status_code==404
    print("......................")