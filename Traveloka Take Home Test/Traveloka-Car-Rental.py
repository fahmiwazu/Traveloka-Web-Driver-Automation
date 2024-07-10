import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("D:\\Work\\webdriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
# Open URL
driver.get("https://www.traveloka.com")
# Select Cars Product
driver.find_element(By.XPATH, "//div[normalize-space()='Car Rental']").click()
# Select tab Without Driver
driver.find_element(By.XPATH, "//div[@class='css-901oao r-t1w4ow r-ubezar r-majxgm r-135wba7 r-fdjqy7'][normalize-space()='Without Driver']").click()
# Select Pick-up Location (e.g.: Jakarta)
driver.find_element(By.XPATH, "//input[@placeholder='Enter city or region']").send_keys("Jakarta")
driver.find_element(By.XPATH, "//div[@aria-label='Jakarta']").click()
# Select Pick-up Date & Time (e.g.: today+2d 09:00)
driver.find_element(By.XPATH, "//input[@value='11 July 2024']").click()
driver.find_element(By.XPATH, "//body[1]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[10]/div[1]/div[1]/div[2]").click()
driver.find_element(By.XPATH, "//input[@data-testid='rental-search-form-time-input-start']").click()
driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-391gc0 r-1loqt21 r-1777fci r-tuq35u r-1otgn73 r-1i6wzkk r-lrvibr']//div[@class='css-901oao r-t1w4ow r-1b43r93 r-majxgm r-rjixqe r-q4m81j'][normalize-space()='9']").click()
driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-391gc0 r-1loqt21 r-1777fci r-tuq35u r-1otgn73 r-1i6wzkk r-lrvibr']//div[@class='css-901oao r-t1w4ow r-1b43r93 r-majxgm r-rjixqe r-q4m81j'][normalize-space()='0']").click()
driver.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-173mn98 r-kdyh1x r-1loqt21 r-1fz3rvf r-10paoce r-5njf8e r-1otgn73 r-lrvibr']").click()
# Select Drop-off Date & Time (e.g.: today+5d 11:00)
driver.find_element(By.XPATH, "//input[@value='13 July 2024']").click()
driver.find_element(By.XPATH, "//body[1]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[4]/div[5]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[10]/div[1]/div[1]/div[2]").click()
driver.find_element(By.XPATH, "//input[@data-testid='rental-search-form-time-input-end']").click()
driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-1loqt21 r-1777fci r-tuq35u r-1otgn73 r-1i6wzkk r-lrvibr']//div[@class='css-901oao r-t1w4ow r-1b43r93 r-majxgm r-rjixqe r-q4m81j'][normalize-space()='11']").click()
driver.find_element(By.XPATH, "//body[1]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[4]/div[7]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
# Click button Search Car
driver.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-173mn98 r-kdyh1x r-1loqt21 r-1fz3rvf r-10paoce r-5njf8e r-1otgn73 r-lrvibr']").click()
# Select Car
driver.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-kdyh1x r-1loqt21 r-10paoce r-1e081e0 r-5njf8e r-1otgn73 r-lrvibr']").click()
time.sleep(5)
# Select Car Provider
driver.find_element(By.XPATH, "(//div[@role='button'])[9]").click()
time.sleep(5)
# Click button Continue in Product Detail
driver.find_element(By.XPATH, "(//div[@role='button'])[5]").click()
time.sleep(5)
# Select Pick-up Location in “Rental Office”
driver.find_element(By.XPATH, "(//div[@role='radio'])[3]").click()
driver.find_element(By.XPATH, "(//div[@class='css-901oao css-bfa6kz r-13awgt0 r-t1w4ow r-ubezar r-majxgm r-135wba7 r-1m04atk r-fdjqy7'])[1]").click()
driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1awozwy r-1472mwg r-1777fci r-lrsllp'])[1]").click()
time.sleep(5)
# Select Drop-off Location in “Other Location”
driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1awozwy r-14lw9ot r-1l31rp8 r-16uyjmq r-rs99b7 r-18yzcnr r-1777fci r-yc9v9c'])[13]").click()
driver.find_element(By.XPATH, "(//input[@placeholder='Search location or address'])[2]").click()
driver.find_element(By.XPATH, "(//h3[@role='heading'][normalize-space()='Soekarno Hatta International Airport (CGK)'])[3]").click()
time.sleep(5)
# Input Pick-up/Drop-off notes is optional
driver.find_element(By.XPATH, "//textarea[@placeholder='Additional notes (optional)']").send_keys("Saudi Airlines 212")
# Click button Book Now
driver.find_element(By.XPATH, "(//div[@class='css-18t94o4 css-1dbjc4n r-kdyh1x r-1loqt21 r-10paoce r-5wp0in r-5njf8e r-1otgn73 r-lrvibr'])[1]").click()
time.sleep(10)
# Fill Contact Details
driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Fahmi Wahyu Wiradika")
driver.find_element(By.XPATH, "(//input[@aria-label='Phone Number'])[1]").send_keys("85281791212")
driver.find_element(By.XPATH, "(//input[@aria-labelledby='emailAddress'])[1]").send_keys("fahmi.wiradika96@gmail.com")
# Fill Driver Details
driver.find_element(By.XPATH, "(//select[@class='r-30o5oe r-1niwhzg r-1yadl64 r-1p0dtai r-t1w4ow r-ubezar r-majxgm r-1pi2tsx r-1r74h94 r-135wba7 r-crgep1 r-orgf3d r-1ny4l3l r-10paoce r-u8s1d r-3mc0re r-ipm5af r-34rx7k r-417010'])[1]").is_selected("Mr.")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Fahmi Wahyu Wiradika")
driver.find_element(By.XPATH, "(//input[@aria-label='Phone Number'])[2]").send_keys("85281791212")
# Click Continue
driver.find_element(By.XPATH,"(//div[@class='css-18t94o4 css-1dbjc4n r-kdyh1x r-1loqt21 r-10paoce r-1e081e0 r-5njf8e r-1otgn73 r-lrvibr'])[1]").click()
time.sleep(10)
# Add a special request is optional
driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-13awgt0 r-18u37iz'])[1]").click()
# Check all rental requirements
driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1awozwy r-k200y r-1loqt21 r-18u37iz r-t60dpp r-1otgn73'])[2]").click()
driver.find_element(By.XPATH, "(//div[@role='button'])[8]").click()
# Click Continue
driver.find_element(By.XPATH, "(//div[@class='css-18t94o4 css-1dbjc4n r-kdyh1x r-1loqt21 r-10paoce r-1e081e0 r-5njf8e r-1otgn73 r-lrvibr'])[1]").click()

driver.close()