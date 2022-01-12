from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import requests, datetime, subprocess, time

CHROMEDRIVER = '/usr/bin/chromedriver' #linux
#CHROMEDRIVER = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'  #windows

ACCESS_TOKEN = 'XXXXXXXXYYYYYYYYZZZZZZZZ'
LOG_FILE_PATH = './log/check_reservation.log'

def main():
    write_log("-----START check_reservation.py-----")
    chrome_service = service.Service(executable_path=CHROMEDRIVER)
    option = Options()
    option.add_argument('--headless')

    driver = webdriver.Chrome(service=chrome_service, options=option)   #for background process
    #driver = webdriver.Chrome(service=chrome_service)                  #for NOT background process

    write_log('OPEN hotpepper beauty')
    driver.get('https://beauty.hotpepper.jp/XXXXXXXXXXX/')
    url = driver.current_url
    driver.find_element(By.LINK_TEXT, '空席確認・予約する').click()

    try:
        driver.find_elements(By.CSS_SELECTOR, '.btn.btn1H50.btnWlines.w150.mHA.fs13')[6].click()
    except IndexError:
        time.sleep(3)
        driver.find_elements(By.CSS_SELECTOR, '.btn.btn1H50.btnWlines.w150.mHA.fs13')[6].click()


    write_log('TRY TO GET availabilities')
    while True:
            try:
                open_cell = driver.find_elements(By.CLASS_NAME, 'openCell ')
                if len(open_cell) == 0:
                    nextpage = driver.find_element(By.LINK_TEXT, '次の一週間')
                    driver.execute_script("arguments[0].click();", nextpage)
                else:
                    write_log("FOUND", len(open_cell), "open cells")
                    num = str(len(open_cell))
                    if True == is_good_send_line(num):
                        send_notice_LINE_with_URL(URL = url, NUM = num)
                    driver.quit()
                    write_log('-----FINISH check_reservation.py-----')
                    break
            except NoSuchElementException:
                driver.quit()
                write_log('NOT FOUND availvability')
                write_log('-----FINISH check_reservation.py-----')
                break

def send_notice_LINE_with_URL(URL, NUM):
    line_notify_token = ACCESS_TOKEN
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {
        'message': (None, '\n美容室XXXで' + NUM + '個の空きが確認できました\n' + URL),
    }
    write_log('SEND a LINE notifications')
    requests.post(line_notify_api, headers = headers, data = data)

def write_log(*MESSAGE):
    fp = open(LOG_FILE_PATH, 'a')
    now = datetime.datetime.now()
    datelist = [now.strftime("[%Y/%m/%d %H:%M:%S]"), str(MESSAGE), '\n']
    fp.writelines(datelist)
    fp.close()

def is_good_send_line(NUM):
    history = str(subprocess.check_output('tail -n 10 ./log/check_reservation.log | head -n 5 | grep FOUND', shell = True, encoding = 'utf-8'))
    search = str(NUM) + ', \'open cells\''
    
    if not(search in history):
        write_log('Will Send LINE notifications')
        return True
    else:
        write_log('NOT SENT LINE notifications')
        return False

if __name__ == '__main__':
    main()