import requests
from bs4 import BeautifulSoup 


def get_content(url):

    cookies = {
        '_ga_DJLCSW50SC': 'GS2.1.s1771463058$o2$g1$t1771463683$j9$l0$h0',
        '_ga': 'GA1.2.1570164588.1771454458',
        '_ga_D6NF5QC4QT': 'GS2.1.s1771463058$o2$g1$t1771463683$j7$l0$h0',
        '_gid': 'GA1.2.963263908.1771454459',
        '__gads': 'ID=4704668cc00585cb:T=1771454458:RT=1771463631:S=ALNI_MZrohr-_6Q4HEZ3N8kZpBlrWB2dqA',
        '__gpi': 'UID=00001043058545ad:T=1771454458:RT=1771463631:S=ALNI_MbASfaYIlMl-a387s2HRb5k-m_ibQ',
        '__eoi': 'ID=40b73f6f34e0a602:T=1771454458:RT=1771463631:S=AA-AfjYqselozbCsoZz068CvbiXg',
        'FCCDCF': '%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22a31cf2cb-fad3-403e-b764-d65c9731c330%5C%22%2C%5B1771454457%2C257000000%5D%5D%22%5D%5D%5D',
        'FCNEC': '%5B%5B%22AKsRol9QBdJ1286S7CIU4sxP_6fJp9BF0GNswPsxqRMLcAHr07TV99RgulKGljZx0r5pr0j8XHY8pgdGlWGvTMf7ohKI-9zS8wLuOlanVNtYeyxbAWzrIxvWDaEQulqoZiZPM7oxd2pk_SmdMFtE7v0H_FMIiBgJXQ%3D%3D%22%5D%5D',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.residentevildatabase.com/personagens/',
        'Alt-Used': 'www.residentevildatabase.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0, i',
    }

    resp = requests.get(url, cookies=cookies, headers=headers)
    return resp


def get_links():
    url = 'https://www.residentevildatabase.com/personagens'
    resp = get_content(url)
    soup_personagens = BeautifulSoup(resp.text)

    ancoras = (soup_personagens.find("div", class_ ="td-page-content")
        .find_all("a"))

    links = [i["href"] for i in ancoras]
    return links