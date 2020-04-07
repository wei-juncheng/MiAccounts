from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main():

##############Please Edit this section##############
    suffix = '@*****' # 填入Email的後綴。例如:'@gmail.com'
    password = '********'  #請輸入account_list.txt裡面帳號一致的密碼 (此程式適合大量相同密碼的帳號海，不適合個別帳號)
####################################################

    account_list = []

    with open('account_list_1.txt') as f: #開啟相同目錄底下的account_list.txt (請先建立並修改此檔案，裡面每一行都是一個帳號且不包含email後綴，請看範例檔案)
        load_account = f.read().splitlines()
    account_list = list(set(load_account)) #去除重複值
    print(account_list)

    opts = webdriver.FirefoxOptions()
    opts.add_argument("--incognito")
    options.add_argument('-headless')

    for index, item in enumerate(account_list):
        print(index,': ',item,suffix)
        driver = webdriver.Firefox(options=opts)
        
        driver.get('https://buy.mi.com/tw/site/login')
                                    
                                    
        driver.find_element_by_name('user').send_keys(item+suffix)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_id('login-button').click()
        try:
            error_message = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[1]/div[4]/div/div/div/div[4]"))) #出現錯誤訊息!!
            print("登入失敗~~")
            driver.close()
            continue    
        except:
            pass

        try:    
            element = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, "J_userName")))
        except:
            print('頁面載入失敗')
            driver.close()
            continue
        cookies_list = driver.get_cookies()
        
        cookies_string = ""
        for item in cookies_list:
            cookies_string += item['name']+"="+item['value']+"; "
        print(cookies_string)
        driver.close()


if __name__ == '__main__':
    main()