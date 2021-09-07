import time

import allure
import pytest
from time import sleep
from selenium import webdriver
import os

@allure.feature('百度搜索功能')
@allure.story("关键字搜索")
@pytest.mark.parametrize("key", ["unittest", "pytest", "allure"])
def test_baidu_search(key):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(r"http://www.baidu.com")
    with allure.step('step one：在搜索栏输入关键字{}'.format(key)):
        driver.find_element_by_id("kw").send_keys(key)
        sleep(2)
        driver.find_element_by_id("su").click()
        sleep(2)
        # print(driver.title)
        assert key in driver.title
    with allure.step('step two：截图保存'):
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        driver.save_screenshot(os.getcwd() + os.sep + "result/{}.png".format(now))
        sleep(1)
        allure.attach.file(os.getcwd() + os.sep + "result/{}.png".format(now), "附件", allure.attachment_type.PNG)
        sleep(1)
    driver.quit()

if __name__ == "__main__":
    # pytest.main(["-s", "test_2.py"])
    pytest.main(['-s', '-v', 'test_2.py',  '--alluredir=result'])