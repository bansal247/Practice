from selenium import webdriver
from selenium.webdriver.common.by import By
from google_drive_downloader import GoogleDriveDownloader as gdd
import os
import time
import shutil

driver = webdriver.Chrome()
driver.maximize_window()

user_id = "shashwatbansal247@gmail.com"
password = "Shashu@247"
time_to_wait = 2

driver.get("https://ineuron.ai/")
time.sleep(time_to_wait)

driver.find_element(by=By.LINK_TEXT,value = "Sign in").click()
time.sleep(time_to_wait)

def rem_frame():
    driver.switch_to.frame(5)
    driver.find_element(By.XPATH,'html/body/div/div/div/div/div/i').click()
    driver.switch_to.default_content()


def find_by_tag(tag,to_find_name=None,to_fill_data=None,show=False):
    k = driver.find_elements(by=By.TAG_NAME,value = tag)
    if type(to_find_name) == list:
        j = 0
        for i in k:
            if j<len(to_find_name) and i.accessible_name == to_find_name[j]:
                while True:
                    try:
                        i.click()
                        if to_fill_data:
                            i.send_keys(to_fill_data[j])
                        j = j + 1
                    except:
                        rem_frame()
                    else:
                        break
    else:
        for i in k:
            if show:
                print(i.accessible_name)
                continue
            if i.accessible_name == to_find_name:
                while True:
                    try:
                        i.click()
                        if to_fill_data:
                            i.send_keys(to_fill_data)
                    except:
                        rem_frame()
                    else:
                        break
                
            elif i.text == to_find_name:
                while True:
                    try:
                        i.click()
                        if to_fill_data:
                            i.send_keys(to_fill_data)
                    except:
                        rem_frame()
                    else:
                        break
                
        
find_by_tag('input',["Email Address","Enter Password"],[user_id,password])


find_by_tag('button','Sign In')
time.sleep(time_to_wait)

driver.get("https://learn.ineuron.ai/")
time.sleep(time_to_wait)

driver.find_element(By.CLASS_NAME,"Home_course-title__3tSE-").click()
time.sleep(time_to_wait)

find_by_tag('li','Assignments')
time.sleep(time_to_wait)

dict_to_use = {}
urls = {}

def download(urls):

    time.sleep(time_to_wait)
    name = driver.find_element(By.CLASS_NAME,"UploadAssignment_info__V5TWV").text
    j = driver.find_element(By.CLASS_NAME,"UploadAssignment_assignment-file__1bReg")
    k = j.find_element(By.TAG_NAME,'a')
    k.click()

    driver.switch_to.window(driver.window_handles[1])

    url = driver.current_url
    urls[name] = url
    #url = url[url.find('/d/')+3:url.find('/view')]
    #gdd.download_file_from_google_drive(file_id=url,
    #                                    dest_path='./{}.docx'.format(name),
    #                                   )
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    
    driver.find_element(By.CLASS_NAME,"fas.fa-times").click()


dir_list = []
for k in driver.find_elements(By.CLASS_NAME,'Assignments_title__xGAqZ'):
    dir_list.append(k.text)


assignments = driver.find_elements(By.CLASS_NAME,'Assignments_classes__2tC8z.Global_grid__2KDqG')
length = []
for assignment in assignments:
    length.append(len(assignment.find_elements(By.CLASS_NAME,'Assignments_class-title__PwgJi')))


def start():

    try:
        os.mkdir('ineuron')
        os.chdir(os.getcwd()+'\\ineuron')
        T_length = len(driver.find_elements(By.CLASS_NAME,'Assignments_class-card__1YQQg'))
        for k in dir_list:
            os.mkdir(k)
            curr_dir = os.getcwd()
            os.chdir(os.getcwd()+'\\'+k)
            urls = {}
            for i in range(T_length):
                while True:
                    try:
                        driver.find_elements(By.CLASS_NAME,'Assignments_class-card__1YQQg')[i].click()
                        download(urls)
                    except:
                        pass
                    else:
                        break
                    
            os.chdir(curr_dir)
            dict_to_use[k] = urls
            
            
    except Exception as e:
        print(e)
        os.chdir("C:\\Users\\Shashwat\\Desktop\\Ineuron\\Practice")
        location = os.getcwd()
        direc = "ineuron"
        path = os.path.join(location, direc)
        shutil.rmtree(path)
        time.sleep(time_to_wait)
        
start()
