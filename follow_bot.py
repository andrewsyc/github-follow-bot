from selenium import webdriver
import time

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
    string = "https://github.com/{}?tab=followers".format(user)
    driver.get(string)
    while(True):
        time.sleep(1)
        follow_buttons_div = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/main[1]/div[2]/div[1]/div[2]/div[2]/div[1]")
        for btn in follow_buttons_div.find_elements_by_css_selector("*"):
            try:
                if "Follow" in btn.get_attribute("value"):
                    btn.click()
            except:
                pass
        try:
            driver.find_element_by_xpath("//a[normalize-space()='Next']").click()
        except:
            break
        
driver.close()
