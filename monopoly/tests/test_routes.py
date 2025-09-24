def test_add_player(client):
    response = client.post("/player/", json={"name": "Alice"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Alice"
