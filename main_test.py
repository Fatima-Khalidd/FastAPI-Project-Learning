from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

def test_home():
    response=client.get("/")
    #status code check 
    assert response.status_code==200
    # format check 
    assert response.json() =={"message":"Hello Fatima"}

# test add api
def test_add():
    response=client.get("/add?a=5&b=5")
    assert response.status_code==200
    assert response.json()=={"result":10}