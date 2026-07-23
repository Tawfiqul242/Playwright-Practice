import re
import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize(
        "username, password",
        [
            ("Admin", "admin123"),
            ("user1", "user123")
        ]
)
def test_parametrize_example(page, username, password):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
   
    page.get_by_role("textbox", name="Username").fill(username)
    
    page.get_by_role("textbox", name="Password").fill(password)
    
    page.get_by_role("button", name="Login").click()
    
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
