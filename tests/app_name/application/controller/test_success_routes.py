from chalice.test import Client


def test_index_function(test_client: Client) -> None:
    http_response = test_client.http.get("/")
    assert http_response.json_body == {
        "status": "healthy",
        "version": "1.0.0",
    }
    assert http_response.status_code == 200
