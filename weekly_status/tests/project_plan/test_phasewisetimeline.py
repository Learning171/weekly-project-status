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
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/5/"
    get_response = client.get(url)
    print("-=-=-=-=-get response phasewise-==-=-=-=",get_response.data)
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
    post_response=client.post(post_url,post_data)
    assert post_response.status_code==201
    print("......................")

    get_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/5/"
    get_response = client.get(get_url)
    print("-=-=-=-=-=-=-=get weekly response issue-=-==-", get_response.data)
    assert get_response.status_code == 200

    #main phasewisetimeline 
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/"
    post_data_phasewise = { 
    "timeline_title":f'{post_data["title"]}',
    "report":5
    }
    post_response=client.post(post_url,post_data_phasewise)
    assert post_response.status_code==201
    print(" phasewisetimeline  added success", post_response.status_code)
    print("......................")

    #Post 400 fail
    post_fail400_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/"
    post_fail_data_phasewise = { 
    "timeline_title":f'{post_data["title"]}',
    "report":"",
    }
    post_fail400_response=client.post(post_fail400_url,post_fail_data_phasewise)
    assert post_fail400_response.status_code == 400
    print(" phasewisetimeline  fail 400 success", post_fail400_response.status_code)
    print("......................")

    # get method
    get_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/"
    get_response = client.get(get_url)
    print("get method for  phasewisetimeline ---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    # get by id
    get_url_id = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/2/"
    get_response_id = client.get(get_url_id)
    print("get method for  phasewisetimeline  by id---------", get_response_id.data)
    print(get_response_id.status_code)
    assert get_response_id.status_code == 200
    print("......................")
    
    #get fail 404
    get_url_fail404 = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/12/"
    get_response_fail404 = client.get(get_url_fail404)
    print("get method for  phasewisetimeline  by id fail 404---------", get_response_fail404.data)
    print(get_response_fail404.status_code)
    assert get_response_fail404.status_code == 404
    print("......................")

    # put method
    put_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/2/"
    put_data = {
    "title": "my title 1",
    "timeline_title":"timeline_title1",
    "report":5
    }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.status_code)
    assert put_response.status_code==200
    print("phasewisetimeline  update success", put_response.status_code)
    print("......................")

    # put 400 fail method
    put_fail_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/2/"
    put_fail_data = {
    "title": "my title 1",
    "timeline_title":"timeline_title1",
    "report":"",
    }
    put_fail_response=client.put(put_fail_url,data=json.dumps(put_fail_data), content_type='application/json')
    print(put_fail_response.status_code)
    assert put_fail_response.status_code == 400
    print("phasewisetimeline  400 success", put_fail_response.status_code)
    print("......................")

    # put 404 fail method
    put_fail404_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/12/"
    put_fail_data = {
    "title": "my title 1",
    "timeline_title":"timeline_title1",
    "report":5,
    }
    put_fail404_response=client.put(put_fail404_url,data=json.dumps(put_fail_data), content_type='application/json')
    print(put_fail404_response.status_code)
    assert put_fail404_response.status_code == 404
    print("phasewisetimeline  404 success", put_fail404_response.status_code)
    print("......................")

    #patch 200 sucess
    patch_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/2/"
    patch_data = {
    "timeline_title":"timeline_title3",
    "report":5
    }
    patch_response=client.patch(patch_url,data=json.dumps(patch_data), content_type='application/json')
    print(patch_response.status_code)
    assert patch_response.status_code==200
    print("phasewisetimeline  patch 200 success", patch_response.data)
    print("......................")

    #patch 400 sucess
    patch_fail400_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/2/"
    patch_fail_data = {
    "timeline_title":"timeline_title3",
    "report":"",
    }
    patch_fail400_response=client.patch(patch_fail400_url,data=json.dumps(patch_fail_data), content_type='application/json')
    print(patch_fail400_response.status_code)
    assert patch_fail400_response.status_code == 400
    print("phasewisetimeline  patch 400 success", patch_fail400_response.data)
    print("......................")

    #patch 404 sucess
    patch_fail404_url = "http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/12/"
    patch_fail404_data = {
    "timeline_title":"timeline_title3",
    "report":5
    }
    patch_fail404_response=client.patch(patch_fail404_url,data=json.dumps(patch_fail404_data), content_type='application/json')
    print(patch_fail404_response.status_code)
    assert patch_fail404_response.status_code == 404
    print("phasewisetimeline  patch 404 success", patch_fail404_response.data)
    print("......................")

    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/2/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    assert delete_response.status_code == 200
    print("......................")

    # delete 404 method
    delete_fail_url ="http://127.0.0.1:8000/api/projectplan/phasewisetimelineapi/12/"
    delete_fail_response =client.delete(delete_fail_url)
    print("delete_response 404------",delete_fail_response.data)
    assert delete_fail_response.status_code == 404

    print("......................")

