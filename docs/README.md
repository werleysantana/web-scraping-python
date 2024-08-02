# Web Scraping Python Project

## Visão Geral

Este projeto realiza scraping na biblioteca de transparência de anúncios do Google para recuperar metadados de anúncios do YouTube relacionados aos domínios inseridos na aplicação. 

## Escalabilidade

O projeto armazena os dados coletados em um banco de dados MongoDB. Uso do MongoDB para armazenamento, o que é adequado para grandes volumes de dados.

Caso desejo acessar o MongoDB Atlas, o IP está 'anywhere' e segue abaixo o URI
"MONGO_URI=mongodb+srv://scraping:testScrapingPython@scraping-python.u86jrcd.mongodb.net/"

Este guia também cobre a configuração do Docker, a implementação de cache com Redis e um exemplo básico de balanceamento de carga com Nginx. Com essas adições, o projeto será mais robusto, escalável e preparado para lidar com grandes volumes de dados e requisições.

## Objetivo solicitado

Acessar a biblioteca de transparência de anúncios do Google e retornar os anúncios do YouTube.

## Requisitos solicitados

1. A aplicação deve permitir a inserção de um ou mais domínios ou landing pages.
2. Para cada domínio ou landing page, a aplicação deve retornar os seguintes dados dos anúncios do YouTube:
    - Título do Vídeo
    - Título do Canal
    - Duração do Vídeo
    - Quantidade de Views
    - Quantidade de Likes
    - Link da Thumbnail
    - Indicação se é um YouTube Shorts ou não
    - Transcrição do Vídeo
    - Data de Publicação
    - Link do Vídeo

## Estrutura do Projeto

web-scraping-python/
env/
setup.py

src/
init.py
main.py

scraper/
init.py
google_ads_transparency.py
youtube_scraper.py

utils/
nit.py
data_processing.py
logger.py
cache.py

database/
init.py
mongo_client.py
data_storage.py

tests/
test_google_ads_transparency.py
test_youtube_scraper.py
test_database.py

docs/
README.md

data/
example_data.json

.env
.gitignore
Dockerfile
docker-compose.yml
nginx.conf

## Orientado a teste

No projeto, há também um módulo na qual implementamos testes para os principais arquivos da aplicação.

## Configuração

### Pré-requisitos

- Python 3.x
- pip
- MongoDB
- Docker
- Docker Compose

### Dependências usadas

- requests
- beautifulsoup4
- selenium
- pymongo
- youtube-transcript-api
- webdriver-manager
- redis

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/web-scraping-python.git
cd web-scraping-python