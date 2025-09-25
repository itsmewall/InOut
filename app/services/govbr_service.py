import requests
from flask import current_app

def get_login_url():
    base_url = current_app.config["GOVBR_AUTH_URL"]
    client_id = current_app.config["GOVBR_CLIENT_ID"]
    redirect_uri = current_app.config["GOVBR_REDIRECT_URI"]
    scope = "openid email profile"
    return f"{base_url}/authorize?response_type=code&client_id={client_id}&scope={scope}&redirect_uri={redirect_uri}"

def exchange_code_for_token(code: str):
    token_url = current_app.config["GOVBR_TOKEN_URL"]
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": current_app.config["GOVBR_REDIRECT_URI"],
        "client_id": current_app.config["GOVBR_CLIENT_ID"],
        "client_secret": current_app.config["GOVBR_CLIENT_SECRET"],
    }
    response = requests.post(token_url, data=data)
    response.raise_for_status()
    return response.json()

def get_user_info(access_token: str):
    userinfo_url = current_app.config["GOVBR_USERINFO_URL"]
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(userinfo_url, headers=headers)
    response.raise_for_status()
    return response.json()