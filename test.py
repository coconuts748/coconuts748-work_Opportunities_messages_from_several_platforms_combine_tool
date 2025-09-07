import ast
import textwrap
from urllib.parse import unquote,quote
import requests
from bs4 import BeautifulSoup
import re
import selenium
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import ast
import textwrap
from urllib.parse import unquote,quote
import requests
from bs4 import BeautifulSoup
import re
import time

from 未完成.接单平台汇集.important_parts import preparation, preparation_head_less

ba_jie_net_search_header = {
    'authority':'www.zbj.com',
    'method':'GET',
    'path':'/fw/?k=2222',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'zh-CN,zh;q=0.9',
    'cache-control':'no-cache',
    'cookie':'_uq=a137d6f870c645b28c320aad708a5a33; uniqid=d0111f0w4tm6ee; _suq=0566bdae-b663-4c03-b995-035eecd0bed1; unionJsonOcpc=eyJvdXRyZWZlcmVyIjoiaHR0cHM6Ly93d3cuYmFpZHUuY29tL2xpbms/dXJsPTFmWVRBTDVCVlZ6OVFpbjY4SHUiLCJwbWNvZGUiOiIifQ==; oldvid=; vid=ab74f64367f8730e4088bbe8edf15f2d; nsid=s%3AqOZFE0sW1MKoR16StEwXz5YZhlKZsaJo.gViJH4pRBA6StCTL32OYKDJuEfgTjtTE9mdcb%2B4M1DM; local_city_path=puer; local_city_name=%E6%99%AE%E6%B4%B1; local_city_id=6519; vidSended=1; Hm_lvt_a360b5a82a7c884376730fbdb8f73be2=1754402744,1754404816; HMACCOUNT=ED5B56ABDFDC827B; Hm_lpvt_a360b5a82a7c884376730fbdb8f73be2=1754411659; s_s_c=xhA3dh7QsA2lgP8ro4tGR8aBaPrwUyVZznOW1maM2kKq9v08n7NH5LxJme172N2NEwqQW2ujiTyHvk%2FVtDl7fQ%3D%3D',
    'pragma':'no-cache',
    'priority' : 'u=0, i',
    'referer' :  'https://www.zbj.com/',
    'sec-ch-ua' : '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile' : '?0',
    'sec-ch-ua-platform' : '"Windows"',
    'sec-fetch-dest' : 'document',
    'sec-fetch-mode' : 'navigate',
    'sec-fetch-site' : 'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests' : '1',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}
def ba_jie_net():
    test_url = 'https://www.zbj.com/fw/?k=2222'
    r = requests.get(test_url)
    name_list = []
    price_list = []

    if r.status_code == 200:
        try:
            # print(r.text)
            soup = BeautifulSoup(r.text, 'lxml')
            # print(soup)
            body = soup.find('body')
            mission_source = body.find_all('div')[0]  # id_=__layout
            print(mission_source)
            ########到这.........................

            # mission_source_1 = mission_source.find_all('div') # id_=
            # print(mission_source_1)
            # mission_source_2 = mission_source_1.find_all('div')[0]  # class_=app-page-layout app-search-layout
            # print(mission_source_2)
            # mission_source_3 = mission_source_2.find_all('div')[2]  # .....
            # print(mission_source_3)
            # mission_source_4 = mission_source_3.find_all('div')[0]  # class_= s50-search-list-page
            # print(mission_source_4)
            # mission_source_5 = mission_source_4.find_all('div')[3]  # class_ = search-content-wrap
            # print(mission_source_5)
            # mission_source_6 = mission_source_5.find_all('div')[0]  # class_ = search-content
            # print(mission_source_6)
            # mission_source_7 = mission_source_6.find_all('div')[1]  # class_ = search-result-list
            # print(mission_source_7)
            # mission_source_8 = mission_source_7.find_all('div')[0]  # class_ = search-result-list-left
            # print(mission_source_8)
            # mission_source_9 = mission_source_8.find_all('div')[1]  # class_= search-result-list-service
            # print(mission_source_9)
            # missions = mission_source_9.find_all('div')
            ####！！！！以上为每单位置！！！####
            ####！！！！以上为每单位置！！！####
            ####！！！！以上为每单位置！！！####
            # for i in missions:
            #     details_source = i.find_all('div')[0]
            #     details_source_1 = details_source.find_all('div')[
            #         1]  # data-href_ = https://www.zbj.com/fw/1934146.html?pdcode=17&pos=1&ym=1&pst=searchf-list-service-2021-1-1&version=1
            ####！！以上为每单细节所在位置#####
            ####！！以上为每单细节所在位置#####
            # price_source = details_source_1.find_all('div')[0]
            # price = price_source.find('span').text
            # price_list.append(price)
            #
            # name_source = details_source_1.find_all('div')[1]  # class_ = name-pic-box
            # name_source_1 = name_source.find_all('div')[0]  # .....
            # name = name_source_1.find('span').text
            # name_list.append(name)
            # for single_name in name_list:
            #     for single_price in price_list:
            #         print(f'{single_name} {single_price}')
            # print('done')
        except IndexError or TypeError:
            print('error')

# ba_jie_net()


def five_eight_net():
    test_url = 'https://zpbasedata.58.com/category/pclistjob/pc/data?city=pe&area='
    r = requests.get(test_url)
    if r.status_code == 200:
        # print(r.text)
        soup = BeautifulSoup(r.text, 'lxml')
        # with open('58_net_origin_message.txt','w',encoding='utf-8') as f:
        #     f.write(str(soup))
        # print('done')
# five_eight_net()


# def five_eight_net_sort_works_code():

    five_eight_net_sort_work_url = 'https://zpbasedata.58.com/category/pclistjob/pc/data?city=pe&area='
    r = requests.get(five_eight_net_sort_work_url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        list_mode = '^<html>.*?"subList":(.*])'
        content_dealing = re.findall(list_mode, str(soup),re.S)
        # print(content_dealing)
        for i in content_dealing:
            the_list_content = textwrap.wrap(str(i.strip()))
            the_list_content_1 = str(the_list_content).strip()
            # print(the_list_content_1)
        #     types_work_list = ast.literal_eval(the_list_content_1)
        #     print(type(types_work_list))
        #     # print(types_work_list)
        #     for j in types_work_list:
        #         print(j)
        #         print('%'*90)


# five_eight_net_sort_works_code()
def five_eight_net_work_searching():
    # aaa = '驾驶员'
    # aaaa = quote(aaa)
    # print(aaaa)
    # url = 'https://pe.58.com/job/1/?key={}&cmcskey={}'.format(aaaa, aaaa)
    url = 'https://pe.58.com/job/1/?key=2222222&cmcskey=2222222'
    print(url)
    r = requests.get(url)
    if r.status_code == 200:
        # print(r.text)
        soup = BeautifulSoup(r.text, 'lxml')
        body = soup.find('body')
        columns_source = body.find('div',class_='con')
        # print(columns_source)
        # for i in columns_source:
        #     print(i)
        #     print('_)'*30)
        columns_source_1 = columns_source   #class_=con
        print(columns_source_1)
        # columns_source_2 = columns_source_1.find('div',class_='main')  #class_=main clearfix
        # print(columns_source_2)
        # for i in columns_source_2:
        #     print(i)
        #     print('((__'*30)
        # columns_source_3 = columns_source_2.find('ul') #id_=list_con
        # print(columns_source_3)
        # columns = columns_source_3.find_all('li')
        # for single_li in columns:
        #     two_main_div = single_li.find_all('div')
        #     work_description_source = two_main_div[0].text
        #     work_description = textwrap.wrap(str(work_description_source))
        #     corporation_name_source = two_main_div[1].text
        #     corporation_name = textwrap.wrap(str(corporation_name_source))
        #     print('{}:{}'.format(corporation_name, work_description))
        #     print('@'*40)


# five_eight_net_work_searching()


def cheng_xv_yuan_net():
    cheng_xv_yuan_net_url = 'https://www.proginn.com/sign/new_v2'
    return cheng_xv_yuan_net_url


def top_tal_net():
    top_tal_net_url = 'https://www.toptal.com/talent/apply'
    return top_tal_net_url

def fiverr_net():
    fiverr_net_url = 'https://www.fiverr.com/search/gigs?query=drawer'
    return fiverr_net_url

def pu_er_chao_ping_net():
    text_input = '教师'
    text_input_1 = unquote(text_input)
    pu_er_chao_ping_net_url = f'http://puer.kuaimi.cn/jobList.html?km=ok&name={text_input_1}'
    r =requests.get(pu_er_chao_ping_net_url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        body = soup.find('body')
        column_source = body.find('div',class_='main_content')
        # print(column_source)
        column_source_1 = column_source.find('div',class_='zhiweiList_content clearfix w_1200')
        # print(column_source_1)
        column_source_2 = column_source.find('div',class_='job-list')
        # print(column_source_2)
        column_source_3 = column_source_2.find('ul')
        # print(column_source_3)
        columns = column_source_3.find_all('li')


        for single_li in columns:
            altogether_source = single_li.find('div')   #class_ = job-primary clearfix
            # print(altogether_source)
            # print('-'*40)
            work_description_and_corporation_and_demands_source = altogether_source.find('div',class_='primary-wrapper')
            work_description_and_corporation_source_1 = work_description_and_corporation_and_demands_source.find('div',class_='job-title').text   ####工作介绍######
            work_description_and_corporation = textwrap.wrap(str(work_description_and_corporation_source_1))  ####公司名字######
            # print(work_description_and_corporation)
            work_demands_source = work_description_and_corporation_and_demands_source.find('div',class_='job-limit').text  #class_ =job-limit clearfix
            work_demands = textwrap.wrap(str(work_demands_source)) ####工作要求######
            ######以上为职位相关字面信息#################
            ######以上为职位相关字面信息#################

            work_href_source = altogether_source.find('div',class_='info-company')
            # print(work_href_source)
            work_href_source_1 = work_href_source.find('div')
            # print(work_href_source_1)
            work_href_source_2 = work_href_source.find('a')
            work_href = work_href_source_2.get('href')  ###工作详细链接####
            # print(work_href)
            real_work_href = f'http://puer.kuaimi.cn/{work_href}'
            print(real_work_href)

# pu_er_chao_ping_net()


def collage_student_help():
    collage_student_help_url = 'https://tuiguang.shixiseng.com/user/register_shixi2'
    return collage_student_help_url


def guang_dong_zhao_ping_net():
    guang_dong_zhao_ping_url = 'https://www.gdrc.com/'
    guang_dong_zhao_ping_url_1 = 'https://www.gdrc.com/index.php?m=&c=jobs&a=jobs_list&key=&search_type=full'
    r = requests.get(guang_dong_zhao_ping_url_1)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup)    #未加载成功.......

# guang_dong_zhao_ping_net()


def guang_xi_zhao_ping_net():
    aa = '英语教师'
    aaa = unquote(aa)
    guang_xi_zhao_ping_url = f'https://s.gxrc.com/sJob?keyword={aaa}&schType=1&PosType=&industry='
    start= preparation()
    start.get(guang_xi_zhao_ping_url)
    start.implicitly_wait(120)
    text_input_position = '/html/body/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/input'
    start.find_element(By.XPATH, text_input_position).click()
    start.find_element(By.XPATH, text_input_position).clear()
    start.find_element(By.XPATH, text_input_position).send_keys(aaa)
    ensure_search_position = '/html/body/div/div/div[2]/div/div[1]/div/div[1]/div/a'
    time.sleep(1)
    start.find_element(By.XPATH, ensure_search_position).click()
    start.implicitly_wait(120)
    # start.get_screenshot_as_file('test.png')
    # print('done')
    column_list_position = '/html/body/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]'
    column_list_content = start.find_element(By.XPATH, column_list_position)
    print(column_list_content)
    work_columns = column_list_content.get_attribute('outerHTML')   #class_=search-position-list
    # print(work_columns)
    start.quit()
    soup = BeautifulSoup(work_columns, 'html.parser')
    column_source = soup.find('div')
    # print(column_source)
    column = column_source.find_all('div',class_ = 'position-item')
    for i in column:
        # print(i)
        # print('&0'* 80)
        work_description_source = i.find('div')
        # print(work_description_source)
        work_description_source_1 = work_description_source.text   ####工作介绍######
        work_description = textwrap.wrap(str(work_description_source_1))   ####工作介绍######
        # print(work_description)

        work_href = i.find('a',class_='position-item-left')['href']   #####工作链接#####
        # print(f'{work_description},{work_href}')

        work_type_source = i.find('div',class_='position-item-footer')
        # print(work_type_source)
        work_type_source_1 = work_type_source.text   ###工作类型####
        work_type = textwrap.wrap(str(work_type_source_1))
        print(f'{work_description}\n{work_href}\n{work_type}')
        print('**' *89)

# guang_xi_zhao_ping_net()

def fu_jian_net():
    test_url ='https://www.hxrc.com/rcnew/SeniorSearchJobInFront.aspx?SearchKind=1&KeyWord=%E8%AF%AD%E6%96%87%E6%95%99%E5%B8%88&wp='
    search_work = '机械设计'
    search_work_1 = quote(search_work)
    # print(search_work_1)
    fu_jian_url = f'https://www.hxrc.com/rcnew/SeniorSearchJobInFront.aspx?SearchKind=1&KeyWord={search_work_1}&wp='
    print(fu_jian_url)
    chrome = preparation()
    chrome.get(fu_jian_url)
    chrome.implicitly_wait(180)
    column_list_position = '/html/body/div[1]/div[4]/div[2]'
    column_list_source = chrome.find_element(By.XPATH, column_list_position)
    column_list_source_1 = column_list_source.get_attribute('outerHTML')
    # print(column_list_source_1)
    soup = BeautifulSoup(column_list_source_1, 'html.parser')
    work_combine = soup.find_all('div',class_='searchjobs2018related_jobslist')   #class_ = searchjobs2018related_right
    for j in work_combine:
        # print(j)
        total_work_description_and_href_source = j.find('div',class_='searchjobs2018related_jobslistleft')   #class_ =class=searchjobs2018related_jobslist clearfix
        print(total_work_description_and_href_source)

        total_work_description_and_href_source_1 = total_work_description_and_href_source.text
        total_work_description = textwrap.wrap(str(total_work_description_and_href_source_1))
        print(total_work_description)
        print('**' *89)

    time.sleep(1)
    # chrome.quit()
# fu_jian_net()




def hu_nan_net():
    test_hu_nan_url = 'https://www.hnrcsc.com/#/positionB/position?position=%E4%BC%9A%E8%AE%A1'
    ##
    la = preparation()
    la.get(test_hu_nan_url)
    la.implicitly_wait(120)
    column_combine_position = '/html/body/div[1]/div[1]/div/section/div[1]/div/div[5]/div[1]'
    column_list_source = la.find_element(By.XPATH, column_combine_position)   #class_= content-left
    # print(column_list_source.get_attribute('outerHTML'))
    column_list_source_1 = column_list_source.get_attribute('outerHTML')
    soup = BeautifulSoup(column_list_source_1, 'lxml')
    column_list = soup.find_all('div',class_='positionlist')

    # range_list = list(range(0,len(column_list)+1))
    # print(range_list)
    for j in column_list:
         # print(range_list)
         then = j.find('div',class_='positionitem')
         work_details_source = then.text
         work_details = textwrap.wrap(str(work_details_source))
         print(work_details)
         # work_href_source_position = f'/html/body/div[1]/div[1]/div/section/div[1]/div/div[5]/div[1]/div[1]/div[{i}]'
         # print(work_href_source_position)
         print('**' * 89)
    # time.sleep(10)
    # la.quit()

# hu_nan_net()


def jiang_si_net():
    test_jiang_si_url = 'https://www.jxrcw.com/job-search?t=%E6%95%B0%E5%AD%A6%E6%95%99%E5%B8%88'
    jiang_si_url = 'https://www.jxrcw.com/job-search?t={}'

    jiang_si = preparation()
    jiang_si.get(test_jiang_si_url)
    jiang_si.implicitly_wait(120)
    work_column_list_position = '/html/body/div/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]'
    work_column_list_position_1 = jiang_si.find_element(By.XPATH, work_column_list_position)   #role_=tabpanel,id_=pane-2
    work_column_list_position_2 = work_column_list_position_1.get_attribute('outerHTML')
    # print(work_column_list_position_1.get_attribute('outerHTML'))
    soup = BeautifulSoup(work_column_list_position_2, 'lxml')
    # print(soup)

    work_column_list = soup.find_all('div',class_='t-job-list-item')
    for j in work_column_list:
        # print(j)
        work_description_source = j.text
        work_description = textwrap.wrap(str(work_description_source))

        href = j.find('a',class_='t-job-info')['href']
        print('{}{}'.format(href, work_description))
        print('@@'*80)

# jiang_si_net()


def gui_zhou_net():   #post形式..
    test_gui_zhou_url = 'http://www.gzrc.com.cn/'
    input_work = '教师'
    guizhou = preparation()
    guizhou.get(test_gui_zhou_url)
    guizhou.minimize_window()
    guizhou.implicitly_wait(120)
    input_position ='/html/body/div[1]/div[1]/div[2]/div[1]/form/div/ul/li[2]/input'
    ensure_search_button_position = '/html/body/div[1]/div[1]/div[2]/div[1]/form/div/input'
    guizhou.find_element(By.XPATH, input_position).click()
    time.sleep(1)
    guizhou.find_element(By.XPATH, input_position).send_keys(input_work)
    guizhou.find_element(By.XPATH, ensure_search_button_position).click()
    guizhou.minimize_window()
    time.sleep(2)

    print(guizhou.window_handles)
    guizhou.implicitly_wait(120)
    guizhou.switch_to.window(guizhou.window_handles[1])
    time.sleep(1)

    column_list_position = '/html/body/div[3]/div[2]/div/table/tbody'
    column_list_source = guizhou.find_element(By.XPATH, column_list_position).get_attribute('outerHTML')
    soup = BeautifulSoup(column_list_source, 'lxml')
    # print(soup)

    column_list_combine = soup.find_all('tr')
    for j in column_list_combine:
        # print(j)
        work_description_source = j.text
        work_description = textwrap.wrap(str(work_description_source))
        print(work_description)
        print('**' * 89)

# gui_zhou_net()



def china_publish_net():
    test_china_publish_url = 'http://job.mohrss.gov.cn/cjobs/jobinfolist/listJobinfolist?acb332=&AREA=&AREA_name=&ACA111=&ACA111_name=&workType=&workTypeName=&textfield=%E5%8A%A9%E7%90%86'
    # eg = '教师'
    # egg = quote(eg)
    # china_publish_url = f'http://job.mohrss.gov.cn/cjobs/jobinfolist/listJobinfolist?acb332=&AREA=&AREA_name=&ACA111=&ACA111_name=&workType=&workTypeName=&textfield={egg}'
    # print(china_publish_url)
    china = preparation()
    china.minimize_window()
    china.get(test_china_publish_url)
    china.implicitly_wait(120)
    work_combine_position = '/html/body/div[1]/div[3]/div[4]/div[2]/div[3]'
    work_combine_position_1 = china.find_element(By.XPATH, work_combine_position).get_attribute('outerHTML')   #class_=list_list
    soup = BeautifulSoup(work_combine_position_1, 'lxml')
    # print(soup)
    work_combine_source = soup.text
    work_combine = textwrap.wrap(str(work_combine_source))
    print(work_combine)   #href给网页链接自己找......

# china_publish_net()

def he_bei_net():   #post形式..
    test_ob = '会计'
    he_bei_url = 'http://www.hbrc.com.cn/web/postsearch'
    he_bei = preparation()
    he_bei.minimize_window()
    he_bei.get(he_bei_url)
    he_bei.implicitly_wait(120)
    ensure_input_position = '/html/body/div/div[2]/div[1]/div[1]/form/div[4]/div/input'
    entry_position = '/html/body/div/div[2]/div[1]/div[1]/form/div[4]/div/input'
    ensure_searching_button_position = '/html/body/div/div[2]/div[1]/div[1]/form/div[5]'
    work_column_combine_position = '/html/body/div/div[2]/div[3]/div/div[1]'
    he_bei.find_element(By.XPATH, ensure_input_position).click()
    time.sleep(1)
    he_bei.find_element(By.XPATH, entry_position).send_keys(test_ob)
    time.sleep(2)
    he_bei.find_element(By.XPATH, ensure_searching_button_position).click()
    work_column_combine = he_bei.find_element(By.XPATH, work_column_combine_position).get_attribute('outerHTML')
    soup = BeautifulSoup(work_column_combine, 'lxml')
    # print(soup)
    column_combine = soup.find_all('div',class_='org-layout')
    for j in column_combine:
        # print(j)
        work_description_source = j.text
        work_description = textwrap.wrap(str(work_description_source))
        print(work_description)   #href给网页链接自己找......
        print('**' * 80)

# he_bei_net()