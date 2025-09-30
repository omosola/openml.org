def login(test_client, email, password):
    response = test_client.post(
        "/login", json={"email": email, "password": password}, follow_redirects=True
    )
    return response
