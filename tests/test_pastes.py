from fastapi.testclient import TestClient
from app.main import app

client= TestClient(app)

def test_create_and_read_pastes():
    create_response=client.post(
        '/pastes',
        json={'content':'hello world'}
    )
    assert create_response.status_code==201
    data=create_response.json()
    paste_id=data['id']
    get_response=client.get(f'/pastes/{paste_id}')
    assert get_response.status_code==200
    assert get_response.json()['content']=='hello world'