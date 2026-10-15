def test_patient_can_signup_login_and_read_profile(client):
    signup = client.post("/api/auth/signup", json={
        "email": "patient@example.com",
        "password": "correct-horse-battery",
        "role": "patient",
    })
    assert signup.status_code == 201
    token = signup.json()["access_token"]
    assert signup.json()["user"]["role"] == "patient"

    me = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me.status_code == 200
    assert me.json()["email"] == "patient@example.com"

    login = client.post("/api/auth/login", json={
        "email": "patient@example.com",
        "password": "correct-horse-battery",
    })
    assert login.status_code == 200
    assert login.json()["token_type"] == "bearer"
