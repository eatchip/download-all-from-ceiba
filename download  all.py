#本程式為一鍵下載臺大ceiba上的所有課件
#本程式由於需要一些套件等，需要下載selenium套件、pywin32等

#載入一些套件
import os
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pprint import pprint
from selenium.webdriver.common.action_chains import ActionChains
import win32api
import win32con

#定義好賬戶和密碼
username = ('')
password = ('')

#建立制定文件夾以便後期下載
rootpath = '/users/shy/ceiba'
ctpath = os.path.join(rootpath,'ctpath')

#用selenium在網頁上一步一步操作
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': ctpath}
options.add_experimental_option('prefs', prefs)
Browser = webdriver.Chrome(executable_path=os.path.join(rootpath, 'chromedriver'), chrome_options=options)
Browser.get('https://ceiba.ntu.edu.tw/')
handle = Browser.current_window_handle
Browser.find_element_by_xpath("//input[1]").click()
Browser.find_element_by_xpath("//form[@name='login2']/p[1]/input[1]").click()
Browser.find_element_by_xpath("//input[1]").send_keys(username)
Browser.find_element_by_name('pass').send_keys(password)
Browser.find_element_by_name('pass').send_keys(Keys.ENTER)
Browser.find_element_by_class_name('select').find_element_by_name('select_d').find_element_by_xpath("//option[text()='全部']").click()
ctlist = Browser.find_element_by_xpath("//div[@id = 'main']/table/tbody")
ctindex = []
ctname = []
NTU = []
new_NTU = []

#打开每一个界面，并点击进入‘课程内容’
for ct in ctlist.find_elements_by_tag_name("tr"):
      ctinfo = ct.find_elements_by_tag_name("td")
      if(len(ctinfo)!=0):
          ct.find_element_by_link_text(ctinfo[4].text.split('\n')[0][:-1]).click()#点击课程名称

          all_hand = Browser.window_handles
          time.sleep(1)
          Browser.switch_to_window(all_hand[-1])
          Browser.switch_to.frame('Main')
          Browser.switch_to.frame('leftFrame')
          Browser.find_element_by_id('syllabus').click()
          Browser.switch_to.frame('mainFrame')
          Browser.find_element_by_id('main')
          Browser.find_element_by_id('section')
          Browser.find_element_by_id('sect_cont')
          dllist = Browser.find_element_by_xpath("//div[@id = 'sect_cont']/table/tbody")
          for dl in dllist.find_elements_by_tag_name("tr"):
            dlinfo = dl.find_elements_by_tag_name("td")
            if(len(dlinfo)!=0):
                dls = dlinfo[3]
                wenben = dls.text.split()
                for wenzi in wenben:
                    url = dls.find_element_by_partial_link_text(wenzi)
                    ActionChains(Browser).context_click(url).perform()
                    time.sleep(2)
                    win32api.keybd_event(75,win32con.KEYEVENTF_KEYUP,0)
                    time.sleep(2)
                    os.system(r"C:\users\shy\test.exe")
                    time.sleep(2)
                    NTU.append(url)
                    new_NTU = list(set(NTU))
                    new_NTU.sort(key = NTU.index)
          pprint (new_NTU)
          print("哎哟不错哦")
          print(len(new_NTU))
          time.sleep(1)
          Browser.close()
          Browser.switch_to_window(all_hand[0])

print ("恭喜结束")


