<h1 align="center">🎮 Data Collect: Resident Evil Database</h1>

Este projeto foi desenvolvido durante o curso **Data Collect** do canal **Teo Me Why**.  
O objetivo é construir um pipeline completo de Engenharia de Dados, desde a coleta via web scraping até o armazenamento estruturado em múltiplos formatos.

> https://www.youtube.com/watch?v=K-bIZt_hSBo&t=2611s

---
<h1 align="center">⚙️ Configuração do Ambiente</h1>

Para garantir reprodutibilidade e isolamento de dependências, utilizamos **venv**, ferramenta nativa do Python para criação de ambientes virtuais.

- ### 1️⃣ Criação do ambiente

```bash
python -m venv .venv
```
- ### 2️⃣ Ativação

#### Windows
```bash
.venv\Scripts\activate
```

#### Linux/Mac
```bash
source .venv/bin/activate
```


- #### 3️⃣ Instalação das dependências
```bash
pip install requests beautifulsoup4 pandas tqdm pyarrow fastparquet
```
---
<h1 align="center">🕷️ Fundamentos da Coleta de Dados</h1>

### 🌐 Requisições HTTP e Autenticação

Utilizamos a biblioteca requests para comunicação via protocolo HTTP.
O atributo status_code verifica se a requisição foi bem-sucedida (200). Para contornar bloqueios do site, simulamos uma requisição humana:

`Abrimos o DevTools (F12) → aba Network`

`Copiamos como cURL (POSIX)`

`Convertendo para Python com headers e cookies (ex: User-Agent)`

`Isso permite simular uma sessão real de navegação.`

<h1 align="center">🔎 Parsing com BeautifulSoup</h1>


Após obter o HTML via .text, utilizamos BeautifulSoup para navegar na árvore DOM:

Localizamos a div principal `(td-page-content)`.

**Extraímos:**

- Parágrafos
- Tags < em > com chaves/valores das características
- Iteramos sobre todos os links da página principal para automatizar a coleta

<h3 align="center">💾 Armazenamento e Formatos de Arquivo</h3>

Os dados são estruturados em um DataFrame do Pandas e exportados para diferentes formatos.

| Formato  | Tipo                 | Características                                                         |
|----------|----------------------|-------------------------------------------------------------------------|
| CSV      | Texto (Plano)        | Legível por humanos, não preserva tipos de dados e ocupa mais espaço  |
| Parquet  | Binário (Colunar)    | Compactado, preserva tipos e é otimizado para Big Data                |
| Pickle   | Binário (Serializado)| Salva o estado exato do objeto Python                                 |

⚠️ Para Engenharia de Dados, **Parquet é preferível** ao CSV devido à **performance e preservação de metadados**, funcionará melhor como um "checkpoint".

---
<h1 align="center">🧩 Estrutura do Código</h1>

O script principal é modularizado em funções:

- **get_content(url)** → `Realiza requisição HTTP com headers/cookies`

- **get_basic_infos(soup)** → `Extrai descrições textuais`

- **get_aparicoes(soup)** → `Mapeia jogos/mídias onde o personagem aparece`

- **get_links()** → `Coleta URLs de todos os personagens`

---

<h1 align="center">🎓 Conclusão</h1>

Este projeto foi uma imersão prática no ciclo de vida inicial do dado:

**Extração bruta → Transformação → Estruturação → Persistência**

Durante o desenvolvimento, foram resolvidos desafios reais como bloqueio de requisições automatizadas, mapeamento de elementos no DOM, estruturação leve de dados desorganizados, o resultado é um dataset limpo, estruturado e pronto para análise.

---
<h1 align="center">🚀 Skills Desenvolvidas</h1>

**🕷️ Web Scraping & Automação `(requests + BeautifulSoup)`**

**🌐 Engenharia de Requisições `(headers e cookies)`**

**📊 Tratamento e estruturação com Pandas**

**💾 Serialização `(CSV vs Parquet vs Pickle)`**

**🧪 Ambientes isolados com `venv`**

**⏳ Monitoramento com `tqdm`**

> Projeto desenvolvido para fins educacionais como prática de Engenharia de Dados.