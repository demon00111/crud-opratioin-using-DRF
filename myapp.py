import requests
import json



URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    stu= {}
    if id is not None:
        stu={'id': id}
    json_data= json.dumps(stu)
    r = requests.get(url=URL ,data=json_data)
    data= r.json()
    print(data)

# get_data(7)


def edit_data():
        
    stu=    {
        'name': 'shivaaaaa',
        'role':'202'
    }
    json_data= json.dumps(stu)
    r = requests.post(url=URL ,data=json_data)
    data= r.json()
    print(data)

edit_data()     

def update_data():
    stu={
        'id': 5,
        'name': 'd',
        # 'role': '100'
    }
    json_data = json.dumps(stu)
    r = requests.put(url=URL, data= json_data)
    data = r.json()
    print(data)


update_data()

def delete_data(id=None):
    stu= {}
    if id is not None:
        stu={'id': id}
    json_data= json.dumps(stu)
    r = requests.delete(url=URL ,data=json_data)
    data= r.json()
    print(data)

# delete_data(1)
