import sys
import os
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r'C:\Program Files (x86)\chromedriver.exe')

text = ''.join(sys.stdin.readlines())    

########Pancake Chef Diffcheck########

driver.get("https://www.diffchecker.com/")
pyperclip.copy(text)
driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div[2]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')

PCS=''

with open(r'C:\Users\mirror\Desktop\app\PCS.txt') as infile:
    for line in infile:
        PCS=PCS+line

pyperclip.copy(PCS)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_name("Find Difference").click()

additions = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/span").text
removals = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/span").text

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/form/input").send_keys('Pancake Diff')
driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div[2]/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[9]/div/div/div/div[2]/div/form/div/button").click()

print("Pancake \n" + additions + "\n" + removals + "\n" + pyperclip.paste() + "\n")

########Goose Chef Diffcheck########

driver.get("https://www.diffchecker.com/")
pyperclip.copy(text)
#driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div[2]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')

Goose=''

with open(r'C:\Users\mirror\Desktop\app\Goose.txt') as infile:
    for line in infile:
        Goose=Goose+line

pyperclip.copy(Goose)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_name("Find Difference").click()

additions = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/span").text
removals = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/span").text

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/input").send_keys('Goose Diff')
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/div[2]/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div/form/div/button").click()

print("Goose \n" + additions + "\n" + removals + "\n" + pyperclip.paste() + "\n")

########Viking Chef Diffcheck########

driver.get("https://www.diffchecker.com/")
pyperclip.copy(text)
#driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div[2]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')

Viking=''

with open(r'C:\Users\mirror\Desktop\app\Viking.txt') as infile:
    for line in infile:
        Viking=Viking+line

pyperclip.copy(Viking)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_name("Find Difference").click()

additions = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/span").text
removals = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/span").text

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/input").send_keys('Viking Diff')
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/div[2]/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div/form/div/button").click()

print("Viking \n" + additions + "\n" + removals + "\n" + pyperclip.paste() + "\n")

########Autofarm Chef Diffcheck########

driver.get("https://www.diffchecker.com/")
pyperclip.copy(text)
#driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div[2]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')

Autofarm=''

with open(r'C:\Users\mirror\Desktop\app\Autofarm.txt') as infile:
    for line in infile:
        Autofarm=Autofarm+line

pyperclip.copy(Autofarm)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_name("Find Difference").click()

additions = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/span").text
removals = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/span").text

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/input").send_keys('Autofarm Diff')
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/div[2]/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div/form/div/button").click()

print("Autofarm \n" + additions + "\n" + removals + "\n" + pyperclip.paste() + "\n")

########Fullsail Chef Diffcheck########

driver.get("https://www.diffchecker.com/")
pyperclip.copy(text)
#driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div[2]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')

Fullsail=''

with open(r'C:\Users\mirror\Desktop\app\Fullsail.txt') as infile:
    for line in infile:
        Fullsail=Fullsail+line

pyperclip.copy(Fullsail)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_name("Find Difference").click()

additions = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/span").text
removals = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/span").text

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/input").send_keys('Fullsail Diff')
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/div[2]/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div/form/div/button").click()

print("Fullsail \n" + additions + "\n" + removals + "\n" + pyperclip.paste() + "\n")

########Jigg Chef Diffcheck########

driver.get("https://www.diffchecker.com/")
pyperclip.copy(text)
#driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div[2]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')

Jigg=''

with open(r'C:\Users\mirror\Desktop\app\Jigg.txt') as infile:
    for line in infile:
        Jigg=Jigg+line

pyperclip.copy(Jigg)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_name("Find Difference").click()

additions = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/span").text
removals = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/span").text

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/input").send_keys('Jigg Diff')
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/div[2]/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div/form/div/button").click()

print("Jigg \n" + additions + "\n" + removals + "\n" + pyperclip.paste() + "\n")

########Slime Chef Diffcheck########

driver.get("https://www.diffchecker.com/")
pyperclip.copy(text)
#driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div[2]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')

Slime=''

with open(r'C:\Users\mirror\Desktop\app\Slime.txt') as infile:
    for line in infile:
        Slime=Slime+line

pyperclip.copy(Slime)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_name("Find Difference").click()

additions = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/span").text
removals = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/span").text

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/input").send_keys('Slime Diff')
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/div[2]/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div/form/div/button").click()

print("Slime \n" + additions + "\n" + removals + "\n" + pyperclip.paste() + "\n")

########Deflate Chef Diffcheck########

driver.get("https://www.diffchecker.com/")
pyperclip.copy(text)
#driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div[2]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')

Deflate=''

with open(r'C:\Users\mirror\Desktop\app\Deflate.txt') as infile:
    for line in infile:
        Deflate=Deflate+line

pyperclip.copy(Deflate)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_name("Find Difference").click()

additions = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/span").text
removals = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/span").text

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/input").send_keys('Deflate Diff')
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/div[2]/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div/form/div/button").click()

print("Deflate \n" + additions + "\n" + removals + "\n" + pyperclip.paste() + "\n")

########Blizzard Chef Diffcheck########

driver.get("https://www.diffchecker.com/")
pyperclip.copy(text)
#driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div[2]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')

Blizzard=''

with open(r'C:\Users\mirror\Desktop\app\Blizzard.txt') as infile:
    for line in infile:
        Blizzard=Blizzard+line

pyperclip.copy(Blizzard)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_name("Find Difference").click()

additions = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/span").text
removals = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/span").text

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/input").send_keys('Blizzard Diff')
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/div[2]/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div/form/div/button").click()

print("BLizzard \n" + additions + "\n" + removals + "\n" + pyperclip.paste() + "\n")

########Panther Chef Diffcheck########

driver.get("https://www.diffchecker.com/")
pyperclip.copy(text)
#driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div[2]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')

Panther=''

with open(r'C:\Users\mirror\Desktop\app\Blizzard.txt') as infile:
    for line in infile:
        Panther=Panther+line

pyperclip.copy(Panther)


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/div[2]/div").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_name("Find Difference").click()

additions = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/span").text
removals = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/span").text

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/input").send_keys('Panther Diff')
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/div[2]/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div/form/div/button").click()

print("Panther \n" + additions + "\n" + removals + "\n" + pyperclip.paste() + "\n")