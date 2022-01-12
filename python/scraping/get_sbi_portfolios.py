import datetime
import time
from decimal import ROUND_HALF_UP, Decimal

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import six
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from check_reservation import LOG_FILE_PATH

#CHROMEDRIVER = '/usr/bin/chromedriver' #linux
CHROMEDRIVER = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'  #windows

ACCESS_TOKEN = 'XXXXXXXXXXX'
LOG_FILE_PATH = './log/get_sbi_portfolios.log'

USER_INFO = {
    'user_id'   :   'XXX-YYYYYYYY',
    'password'  :   'XXXXXXXXXXXXXXXXXX',
}

def main():
    write_log('-----START CHECKING SBI-----')
    
    driver = __init_driver__(CHROMEDRIVER, 'bg')

    login_sbi(driver, USER_INFO)

    move_to_portfolio_page(driver)

    df_result = get_table(driver)

    file_name = datetime.datetime.now().strftime("%Y%m%d") + '_sbi.png'
    
    convert_graph_to_image(df_result, header_columns=0, col_width=2.0).figure.savefig(file_name)

    send_notice_LINE(FILENAME = file_name)

    write_log('-----FINISH CHECKING SBI-----')
    return 0

def __init_driver__(DRIVER_PATH, OPT):
    chrome_service = service.Service(executable_path = DRIVER_PATH)
    
    if OPT == 'bg':     # Background process
        write_log('Option is Background')
        option = Options()
        option.add_argument('--headless')
        driver = webdriver.Chrome(service=chrome_service, options=option)   #for background process
        return driver
    elif OPT == 'fg':   # Foreground process
        write_log('Option is Foreground')
        driver = webdriver.Chrome(service=chrome_service)                  #for NOT background process
        return driver
    else:
        write_log('#####ERROR : OPTION is invalid (__init_driver__)#####')
        exit(-1)

def login_sbi(DRIVER, USER_INFO):
    write_log('Log in SBI')
    DRIVER.get('https://site1.sbisec.co.jp/ETGate/')
    DRIVER.find_element(By.NAME, 'user_id').send_keys(USER_INFO['user_id'])
    DRIVER.find_element(By.NAME, 'user_password').send_keys(USER_INFO['password'])
    DRIVER.find_element(By.NAME, 'ACT_login').send_keys(Keys.ENTER)
    write_log('Successfully logged in SBI')

def move_to_portfolio_page(DRIVER):
    write_log('Move to portfolio page')
    try:
        DRIVER.find_element(By.LINK_TEXT, 'ポートフォリオ').click()
    except NoSuchElementException:
        DRIVER.find_element(By.XPATH, '//*[@id="link02M"]/ul/li[1]/a/img').click()    

def get_table(DRIVER):
    time.sleep(3)
    write_log('Get table data from portflio page')
    html = DRIVER.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    table_all = soup.find_all('table', bgcolor = '#9fbf99', cellpadding = '4', cellspacing = '1', width = '100%')

    df_stock_actuals_general = pd.read_html(str(table_all), header = 0)[0]
    df_stock_actuals_general = df_stock_actuals_general.rename(columns = {'銘柄（コード）': 'Brand/Fund'})

    df_investtrust_specific = pd.read_html(str(table_all), header = 0)[1]
    df_investtrust_specific = df_investtrust_specific.rename(columns = {'ファンド名': 'Brand/Fund'})

    df_investtrust_nisa_reserve = pd.read_html(str(table_all), header= 0 )[2]
    df_investtrust_nisa_reserve = df_investtrust_nisa_reserve.rename(columns = {'ファンド名': 'Brand/Fund'})

    df_stock_actuals_general = df_stock_actuals_general.loc[:, ['Brand/Fund', '損益', '損益（％）', '評価額']]
    df_investtrust_specific = df_investtrust_specific.loc[:, ['Brand/Fund', '損益', '損益（％）', '評価額']]
    df_investtrust_nisa_reserve = df_investtrust_nisa_reserve.loc[:, ['Brand/Fund', '損益', '損益（％）', '評価額']]
    df_result = pd.concat([df_stock_actuals_general, df_investtrust_specific, df_investtrust_nisa_reserve])
    df_result = df_result.reset_index(drop = True)
    df_result.loc[:, 'Brand/Fund'] = ['APPLE', 'NASDAQ100', 'NASDAQ100L', 'All Country', 'Europe', 'S&P500']

    df_result = df_result.rename(columns = {'損益': 'Loss and Gain', '損益（％）' : 'Ratio(%)', '評価額' : 'Values'})

    total_loss_and_gain = df_result['Loss and Gain'].sum()
    total_values = df_result['Values'].sum()
    total_ratio = ((total_loss_and_gain + total_values )/ total_values - 1) * 100

    total_loss_and_gain = round_num(total_loss_and_gain)
    total_values = round_num(total_values)
    total_ratio = round_num(total_ratio)

    df_result.loc[len(df_result)] = ['Total', total_loss_and_gain, total_ratio, total_values]
    
    write_log('Successfully got table data')
    DRIVER.quit()
    return df_result

def round_num(num):
    num = Decimal(num).quantize(Decimal('0.01'), rounding = ROUND_HALF_UP)
    return num

def send_notice_LINE(FILENAME):
    write_log('Send a LINE notifications')

    line_notify_token = ACCESS_TOKEN
    line_notify_api = 'https://notify-api.line.me/api/notify'
    
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    files = {'imageFile': open(FILENAME, "rb")}   #open binary file
    payload = {'message' : '\n本日のポートフォリオです。'}
    requests.post(line_notify_api, headers = headers, params = payload, files = files)
    write_log('Successfully sent a LINE notifications')

def convert_graph_to_image(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], Edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in  six.iteritems(mpl_table._cells):
        cell.set_edgecolor(Edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax

def write_log(MESSAGES):
    fp = open(LOG_FILE_PATH, 'a')
    now = datetime.datetime.now()
    MESSAGES = now.strftime("[%Y/%m/%d %H:%M:%S]") + MESSAGES + '\n'
    fp.write(MESSAGES)
    fp.close()

if __name__ == '__main__':
    main()
