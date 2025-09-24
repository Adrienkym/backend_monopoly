def test_roll_dice(client):
    response = client.post("/game/roll_dice/1")
    assert response.status_code == 200
    data = response.get_json()
    assert "dice" in data