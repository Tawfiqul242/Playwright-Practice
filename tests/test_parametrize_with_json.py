import re
import pytest
from playwright.sync_api import expect
from utils.json_read import load_json 


login_data = load_json("test_data/login_data.json")

@pytest.mark.parametrize(
        "username, password",
        [(d["username"], d["password"]) for d in login_data]
)
def test_parametrize_with_json(page, username, password):


    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
   
    page.get_by_role("textbox", name="Username").fill(username)
    
    page.get_by_role("textbox", name="Password").fill(password)
    
    page.get_by_role("button", name="Login").click()
    
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
