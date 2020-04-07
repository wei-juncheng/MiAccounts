from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def main():

##############Please Edit This Section##############
    main_account = '**' #請輸入主要帳號(不要加@gmail......等等的後綴!)
    suffix = '@************' # 填入Email的後綴。例如:'@gmail.com'
    password = '***********'  #請輸入account_list.txt裡面帳號一致的密碼 (此程式適合大量相同密碼的帳號海，不適合個別帳號)
    account_N = 7 # for MUMI
####################################################

    account_list = []

    # with open('account_list.txt') as f: #開啟相同目錄底下的account_list.txt (請先建立並修改此檔案，裡面每一行都是一個帳號且不包含email後綴，請看範例檔案)
    #     load_account = f.read().splitlines()
    # account_list = list(set(load_account)) #去除重複值

    # print(account_list)

    for i in range(1,account_N):
        account = main_account + str(i)
        account_list.append(account)

    print("所有帳號: ",account_list)

    

    opts = webdriver.FirefoxOptions()
    opts.add_argument("--incognito")
    # opts.add_argument('-headless') ## 加入這個參數可以不顯示瀏覽器視窗，預設先不加

    for index, item in enumerate(account_list):
        print(index,': ',item,suffix)
        driver = webdriver.Firefox(options=opts)
        
        driver.get('https://buy.mi.com/tw/user/points-center')
                                    
        try:
            login = driver.find_element_by_id('login-main') #登入頁面載入完成  
                                
            driver.find_element_by_name('user').send_keys(item+suffix)
            driver.find_element_by_name('password').send_keys(password)
            driver.find_element_by_id('login-button').click()

            time.sleep(0.5)
            error_message_elements = driver.find_elements_by_class_name('err_tip') #取得錯誤訊息element
            
            if error_message_elements[0].text:  ##有錯誤訊息
                print("錯誤: ",error_message_elements[0].text)
                # driver.close() 
                continue
        except:
            print('登入失敗')
            continue

        try:
            driver.get("https://buy.mi.com/tw/user/points-center")    
            element = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, "getcoin")))
        except:
            print('頁面載入失敗')
            # driver.close()
            continue
        cookies_list = driver.get_cookies()
        
        cookies_string = ""
        for item in cookies_list:
            cookies_string += item['name']+"="+item['value']+"; "
        print(cookies_string)
        driver.close()


if __name__ == '__main__':
    main()