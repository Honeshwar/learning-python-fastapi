# importing a client that help to run our app on client and give client to access api calls,
#  from which we call app to get response eg, postman,thunder,... similar
from fastapi.testclient import TestClient
# import main to access app and run server for this application
import main 
# import status to check response status validation
from fastapi import status

# create an client instance
client = TestClient(main.app)

def test_healthy_api():
    response = client.get('/healthy')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status':"healthy"}