import pytest
import json

@pytest.mark.django_db
def test_dependency_post(client, payload):
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
    print("---get method------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    # weekly report
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"
    post_data = {
        "title": "my title",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-15",
        "project":get_response.data['id']
    }
    post_response=client.post(post_url,post_data)
    print(post_response.status_code)
    assert post_response.status_code==201
    print("weeklyreport added success", post_response.status_code)
    print("......................")

    # get method
    get_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"
    get_response = client.get(get_url)
    print("get method for weeklyreport---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")


    #main dependency report
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/dependancyapi/"
    post_data = {
        "dependency_description":"dependency description",
        "target_completion_date":"2023-09-10",
        "responsible_party":"responsible party",
        "RAGStatus":"R",
        "report":2
    }
    post_response=client.post(post_url,post_data)
    print(post_response.status_code)
    assert post_response.status_code==201
    print("Dependency  added success", post_response.status_code)
    print("......................")

    # get method
    get_url = "http://127.0.0.1:8000/api/projectplan/dependancyapi/"
    get_response = client.get(get_url)
    print("get method for Dependency ---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    # get by id
    get_url_id = "http://127.0.0.1:8000/api/projectplan/dependancyapi/1/"
    get_response_id = client.get(get_url_id)
    print("get method for Dependency  by id---------", get_response_id.data)
    print(get_response_id.status_code)
    assert get_response_id.status_code == 200
    print("......................")

    # put method
    put_url = "http://127.0.0.1:8000/api/projectplan/dependancyapi/1/"
    put_data = {
        "dependency_description":"dependency description",
        "target_completion_date":"2023-09-10",
        "responsible_party":"responsible party",
        "RAGStatus":"G",
        "report":2
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.status_code)
    assert put_response.status_code==200
    print("Dependency update success", put_response.status_code)
    print("......................")

    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/dependancyapi/1/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    print("......................")

