import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fetch_exchange_rate(date, currency_code):
    # 启动WebDriver
    driver = webdriver.Chrome()  # 需要确保Chrome WebDriver路径正确, 可根据需要修改
    driver.maximize_window()

    try:
        # 模拟访问网页
        driver.get("https://www.boc.cn/sourcedb/whpj/")

        # 选择日期
        date_input = driver.find_element_by_id("erectDate")
        date_input.clear()
        date_input.send_keys(date)

        # 选择货币
        currency_select = driver.find_element_by_name("pjname")
        currency_select.send_keys(currency_code)

        # 点击查询按钮
        search_button = driver.find_element_by_xpath("//input[@type='submit']")
        search_button.click()

        # 等待页面元素的出现, 以便页面加载完成
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "publish")))

        # 找到并打印结果
        exchange_rate = driver.find_element_by_xpath("//table[@class='publish']/tbody/tr[1]/td[5]").text
        print(exchange_rate)

        # 将结果写入本地文件result.txt
        result_file_path = "result.txt"
        # 本地文件存在就追加写, 方便多次运行并保留结果, 不存在就新建
        mode = "w" if not os.path.exists(result_file_path) else "a"
        with open(result_file_path, mode) as file:
            file.write(f"Exchange rate for {date} and currency {currency_code}: {exchange_rate}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # 关闭浏览器
        driver.quit()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 yourcode.py <date> <currency_code>")
    else:
        Date = sys.argv[1]
        CurrencyCode = sys.argv[2]
        fetch_exchange_rate(Date, CurrencyCode)
