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
    print(response.data)
    assert response.status_code==201
    print("Project added success", response.status_code)
    print("......................")
   
    
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"
    post_data = {
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-15",
        "project":1
    }
    post_response=client.post(post_url,post_data)
    print(post_response.data)
    assert post_response.status_code==201
    print("weeklyreport added success", post_response.status_code)
    print("......................")

    # main risk test case
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/issueapi/"
    post_data = {
        "issue_description":"kay value binding",
        "severity":"medium",
        "complexity":"project is complex",
        "impact":"bad",
        "responsible_party":"self",
        "RAGStatus":"A",
        "report":1
    }
    post_response=client.post(post_url,post_data)
    assert post_response.status_code==201
    print("issue added success", post_response.data)
    print(post_response.status_code)
    print("......................")

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

     # put method
    put_url = "http://127.0.0.1:8000/api/projectplan/issueapi/1/"
    put_data = {
        "issue_description":"project not on time",
        "severity":"high",
        "complexity":"project is complex",
        "impact":"bad",
        "responsible_party":"developers",
        "RAGStatus":"R",
        "report":1
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.data)
    assert put_response.status_code==200
    print("issue update success", put_response.status_code)
    print("......................")

    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/issueapi/1/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    assert delete_response.status_code==200
    print("......................")