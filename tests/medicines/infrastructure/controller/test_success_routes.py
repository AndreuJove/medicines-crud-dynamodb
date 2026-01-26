from chalice.test import Client


def test_index_function(test_client: Client) -> None:
    http_response = test_client.http.get("/")
    assert http_response.json_body == {
        "status": "healthy",
        "version": "1.0.0",
    }
    assert http_response.status_code == 200


def test_get_user_by_drug_name(test_client, temp_medicine_user):
    response = test_client.http.get("/medicines/TestDrug_001")
    assert response.status_code == 200
    assert response.json_body == {'drug_name': 'TestDrug_001', 'target': 'IntegrationTest'}

def test_endpoint_not_found(test_client):
    response = test_client.http.get("/medicines/TestDrug_002")
    assert response.status_code == 404
    assert response.json_body == {'Status': 'Not found'}
