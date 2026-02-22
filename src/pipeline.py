from tqdm import tqdm
import pandas as pd
from scraping import get_links
from parser import get_personagens_infos


def run_pipeline():

    links = get_links()
    data = []

    for i in tqdm(links):
        d = get_personagens_infos(i)
        d["Link"] = i
        nome = i.strip("/").split("/")[-1].replace("-"," ").title()
        d["nome"] = nome
        
        data.append(d)
        
    df = pd.DataFrame(data)

    return df