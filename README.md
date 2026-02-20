# data_collect

Pipeline de coleta de dados desenvolvido durante o curso Data Collect do Teo Me Why. Inclui processos de scraping, tratamento, validação e armazenamento estruturado de dados, simulando cenários reais de engenharia de dados.

## Configuração de ambiente 

Criar um interpretador de python, usarei o *.venv* (o Téo usa o anaconda), assim você aloja todas as bibliotecas de um mesmo projeto nesse interpretador, ele que RODARÁ o projeto nele mesmo, você isolar as dependências de um projeto para outro.

1 - Abra o terminal na pasta do projeto e digite
python -m venv .venv

2 - Ative-o digitando
.venv\Scripts\Activate

3 - Confirme visualizando o (.venv) no terminal e o caminho do seu projeto ao lado.

Requests será a biblioteca utilizada para requisitar dados de sites.
Importe ela com: 
pip install requests 
* no TERMINAL dentro do .venv 

Através do import requests, você pode puxar informações de um HTML, tendo o google como exemplo, você pode através do .status_code verificar o http status code, basicamente o que diz se a conexão com o site deu OK ou não, dependendo ele retornará um valor, dando 200, a conexão foi completa com sucesso.

Além disso, com o .text, você visualiza a string que corresponde a página do google.

Tentando pegar o perfil de Ada Wong no site do Resident Evil DATABASE (copiando a URL), ele retorna um erro, pois muitas vezes o site pede que seja um humano, não um script.
Para contornar isso abra as configurações de DESENVOLVEDOR (ctrl+shift+i), clicando em NETWORK, dando após um ctrl+r, você verifica que ele requisita o ada.wong/, clicando com o botão direito, você seleciona "copy" e depois "copy as curl(POSIX)", copiamos o que o nosso navegador envia de requisição para um endereço, e assim retornar os valores da Ada, agora com isso copiado, você pode "traduzir" pro python, buscando um curl to python no google e abrindo qualquer conversor, nele você recebe agora tudo pronto para que seu script FINJA ser um humano navegando normalmente.

Nele recebemos cookies e headers, que basicamente são informações que o navegador envia junto com a requisição para provar quem ele é e manter a sessão ativa.

Com isso, status_code 200, conseguimos conectar!

O text retorna então TODA A PÁGINA DA ADA, absolutamente tudo.


Clicando em ELEMENTS ou melhor, em INSPECTOR com o inspector ativado, depois clicando na setinha ao lado, você pode passar o mouse pela página e buscar no HTML, partes de onde o seu mouse passa.

Agora vamos utilizar BeautifulSoup, pip install beautifulsoup4
Para importar, from bs4 import BeautifulSoup.

A informação que queremos está dentro de div, onde a class é td-page-content

Agora buscaremos o segundo parágrafo, onde começa em <p> e termina com </p> 
dando print(div_page.find_all("p")) você consegue chegar nesse resultado de achar o segundo parágrafo, que é o que buscamos.

A partir desse parágrafo damos paragrafo.find_all["em"] para buscar todos os "em", e isso se torna uma LISTA.

O mesmo pode ser feito para outros personagens, apenas mudando o nome no link.

Colocando então os headers e cookies dentro de uma função, podemos buscar diferentes nomes de Resident Evil dentro do mesmo código.