# coding:GBK
import os
import time
import requests
import time, os
import pandas as pd
from hashlib import md5
from selenium import webdriver
from selenium.webdriver.support.select import Select
from pykeyboard import ReplyKeyboard

options = webdriver.ChromeOptions()

# -- 防止被检测，旧版本用法（1）：
# chrome在79版之前用这个
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
# -- 防止被检测，新版本用法（2）：
# chrome在79和79版之后用这个
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
driver.get('http://www.hmm21.com/cms/company/engn/index.jsp?from=singlemessage&isappinstalled=0')
time.sleep(6)
handle = driver.window_handles
driver.switch_to.window(handle[1])
time.sleep(2)
driver.close()
handle = driver.window_handles
driver.switch_to.window(handle[0])
s = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/form/fieldset/p/span[1]/select')
Select(s).select_by_index(1)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/form/fieldset/p/span[2]/input').send_keys('T210105180027')
time.sleep(6)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/form/fieldset/p/span[3]/a').click()
time.sleep(6)
os.system('pause')