from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main():

##############Please Edit this section##############
    main_account = '**' #請輸入主要帳號(不要加@gmail......等等的後綴!)
    suffix = '@************' # 填入Email的後綴。例如:'@gmail.com'
    password = '************'  #請輸入這些帳號的密碼
    max_success = 10 # 設定這次先建立幾組帳號，避免一次建立太多打驗證碼會打到手軟 (可以依照個人身體狀況增加)
    account_N_begin = 1 # for MUMI
    account_N_end = 4   # for MUMI
####################################################


    # print('可產生:',len(main_account)-1+sum(list(range(1,len(main_account)-1))),'組帳號')

    opts = webdriver.FirefoxOptions()
    opts.set_preference("dom.popup_maximum", 200) #允許最高開啟200個Tab(Firefox預設是最多20個Tab)
    driver = webdriver.Firefox(options=opts)
    
    account_list = []

    #自動產生所有透過小數點位移產生的排列組合
    # for dot in range(1,len(main_account)):
    #     account = main_account[:dot]+'.'+main_account[dot:]
    #     account_list.append(account)
        
    # for dot1 in range(1,len(main_account)-1):
    #     for dot2 in range(len(main_account)-1,dot1,-1):
    #         account = main_account[:dot1]+'.'+main_account[dot1:dot2]+'.'+main_account[dot2:]
    #         account_list.append(account)

    #For MUMI
    for i in range(account_N_begin,account_N_end+1):
        account = main_account + str(i)
        account_list.append(account)

    print("所有帳號: ",account_list)

    success_counter = 0
    for index, item in enumerate(account_list):
        print(index,': ',item)
        
        
        driver.get('https://account.xiaomi.com/pass/register?callback=https%3A%2F%2Fbuy.mi.com%2Ftw%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252Ftw%252F%26sign%3DM2NhMTUwMTU5MGM2YzZiM2Q4YjMyNzZmOWMyZTFjMWNiYzYyMGEwOQ%2C%2C&sid=mi_xiaomitw&_locale=zh_TW')
                                    
                                    
        driver.find_element_by_name('email').send_keys(item+suffix)
        
        driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[1]/div/div[6]/input").click()
        
        try:
            wait = WebDriverWait(driver, 2) 
            element = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div/div[5]/div/dl/dd[1]/div/label/input')))  
        except:
            print(item,' 註冊失敗')
            continue
                                         
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/dl/dd[1]/div/label/input").send_keys(password)
        driver.find_element_by_xpath("//*[@id='main_container']/div[5]/div/dl/dd[2]/div[1]/label/input").send_keys(password)
        success_counter +=1

        #open new tab
        driver.execute_script("window.open();")
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])

        if success_counter==max_success: 
            break

    driver.close()
        


if __name__ == '__main__':
    main()