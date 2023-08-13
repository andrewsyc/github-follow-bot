from selenium import webdriver
import time
import sys
import importlib

importlib.reload(sys)
sys.setdefaultencoding('utf-8')

# Firefox used
driver = webdriver.Firefox()
# base url
driver.get("http://github.com/login")

username = driver.find_element_by_id("login_field")
password = driver.find_element_by_id("password")

# password and username need to go into these values
username.send_keys("username for github")
time.sleep(1)
password.send_keys("password for github")
time.sleep(1)

login_form = driver.find_element_by_xpath("//input[@value='Sign in']")
time.sleep(1)
login_form.click()
time.sleep(1)

# These are some of the most popular users on github
prepend = ["jashkenas", "ruanyf", "substack", "kennethreitz", "jlord", "daimajia", "mdo", "schacon", "mattt",
           "sindresorhus", "defunkt", "douglascrockford", "mbostock", "jeresig",
           "mojombo", "addyosmani", "paulirish", "vczh", "romannurik", "tenderlove", "chriscoyier", "johnpapa",
           "josevalim",
           "charliesome", "CoderMJLee", "ry", "antirez", "muan", "isaacs", "angusshire",
           "hadley", "hakimel", "yyx990803", "fat", "fabpot", "ibireme", "tekkub",
           "BYVoid", "laruence", "onevcat", "tpope", "mrdoob", "LeaVerou", "chrisbanes", "wycats", "lifesinger",
           "cloudwu", "mitsuhiko", "michaelliao", "ryanb", "clowwindy", "JacksonTian", "yinwang0", "Trinea",
           "pjhyett", "dhh", "gaearon"]

for user in prepend:
    for t in range(1, 100):
        string = "https://github.com/{}/followers?page={}".format(user, t)
        driver.get(string)
        time.sleep(1)

        # make sure to pick the correct directory to save the files to
        # follow_button = driver.find_elements_by_xpath("//button[@type='submit']")
        follow_button = driver.find_elements_by_xpath("//button[@aria-label='Follow this person']")

        # Once page is loaded this clicks all buttons for follow
        try:
            for i in follow_button:
                i.submit()
        except:
            pass
        time.sleep(1)

driver.close()
