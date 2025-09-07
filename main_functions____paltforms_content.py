import ast
import textwrap
from urllib.parse import unquote,quote
import requests
from bs4 import BeautifulSoup
import re
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import ast
from selenium.webdriver.common.by import By
import textwrap
from urllib.parse import unquote,quote
import requests
from bs4 import BeautifulSoup
import re
import time

from 已完成.接单平台汇集.important_parts import preparation,total_search_content
# from 未完成.接单平台汇集.important_parts import preparation



def five_eight_net_work_searching(search_content):
    print('58网运行中。。。。。')
    aaaa = quote(search_content)
    print(aaaa)
    url = 'https://pe.58.com/job/1/?key={}&cmcskey={}'.format(aaaa, aaaa)
    # url = 'https://pe.58.com/job/1/?key=2222222&cmcskey=2222222'
    print(url)
    five_eight = preparation()
    five_eight.minimize_window()
    five_eight.get(url)
    five_eight.implicitly_wait(60)
    work_details_position = '/html/body/div[3]/div[4]/div[1]/ul'
    work_details = five_eight.find_element(By.XPATH, work_details_position).get_attribute('outerHTML')
    soup = BeautifulSoup(work_details, 'lxml')
    # print(soup)
    each_works = soup.find_all('li')
    for i in each_works:
        # print(i)
        work_real_details_source = i.text
        work_real_details = textwrap.wrap(str(work_real_details_source))
        print(work_real_details) ####href待议.....
        ###########################################################
        total_search_content.append(work_real_details)
        ###########################################################
        print(')))'*89)
    time.sleep(10)
    five_eight.quit()

# five_eight_net_work_searching('语文教师')

######以上为58网######################

def cheng_xv_yuan_net():
    cheng_xv_yuan_net_url = 'https://www.proginn.com/sign/new_v2'
    return cheng_xv_yuan_net_url

# cheng_xv_yuan_net()

##########以上为程序员客栈#################
def top_tal_net():
    top_tal_net_url = 'https://www.toptal.com/talent/apply'
    return top_tal_net_url

##########以上为top_tal网站#################
def fiverr_net():
    fiverr_net_url = 'https://www.fiverr.com/search/gigs?query=drawer'
    return fiverr_net_url

##########以上为fiverr网站#################


def pu_er_chao_ping_net(pu_er_search_content):
    print('普洱网运行中。。。。。。。')
    # text_input = '会计'
    text_input_1 = unquote(pu_er_search_content)
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
            # print(real_work_href)
            # print(f'{work_description_and_corporation}\n{work_demands}\n{real_work_href}')
            work_description_and_corporation_1= str(work_description_and_corporation).replace('[','').replace(']','').strip()
            work_demands_1 = str(work_demands).replace('[','').replace(']','').strip()
            all_combine = f'{work_description_and_corporation_1}\t{work_demands_1}\t{real_work_href}'
            print(all_combine)
            ###########################################################
            total_search_content.append(all_combine)
            ###########################################################

            print('^&^^'*98)

# pu_er_chao_ping_net('教师')

##########以上为普洱人才网#################


def collage_student_help():
    collage_student_help_url = 'https://tuiguang.shixiseng.com/user/register_shixi2'
    return collage_student_help_url


##########以上为大学生就业指导网址#################

def hai_gui():
    hai_gui_net = 'https://www.togocareer.cn/'
    return hai_gui_net

##########以上为留学生回国求职网址#################

def guang_xi_zhao_ping_net(guang_xi_search_content):
    print('广西网运行中。。。。。')
    # aa = '英语教师'
    aaa = unquote(guang_xi_search_content)
    guang_xi_zhao_ping_url = f'https://s.gxrc.com/sJob?keyword={aaa}&schType=1&PosType=&industry='
    try:
        start = preparation()
        start.minimize_window()
        start.get(guang_xi_zhao_ping_url)
        start.implicitly_wait(60)
        text_input_position = '/html/body/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/input'
        start.find_element(By.XPATH, text_input_position).click()
        start.find_element(By.XPATH, text_input_position).clear()
        start.find_element(By.XPATH, text_input_position).send_keys(aaa)
        ensure_search_position = '/html/body/div/div/div[2]/div/div[1]/div/div[1]/div/a'
        time.sleep(1)
        start.find_element(By.XPATH, ensure_search_position).click()
        start.implicitly_wait(60)
        # start.get_screenshot_as_file('test.png')
        # print('done')
        column_list_position = '/html/body/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]'
        column_list_content = start.find_element(By.XPATH, column_list_position)
        print(column_list_content)
        work_columns = column_list_content.get_attribute('outerHTML')  # class_=search-position-list
        # print(work_columns)
        soup = BeautifulSoup(work_columns, 'html.parser')
        column_source = soup.find('div')
        # print(column_source)
        column = column_source.find_all('div', class_='position-item')
        for i in column:
            # print(i)
            # print('&0'* 80)
            work_description_source = i.find('div')
            # print(work_description_source)
            work_description_source_1 = work_description_source.text  ####工作介绍######
            work_description = textwrap.wrap(str(work_description_source_1))  ####工作介绍######
            # print(work_description)

            work_href = i.find('a', class_='position-item-left')['href']  #####工作链接#####
            # print(f'{work_description},{work_href}')

            work_type_source = i.find('div', class_='position-item-footer')
            # print(work_type_source)
            work_type_source_1 = work_type_source.text  ###工作类型####
            work_type = textwrap.wrap(str(work_type_source_1))
            all_combine = f'{work_description}\t{work_href}\t{work_type}'
            ###########################################################
            total_search_content.append(all_combine)
            ###########################################################
            print('**' * 89)
    finally:
        start.quit()

# guang_xi_zhao_ping_net()

##########以上为广西人才网站#################

def fu_jian_net(fu_jian_search_content):
    # test_url = 'https://www.hxrc.com/rcnew/SeniorSearchJobInFront.aspx?SearchKind=1&KeyWord=%E8%AF%AD%E6%96%87%E6%95%99%E5%B8%88&wp='
    # search_work = '机械设计'
    search_work_1 = quote(fu_jian_search_content)
    # print(search_work_1)
    fu_jian_url = f'https://www.hxrc.com/rcnew/SeniorSearchJobInFront.aspx?SearchKind=1&KeyWord={search_work_1}&wp='
    print(fu_jian_url)
    chrome = preparation()
    chrome.minimize_window()
    chrome.get(fu_jian_url)
    chrome.implicitly_wait(60)
    column_list_position = '/html/body/div[1]/div[4]/div[2]'
    column_list_source = chrome.find_element(By.XPATH, column_list_position)
    column_list_source_1 = column_list_source.get_attribute('outerHTML')
    # print(column_list_source_1)
    soup = BeautifulSoup(column_list_source_1, 'html.parser')
    work_combine = soup.find_all('div', class_='searchjobs2018related_jobslist')  # class_ = searchjobs2018related_right

    for j in work_combine:
        # print(j)
        total_work_description_and_href_source = j.find('div',class_='searchjobs2018related_jobslistleft')  # class_ =class=searchjobs2018related_jobslist clearfix
        print(total_work_description_and_href_source)

        total_work_description_and_href_source_1 = total_work_description_and_href_source.text
        total_work_description = textwrap.wrap(str(total_work_description_and_href_source_1))
        print(total_work_description)
        ###########################################################
        total_search_content.append(total_work_description)
        ###########################################################

        print('**' * 89)
        time.sleep(10)
        chrome.quit()

# fu_jian_net()

##########以上为福建人才网站#################


def hu_nan_net(hu_nan_search_content):
    # test_hu_nan_url = 'https://www.hnrcsc.com/#/positionB/position?position=%E4%BC%9A%E8%AE%A1'
    hu_nan_url = f'https://www.hnrcsc.com/#/positionB/position?position={unquote(hu_nan_search_content)}'
    la = preparation()
    la.minimize_window()
    la.get(hu_nan_url)
    la.implicitly_wait(60)
    column_combine_position = '/html/body/div[1]/div[1]/div/section/div[1]/div/div[5]/div[1]'
    column_list_source = la.find_element(By.XPATH, column_combine_position)   #class_= content-left
    # print(column_list_source.get_attribute('outerHTML'))
    column_list_source_1 = column_list_source.get_attribute('outerHTML')
    soup = BeautifulSoup(column_list_source_1, 'lxml')
    column_list = soup.find_all('div',class_='positionlist')

    # range_list = list(range(0,len(column_list)+1))
    # print(range_list)
    try:
        for j in column_list:
            # print(range_list)
            then = j.find('div', class_='positionitem')
            work_details_source = then.text
            work_details = textwrap.wrap(str(work_details_source))
            print(work_details)
            # work_href_source_position = f'/html/body/div[1]/div[1]/div/section/div[1]/div/div[5]/div[1]/div[1]/div[{i}]'
            # print(work_href_source_position)
            ###########################################################
            total_search_content.append(work_details)
            ###########################################################
            print('**' * 89)
    finally:
        time.sleep(10)
        la.quit()


# hu_nan_net()

##########以上为湖南人才网站#################

def jiang_si_net(jiang_su_search_content):
    # test_jiang_si_url = 'https://www.jxrcw.com/job-search?t=%E6%95%B0%E5%AD%A6%E6%95%99%E5%B8%88'
    jiang_si_url = f'https://www.jxrcw.com/job-search?t={unquote(jiang_su_search_content)}'

    jiang_si = preparation()
    jiang_si.get(jiang_si_url)
    jiang_si.implicitly_wait(60)
    work_column_list_position = '/html/body/div/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]'
    work_column_list_position_1 = jiang_si.find_element(By.XPATH, work_column_list_position)   #role_=tabpanel,id_=pane-2
    work_column_list_position_2 = work_column_list_position_1.get_attribute('outerHTML')
    # print(work_column_list_position_1.get_attribute('outerHTML'))
    soup = BeautifulSoup(work_column_list_position_2, 'lxml')
    # print(soup)

    work_column_list = soup.find_all('div',class_='t-job-list-item')
    try:
        for j in work_column_list:
            # print(j)
            work_description_source = j.text
            work_description = textwrap.wrap(str(work_description_source))

            href = j.find('a', class_='t-job-info')['href']
            all_combine = '{}{}'.format(href, work_description)
            print(all_combine)
            ###########################################################
            total_search_content.append(all_combine)
            ###########################################################
            print('@@' * 80)
    finally:
        time.sleep(10)
        jiang_si.quit()

# jiang_si_net()

##########以上为江西人才网站#################


def gui_zhou_net(gui_zhou_search_content):
    test_gui_zhou_url = 'http://www.gzrc.com.cn/'
    input_work = f'{gui_zhou_search_content}'
    guizhou = preparation()
    try:
        guizhou.minimize_window()
        guizhou.get(test_gui_zhou_url)
        guizhou.implicitly_wait(60)
        input_position = '/html/body/div[1]/div[1]/div[2]/div[1]/form/div/ul/li[2]/input'
        ensure_search_button_position = '/html/body/div[1]/div[1]/div[2]/div[1]/form/div/input'
        guizhou.find_element(By.XPATH, input_position).click()
        time.sleep(1)
        guizhou.find_element(By.XPATH, input_position).send_keys(input_work)
        guizhou.find_element(By.XPATH, ensure_search_button_position).click()
        guizhou.minimize_window()
        time.sleep(2)

        print(guizhou.window_handles)
        guizhou.implicitly_wait(60)
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
            ###########################################################
            total_search_content.append(work_description)
            ###########################################################

            print('**' * 89)
    finally:
        time.sleep(10)
        guizhou.quit()


# gui_zhou_net()


##########以上为贵州人才网站#################


def china_publish_net(china_publish_search_content):
    # test_china_publish_url = 'http://job.mohrss.gov.cn/cjobs/jobinfolist/listJobinfolist?acb332=&AREA=&AREA_name=&ACA111=&ACA111_name=&workType=&workTypeName=&textfield=%E5%8A%A9%E7%90%86'
    eg = f'{china_publish_search_content}'
    egg = quote(eg)
    china_publish_url = f'http://job.mohrss.gov.cn/cjobs/jobinfolist/listJobinfolist?acb332=&AREA=&AREA_name=&ACA111=&ACA111_name=&workType=&workTypeName=&textfield={egg}'
    # print(china_publish_url)
    china = preparation()
    try:
        china.minimize_window()
        china.get(china_publish_url)
        china.implicitly_wait(60)
        work_combine_position = '/html/body/div[1]/div[3]/div[4]/div[2]/div[3]'
        work_combine_position_1 = china.find_element(By.XPATH, work_combine_position).get_attribute(
            'outerHTML')  # class_=list_list
        soup = BeautifulSoup(work_combine_position_1, 'lxml')
        # print(soup)
        work_combine_source = soup.text
        work_combine = textwrap.wrap(str(work_combine_source))
        print(work_combine)  # href给网页链接自己找......
        ###########################################################
        total_search_content.append(work_combine)
        ###########################################################
    finally:
        time.sleep(10)
        china.quit()

# china_publish_net()

##########以上为中国公共招聘网#################

def he_bei_net(he_bei_search_content):   #post形式..
    test_ob = f'{he_bei_search_content}'
    he_bei_url = 'http://www.hbrc.com.cn/web/postsearch'
    he_bei = preparation()
    try:
        he_bei.minimize_window()
        he_bei.get(he_bei_url)
        he_bei.implicitly_wait(60)
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
        column_combine = soup.find_all('div', class_='org-layout')
        for j in column_combine:
            # print(j)
            work_description_source = j.text
            work_description = textwrap.wrap(str(work_description_source))
            print(work_description)  # href给网页链接自己找......
            ###########################################################
            total_search_content.append(work_description)
            ###########################################################
            print('**' * 80)
    finally:
        time.sleep(10)
        he_bei.quit()

# he_bei_net()


##########以上为河北人才网#################