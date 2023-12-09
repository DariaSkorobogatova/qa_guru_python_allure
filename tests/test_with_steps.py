import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps(browser_configs):
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").type("DariaSkorobogatova/qa_guru_python_9_9")
        s("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("DariaSkorobogatova/qa_guru_python_9_9")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue for homework 9 with allure"):
        s(by.text("Issue for homework 9 with allure")).should(be.visible)

