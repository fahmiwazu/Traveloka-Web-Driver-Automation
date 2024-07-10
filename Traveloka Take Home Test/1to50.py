import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("D:\\Work\\webdriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://zzzscore.com/1to50/en/")

a=1
while(a!=51):
    driver.find_element(By.XPATH, "//div[normalize-space()='"+str(a)+"']//span[@class='box']").click()
    print("number "+str(a)+" are clicked")
    if(a%6==0):
        time.sleep(1)

    a=a+1

print("Quiz are completed")

time_record = driver.find_element(By.XPATH, "(//div[@id='time'])[1]")
record = time_record.text

print("Congratulation! your record are "+ record+ " seconds")
time.sleep(10)

driver.close()