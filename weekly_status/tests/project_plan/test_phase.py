import pytest
import json

@pytest.mark.django_db
def test_phase_post(client, payload):
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
        
    "timeline_title":"timeline_title",
    "report":1
    }
    post_response=client.post(post_url,post_data)
    assert post_response.status_code==201
    print(" phasewisetimeline  added success", post_response.status_code)
    print("......................")

     #main phase 
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/phaseviewapi/"
    post_data = {
         "phase_name":"Prepare",
        "planned_start_date":"2023-09-10",
        "planned_end_date":"2023-09-13",
        "revised_end_date":"2023-09-14",
        "status":"R",
        "remark":"remark",
         "timeline":1
    }
    post_response=client.post(post_url,post_data)
    print(post_response.status_code)
    assert post_response.status_code==201
    print(" phase  added success", post_response.status_code)
    print("......................")

    # get method
    get_url = "http://127.0.0.1:8000/api/projectplan/phaseviewapi/"
    get_response = client.get(get_url)
    print("get method for  phase ---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    # get by id
    get_url_id = "http://127.0.0.1:8000/api/projectplan/phaseviewapi/1/"
    get_response_id = client.get(get_url_id)
    print("get method for  phase  by id---------", get_response_id.data)
    print(get_response_id.status_code)
    assert get_response_id.status_code == 200
    print("......................")

    # put method
    put_url = "http://127.0.0.1:8000/api/projectplan/phaseviewapi/1/"
    put_data = {
         "phase_name":"Realize",
        "planned_start_date":"2023-09-10",
        "planned_end_date":"2023-09-13",
        "revised_end_date":"2023-09-14",
        "status":"G",
        "remark":"remark",
        "timeline":1
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.status_code)
    assert put_response.status_code==200
    print("phase  update success", put_response.status_code)
    print("......................")

    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/phaseviewapi/1/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    print("......................")

