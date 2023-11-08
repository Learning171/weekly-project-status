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
    
    url = "http://127.0.0.1:8000/api/projectplan/projectsapi/9/"
    get_response = client.get(url)
    print("-----test_projecstatus_get----", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    
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

    get_url = "http://127.0.0.1:8000/api/projectplan/weeklyreportapi/8/"
    get_response = client.get(get_url)
    print("-=-=-=-=-=-=-=get weekly response issue-=-==-", get_response.data)
    assert get_response.status_code == 200

    # main risk test case
    # post method
    post_url = "http://127.0.0.1:8000/api/projectplan/riskapi/"
    post_data = {
        "risk_description":"project not on time",
        "severity":"medium",
        "complexity":"project is complex",
        "impact":"bad",
        "mitigation_plan":"risk lokhande",
        "RAGStatus":"A",
        "report":8
    }
    post_response=client.post(post_url,post_data)
    assert post_response.status_code==201
    print("risk added success", post_response.data)
    print(post_response.status_code)
    print("......................")

    #risk post fail 400
    #post_fail_url = "http://127.0.0.1:8000/api/projectplan/riskapi/"
    post_fail_data = {
        "risk_description":"project not on time",
        "severity":"medium",
        "complexity":"project is complex",
        "impact":"bad",
        "mitigation_plan":"risk lokhande",
        "RAGStatus":"A",
        "report":""
    }
    post_fail_response=client.post(post_url,post_fail_data)
    assert post_fail_response.status_code == 400
    print("risk post fail 400 success", post_fail_response.data)
    print(post_fail_response.status_code)
    print("......................")

    # get method
    get_url ="http://127.0.0.1:8000/api/projectplan/riskapi/"
    get_response = client.get(get_url)
    print("get method for risk---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    # get method by id
    get_url ="http://127.0.0.1:8000/api/projectplan/riskapi/1/"
    get_response = client.get(get_url)
    print("get method for risk by id---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 200
    print("......................")

    # get method fail 404
    get_url ="http://127.0.0.1:8000/api/projectplan/riskapi/3/"
    get_response = client.get(get_url)
    print("get method fail 404 ---------", get_response.data)
    print(get_response.status_code)
    assert get_response.status_code == 404
    print("......................")

     # put method
    put_url = "http://127.0.0.1:8000/api/projectplan/riskapi/1/"
    put_data = {
        "risk_description":"project not on time",
        "severity":"high",
        "complexity":"project is complex",
        "impact":"bad",
        "mitigation_plan":"risk lokhande",
        "RAGStatus":"R",
        "report": 8
                }
    put_response=client.put(put_url,data=json.dumps(put_data), content_type='application/json')
    print(put_response.status_code)
    assert put_response.status_code==200
    print("risk update success", put_response.status_code)
    print("......................")

    #risk put fail 400
    # put method
    put_fail_url = "http://127.0.0.1:8000/api/projectplan/riskapi/1/"
    put_fail_data = {
        "risk_description":"project not on time",
        "severity":"high",
        "complexity":"project is complex",
        "impact":"bad",
        "mitigation_plan":"risk lokhande",
        "RAGStatus":"R",
        "report": ""
                }
    put_fail_response=client.put(put_fail_url,data=json.dumps(put_fail_data), content_type='application/json')
    print(put_fail_response.status_code)
    assert put_fail_response.status_code == 400
    print("risk put fail 400 success", put_fail_response.status_code)
    print("......................")

    #risk put fail 404
    put_fail404_url = "http://127.0.0.1:8000/api/projectplan/riskapi/4/"
    put_fail404_data = {
        "risk_description":"project not on time",
        "severity":"high",
        "complexity":"project is complex",
        "impact":"bad",
        "mitigation_plan":"risk lokhande",
        "RAGStatus":"R",
        "report": 8
                }
    put_fail404_response=client.put(put_fail404_url,data=json.dumps(put_fail404_data), content_type='application/json')
    print(put_fail404_response.status_code)
    assert put_fail404_response.status_code == 404
    print("risk put fail 404 success", put_fail404_response.status_code)
    print("......................")

    # patch method
    patch_url = "http://127.0.0.1:8000/api/projectplan/riskapi/1/"
    patch_data = {
        "risk_description":"project not on time",
        "severity":"medium",
        "complexity":"project is complex",
        "impact":"bad",
        "mitigation_plan":"risk lokhande",
        "RAGStatus":"R",
        "report": 8
                }
    patch_response=client.patch(patch_url,data=json.dumps(patch_data), content_type='application/json')
    print(patch_response.status_code, patch_response.data)
    assert patch_response.status_code==200
    print("risk patch update success", patch_response.status_code)
    print("......................")


    # patch method 400
    patch_url = "http://127.0.0.1:8000/api/projectplan/riskapi/1/"
    patch_data = {
        "risk_description":"project not on time",
        "severity":"medium",
        "complexity":"project is complex",
        "impact":"bad",
        "mitigation_plan":"risk lokhande",
        "RAGStatus":"R",
        "report": ""
                }
    patch_response=client.patch(patch_url,data=json.dumps(patch_data), content_type='application/json')
    print(patch_response.status_code, patch_response.data)
    assert patch_response.status_code == 400
    print("risk patch update success", patch_response.status_code)
    print("......................")

    # patch method 404
    patch_url = "http://127.0.0.1:8000/api/projectplan/riskapi/3/"
    patch_data = {
        "risk_description":"project not on time",
        "severity":"medium",
        "complexity":"project is complex",
        "impact":"bad",
        "mitigation_plan":"risk lokhande",
        "RAGStatus":"R",
        "report": 8
                }
    patch_response=client.patch(patch_url,data=json.dumps(patch_data), content_type='application/json')
    print(patch_response.status_code, patch_response.data)
    assert patch_response.status_code == 404
    print("risk patch update success", patch_response.status_code)
    print("......................")


    # delete method
    delete_url ="http://127.0.0.1:8000/api/projectplan/riskapi/1/"
    delete_response =client.delete(delete_url)
    print("delete_response------",delete_response.data)
    print("......................")

    # delete method fail 404
    delete_url ="http://127.0.0.1:8000/api/projectplan/riskapi/3/"
    delete_response =client.delete(delete_url)
    assert delete_response.status_code == 404
    print("delete_response------",delete_response.data)
    print("......................")
