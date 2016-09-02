from selenium import webdriver
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')




#Firefox used
driver = webdriver.Firefox()
# base url
driver.get("http://github.com/login")

username = driver.find_element_by_id("login_field")
password = driver.find_element_by_id("password")

# password and username need to go into these values
username.send_keys("username")
time.sleep(1)
password.send_keys("password")
time.sleep(1)


login_form = driver.find_element_by_xpath("//input[@value='Sign in']")
time.sleep(1)
login_form.click()
time.sleep(1)

prepend = ["your_username"]


for user in prepend:
    for i in range(0, 200):
        for t in range(1, 100):
            string = "https://github.com/{}/following?page={}".format(user, t)
            driver.get(string)
            time.sleep(1)

            follow_button = driver.find_elements_by_xpath("//button[@aria-label='Unfollow this person']")

            # time.sleep(1)
            # print len(follow_button)
            try:
                for i in follow_button:
                    i.submit()
            except:
                pass
            time.sleep(1)



driver.close()

time.sleep(3)

time.sleep(3)

driver.close()