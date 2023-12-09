from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github(browser_configs):
    browser.open("https://github.com")
    s(".header-search-button").click()
    s("#query-builder-test").type("DariaSkorobogatova/qa_guru_python_9_9")
    s("#query-builder-test").submit()
    s(by.link_text("DariaSkorobogatova/qa_guru_python_9_9")).click()
    s("#issues-tab").click()
    s(by.text("Issue for homework 9 with allure")).should(be.visible)
