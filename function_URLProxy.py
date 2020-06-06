import requests
from urllib.request import Request,urlopen
from lxml import html
from bs4 import BeautifulSoup
from time import sleep, time
start_time = time()

service_key = "2817e8a658731921d4792b6bc3f1eae4"
google_site_key = '6LeGq1sUAAAAALKlIBMVtMk8wo-KtgdRObUG0ZCX&co=aHR0cHM6Ly9pY3V0aXQuY2E6NDQz&hl=en&v=v1537165899310&size=normal&cb=onpwtvgy4nmf' 
page_url         = "https://icutit.ca/nMFu"
proxy_list  = "https://free-proxy-list.net/"
# https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/
url = "http://2captcha.com/in.php?key=" + service_key + "&method=userrecaptcha&googlekey=" + google_site_key + "&pageurl=" + page_url 


req = Request(proxy_list, headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()

with urlopen(req) as html_txt:
    soup = BeautifulSoup(html_txt, 'lxml')

element = soup.select("#proxylisttable > tbody > tr")

for i in element:
    # 0 la ip
    # 1 el puerto
    # 6 si es https
    # if i.select("td")[6].text=="yes":
    #     url_available_proxy="https://{0}:{1}".format(i.select("td")[0].text,i.select("td")[1].text)
    # else:
    #     url_available_proxy="http://{0}:{1}".format(i.select("td")[0].text,i.select("td")[1].text)
    # print(url_available_proxy)    
    url_available_proxy="https://{0}:{1}".format(i.select("td")[0].text,i.select("td")[1].text)
    print("se va a usar el proxy {0}".format(url_available_proxy))
    proxies = {
        "http": url_available_proxy, 
        "https": url_available_proxy
    }
    try:
        resp = requests.get(url,proxies=proxies)
        if resp.text[0:2] != 'OK':
            print('Error. Captcha is not received')

        print ("response captcha "+ resp.text[3:])
        captcha_id = resp.text[3:]
        
        # fetch ready 'g-recaptcha-response' token for captcha_id  
        fetch_url = "http://2captcha.com/res.php?key="+ service_key +"&action=get&id=" + captcha_id
        for i in range(1, 20):	
            sleep(5) # wait 5 sec.
            resp = requests.get(fetch_url)
            if resp.text[0:2] == 'OK':
                break
                
        print('Time to solve: ', time() - start_time) 
        
        # final submitting of form (POST) with 'g-recaptcha-response' token
        submit_url = page_url
            # spoof user agent
        headers = {'user-agent': 'Mozilla/5.0 Chrome/52.0.2743.116 Safari/537.36'} 
            # POST parameters, might be more, depending on form content
        payload = {'submit': 'submit', 'g-recaptcha-response': resp.text[3:]  }
        resp = requests.post(submit_url, headers=headers, data=payload)


        # response = requests.get(url,proxies=proxies)
        # print(response)
    except:
        print("Error al consultar la url con el proxy {0}".format(url_available_proxy))

    sleep(10)