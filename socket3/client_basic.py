import requests
import json


def main():
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}

    # Example 
    payload = {
        "method": "echo",
        "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    assert response["result"] == "echome!"
    assert response["jsonrpc"]
    assert response["id"] == 0

    print("First method successfull")

    payload = {
        "method": "add",
        "params": [5,4],
        "jsonrpc": "2.0",
        "id": 0,
    }

    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    
    print response["result"]
    print("Second method successfull")


    payload = {
        "method": "writefile",
        "params": {"token": "FRZSXSQ912se3SL","filename": "test.txt", "data": "This is my test to transfer data and create a file at the server"},
        "jsonrpc": "2.0",
        "id": 0,
    }

    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    
    print response["result"]
    print("Third  method successfull")




if __name__ == "__main__":
    main()
