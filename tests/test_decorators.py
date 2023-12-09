import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").type(repo)
    s("#query-builder-test").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue")
def should_see_issue_with_text(text):
    s(by.text(text)).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "daskorobogatova")
@allure.feature("Issues в репозитории")
@allure.story("Пользователь может просмотреть issue в репо")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps(browser_configs):
    open_main_page()
    search_for_repository("DariaSkorobogatova/qa_guru_python_allure")
    go_to_repository("DariaSkorobogatova/qa_guru_python_allure")
    open_issue_tab()
    should_see_issue_with_text("Issue for homework 9 with allure")


