
import allure,pytest

class Test001:
    @allure.step("这是一个测试方法")
    def test_001(self):
        print("test_001")
        allure.attach("文件","文件内容")
        assert True