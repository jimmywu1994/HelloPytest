import pytest

@pytest.fixture(scope="session")
def start():
    print("\n打开首页")
    return "yoyo"

if __name__ == "__main__":
    # pytest.main(["-s", "test_2.py"])
    pytest.main(['-s',  'baidu/test_2.py',  '--alluredir=result/xml'])