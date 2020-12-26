import allure
import yaml

from appium import webdriver
import pytest
from src.file import File

app_driver = None

path =File.get_root_path("Pytest_Auto")
caps_path = path+'\\config\\caps.yml'

@pytest.fixture(scope='session', autouse=True)
def driver():
    global app_driver

    # if app_driver is None:
    #     cpas_file = open(caps_path, "r")
    #     # 先将yaml转换为dict格式
    #     capabilities = yaml.load(cpas_file, Loader=yaml.FullLoader)
    #     app_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    #     app_driver.implicitly_wait(10)

    app_driver ='123123'

    yield app_driver # 整个测试完毕

    # 进行销毁逻辑
    # app_driver.close()
    # app_driver.quit()






# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''
#     hook pytest失败
#     :param item:
#     :param call:
#     :return:
#     '''
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#     # we only look at actual failing test calls, not setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         with allure.step('添加失败截图...'):
#             allure.attach(driver.get_screenshot_as_file(), "失败截图", allure.attachment_type.PNG)





# @pytest.hookimpl
# def pytest_addoption(parser):
#     parser.addoption('--app', action='store', default="ios", help="Choose App: ios or android")
#     parser.addoption('--device', action='store', default="emulator", help="Choose Device: simulator / emulator / real "
#                                                                           "device")
#
#
# @pytest.fixture(scope="session")
# def app(request):
#     return request.config.getoption("--app")
