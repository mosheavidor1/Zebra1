
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import datetime

driver = wd.Chrome(executable_path="C:\Program Files\chromedriver.exe")


driver.get("https://www.google.com/")

driver.maximize_window()


driver.find_element_by_xpath ( "//input[@name='q']" ).send_keys( "Zebra Medical Vision" )
driver.find_element_by_xpath("//input[@name='q']").send_keys(Keys.ENTER)

driver.find_element_by_xpath("//*[contains(text(), 'Medical Imaging & AI')]").click()


driver.find_element_by_xpath("//*[contains(text(), 'Team')]").click()



images = driver.find_elements_by_tag_name('img')


for image in images:

  
 print(image.get_attribute('alt'))
 print(image.get_attribute('src'))




f = open("test123.txt", "w+")
f.write(datetime.datetime.now().ctime())

f.write('\n')

f.write(str(image.get_attribute('src')))

f.write('\n')

f.write(str(image.get_attribute('alt')))

f.write('\n')

f.close()




