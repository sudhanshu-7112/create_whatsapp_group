import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from simon.accounts.pages import LoginPage
from simon.pages import BasePage

n = int(input("Enter no of contacts to make group:"))
l = []
for i in range(n):
    s = input()
    l.append(s)

group = input("Enter name of Group: ")

driver = webdriver.Chrome()
driver.maximize_window()

login_page = LoginPage(driver)
login_page.load()
# login_page.remember_me = False
print("1")
time.sleep(15)
print("2")

base_page = BasePage(driver)
if base_page.is_pane_page_available():
    element = driver.find_elements(By.TAG_NAME, "div")
    for i in element[::-1]:
        if i.get_attribute("class") == "_3ndVb fbgy3m38 ft2m32mm oq31bsqd nu34rnf1":
            more_element = i
            break

    more_element.click()
    time.sleep(3)
    element = driver.find_elements(By.TAG_NAME, "div")
    for i in element:
        if i.get_attribute("class") == "iWqod _1MZM5 _2BNs3":
            new_group = i
            break

    new_group.click()

    time.sleep(2)
    element = driver.find_element(By.TAG_NAME, "input")
    for i in range(n):
        element.send_keys(l[i])
        time.sleep(2)
        add = driver.find_elements(By.CLASS_NAME, "_8nE1Y")
        add = add[i * 2]
        add.click()
        time.sleep(2)

    element = driver.find_elements(By.TAG_NAME, "div")

    for i in element:
        if (
            i.get_attribute("class")
            == "p357zi0d gndfcl4n ac2vgrno d6ll3xky db4qzak4 i5tg98hk f9ovudaz przvwfww gx1rr48f f8jlpxt4 hnx8ox4h k17s6i4e ofejerhi os0tgls2 g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb hftcxtij rtx6r8la e3b81npk oa9ii99z p1ii4mzz"
        ):
            forward = i
            break

    forward.click()

    element = driver.find_elements(By.TAG_NAME, "div")
    for i in element:
        if i.get_attribute("class") == "to2l77zo gfz4du6o ag5g9lrv fe5nidar kao4egtt":
            name = i
            break

    name.send_keys(group)
    time.sleep(3)

    element = driver.find_elements(By.TAG_NAME, "div")
    for i in element:
        if (
            i.get_attribute("class")
            == "p357zi0d gndfcl4n ac2vgrno d6ll3xky db4qzak4 i5tg98hk f9ovudaz przvwfww gx1rr48f f8jlpxt4 hnx8ox4h k17s6i4e ofejerhi os0tgls2 g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb hftcxtij rtx6r8la e3b81npk oa9ii99z p1ii4mzz"
        ):
            add = i
            break

    add.click()
    time.sleep(15)
