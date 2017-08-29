import requests as rqs, os
import urllib
from bs4 import BeautifulSoup as BS

def trim_str(str):
    return "".join(str.split())

def check(data, list):
    for n in range(0, len(list)):
        if data == list[n].text:
            return True
    return False

os.system("clear")

url = 'http://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx'
html = rqs.get(url)
soup = BS(html.text,'html.parser')

view_state = soup.find("input", attrs = {"name" : "__VIEWSTATE"})
view_state_generator = soup.find("input", attrs = {"name" : "__VIEWSTATEGENERATOR"})
event_validation = soup.find("input", attrs = {"name" : "__EVENTVALIDATION"})
submit_text = soup.find("input", attrs = {"name" : "SuperLotto638Control_history1$btnSubmit"})
lottery_type = soup.find(id = "SuperLotto638Control_history1_DropDownList1").find_all("option")
searching_year = soup.find(id = "SuperLotto638Control_history1_dropYear").find_all("option")
searching_month = soup.find(id = "SuperLotto638Control_history1_dropMonth").find_all("option")

print("＝＝＝＝＝威力彩歷史獎號查詢＝＝＝＝＝")
user_year = input("請輸入欲查詢年份(103年開始)：")
if(check(user_year, searching_year)):
    user_month = input("請輸入欲查詢月份：")
    if(check(user_month, searching_month)):
        post_data = {}
        post_data[view_state['name']] = view_state['value']
        post_data[view_state_generator['name']] = view_state_generator['value']
        post_data[event_validation['name']] = event_validation['value']
        post_data['SuperLotto638Control_history1$DropDownList1'] = '1'
        post_data['SuperLotto638Control_history1$chk'] = 'radYM'
        post_data['SuperLotto638Control_history1$dropYear'] = user_year
        post_data['SuperLotto638Control_history1$dropMonth'] = user_month
        post_data[submit_text['name']] = submit_text['value']

        request = urllib.request.Request(url)
        request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36")
        post_data = urllib.parse.urlencode(post_data)
        post_data = post_data.encode('utf-8')
        response = urllib.request.urlopen(request, data = post_data)
        soup_res = BS(response, 'html.parser')
        table_all = soup_res.find_all("table", attrs = {"class":["table_org td_hm", "table_gre td_hm"]})

        for table in table_all:
            tr_all = table.find_all("tr")
            td_basic_text = tr_all[0].find_all("td")
            td_basic_data = tr_all[1].find_all("td")
            print("--------------------------------------------------")

            for n in range(0, len(td_basic_text)):
                print("%s: %s" %(trim_str(td_basic_text[n].text), trim_str(td_basic_data[n].text)))

            td_num = tr_all[2].find("td")
            td_num_block = tr_all[3].find_all("td")
            print("%s: " %(trim_str(td_num.text)))
            print("\t\t    %s\t\t%s" %(trim_str(td_num_block[0].text), trim_str(td_num_block[1].text)))
            td_num_order = tr_all[4].find_all("td")
            print("  %s:" %(trim_str(td_num_order[0].text)), end="  ")
            for n in range(1, len(td_num_order)):
                if n == len(td_num_order) - 1:
                    print("\t  %s" %(trim_str(td_num_order[n].text)), end="  ")
                else:
                    print("%s" %(trim_str(td_num_order[n].text)), end="  ")
            td_num_sorted = tr_all[5].find_all("td")
            print("\n  %s:" %(trim_str(td_num_sorted[0].text)), end="  ")
            for n in range(1, len(td_num_sorted)):
                if n == len(td_num_sorted) - 1:
                    print("\t  %s" %(trim_str(td_num_sorted[n].text)), end="  ")
                else:
                    print("%s" %(trim_str(td_num_sorted[n].text)), end="  ")
            print("\n--------------------------------------------------")
