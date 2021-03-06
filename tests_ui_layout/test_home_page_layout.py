from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright
import pytest


# @pytest.mark.skip(reason="just skipped")
@pytest.mark.integration
def test_about_us_section_verbiage(playwright):
    # Assess - Given
    browser = playwright.firefox.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.set_default_timeout(3000)

    assert page.is_visible(HomePage.celebrating_beauty_header)
    # Click text=playwright-practice was founded by a group of like-minded fashion devotees, dete
    assert page.is_visible(HomePage.celebrating_beauty_body)

    # context.close()
    # browser.close()


@pytest.mark.skip(reason="just skipped")
@pytest.mark.regression
def test_about_us_section_verbiage_2(playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.click(HomePage.celebrating_beauty_header)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    assert page.is_visible(HomePage.celebrating_beauty_header)
    # Click text=playwright-practice was founded by a group of like-minded fashion devotees, dete
    assert page.is_visible(HomePage.celebrating_beauty_body)

    # context.close()
    # browser.close()