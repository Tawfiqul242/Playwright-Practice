import re
from playwright.sync_api import expect


def test_example(page):
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
   
    page.get_by_role("textbox", name="Username").fill("Admin")
    
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("listitem").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
