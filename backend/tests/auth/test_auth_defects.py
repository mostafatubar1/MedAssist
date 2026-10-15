def test_duplicate_signup_and_wrong_password_are_rejected(client):
    payload = {"email": "doctor@example.com", "password": "strong-password", "role": "doctor"}
    first = client.post("/api/auth/signup", json=payload)
    assert first.status_code == 201

    duplicate = client.post("/api/auth/signup", json=payload)
    assert duplicate.status_code == 409

    wrong_password = client.post("/api/auth/login", json={"email": payload["email"], "password": "wrong-password"})
    assert wrong_password.status_code == 401


def test_role_protection_blocks_patient_from_doctor_dashboard(client):
    signup = client.post("/api/auth/signup", json={
        "email": "patient2@example.com",
        "password": "strong-password",
        "role": "patient",
    })
    token = signup.json()["access_token"]
    response = client.get("/api/dashboard/queue", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403


def test_admin_self_signup_is_blocked(client):
    response = client.post("/api/auth/signup", json={
        "email": "admin@example.com",
        "password": "strong-password",
        "role": "admin",
    })
    assert response.status_code == 403
