import pytest
import json

@pytest.mark.django_db
def test_phasewisetimeline_post(client, payload):
    # User Registration

    register_response = client.post('http://127.0.0.1:8000/api/user/register/',payload)
    assert register_response.status_code==201
 
    headers = {
        'Authorization': f"Bearer {register_response.data['token']['access']}"
        }
   
    profile_response = client.get("http://127.0.0.1:8000/api/user/profile/", headers=headers)
    assert profile_response.status_code == 200
 

    #post method for Phasewise timeline
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
    assert response.status_code==201
    
   
    # get method
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/"
    response = client.get(url)
    assert response.status_code == 200
    print("......................")

    #main weekly report
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/"
    post_data = {
        "title": "my title",
        "week_start_date":"2023-09-10",
        "week_end_date":"2023-09-15",
        "project":1
    }
    post_response=client.post(post_url,post_data)
    assert post_response.status_code==201
    print("......................")

    #main phasewisetimeline 
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/"
    post_data = {
        
    "timeline_title":f'{post_data["title"]}',
    "report":1
    }
    post_response=client.post(post_url,post_data)
    assert post_response.status_code==201
    print(" phasewisetimeline  added success", post_response.status_code)
    print("......................")

    # get method
    get_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/"
    get_response = client.get(get_url)
    print("get method for  phasewisetimeline ---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    # get by id
    get_url_id = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/1/"
    get_response_id = client.get(get_url_id)
    print("get method for  phasewisetimeline  by id---------", get_response_id.data)
    print(get_response_id.status_code)
    assert get_response_id.status_code == 200
    print("......................")

    # put method
    put_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/1/"
    put_data = {
    "title": "my title 1",
    "timeline_title":"timeline_title1",
    "report":1
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.status_code)
    assert put_response.status_code==200
    print("phasewisetimeline  update success", put_response.status_code)
    print("......................")

    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/1/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    print("......................")

