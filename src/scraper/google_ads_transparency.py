from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import logging

def get_ads_for_domains(domains):
    ads = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    for domain in domains:
        logging.info(f"Acessando biblioteca de transparência para o domínio: {domain}")
        domain_ads = get_ads_for_domain(driver, domain)
        logging.info(f"Anúncios encontrados para {domain}: {len(domain_ads)}")
        ads.extend(domain_ads)
    
    driver.quit()
    return ads

def get_ads_for_domain(driver, domain):
    ads = []
    base_url = f"https://adstransparency.google.com/?region=anywhere&domain={domain}&platform=YOUTUBE"
    
    driver.get(base_url)
    try:
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-id='ad']"))
        )
        time.sleep(15)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        logging.info("Estrutura HTML da página carregada:")
        logging.info(soup.prettify()[:1000])

        video_elements = soup.find_all("div", attrs={"data-id": "ad"})
        logging.info(f"Número de elementos de anúncios encontrados: {len(video_elements)}")

        for video_element in video_elements:
            ad_info = extract_ad_info(video_element)
            if ad_info:
                ads.append(ad_info)

    except Exception as e:
        logging.error(f"Erro ao acessar os anúncios para {domain}: {e}")

    return ads

def extract_ad_info(video_element):
    try:
        title_element = video_element.find("h3")
        title = title_element.get_text(strip=True) if title_element else "N/A"

        channel_element = video_element.find("div", class_="ZjXmG")
        channel = channel_element.get_text(strip=True) if channel_element else "N/A"

        video_link_element = video_element.find("a")
        video_url = video_link_element["href"] if video_link_element else "N/A"

        video_id = extract_video_id(video_url)
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

        return {
            "title": title,
            "channel": channel,
            "video_url": video_url,
            "thumbnail_url": thumbnail_url,
            "video_id": video_id,
        }
    except Exception as e:
        logging.error(f"Erro ao extrair informações do vídeo: {e}")
        return None

def extract_video_id(video_url):
    return video_url.split('v=')[-1].split('&')[0]