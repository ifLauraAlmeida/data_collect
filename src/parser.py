from bs4 import BeautifulSoup
from scraping import get_content


def get_basic_infos(soup):
    div_page = soup.find("div", class_="td-page-content")
    paragrafos = div_page.find_all("p")

    if len(paragrafos) < 2:
        return {}

    ems = paragrafos[1].find_all("em")

    data = {}

    for i in ems:
        partes = i.text.split(":", 1)
        if len(partes) == 2:
            chave, valor = partes
            data[chave.strip()] = valor.strip()

    return data


def get_aparicoes(soup):
    lis = (soup.find("div", class_ ="td-page-content")
        .find("h4")
        .find_next()
        .find_all("li"))

    aparicoes = [i.text for i in lis]
    return aparicoes


def get_personagens_infos(url):
    
    resp = get_content(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, features="html.parser")
        data = get_basic_infos(soup)
        data["Aparicoes"] = get_aparicoes(soup)
        return data
        
    else: 
        print("Não foi possível obter os dados.")
        return {}