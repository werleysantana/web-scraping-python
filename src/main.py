from scraper.youtube_scraper import search_youtube_videos
from database.data_storage import store_data_in_db
from utils.logger import setup_logging
import logging

setup_logging()

def main():
    domains = [
        "https://creatify.ai/?utm_source=google&utm_medium=ppc&utm_campaign=21338417757&utm_term=ai%20generated%20ads&utm_content=701068221309&gad_source=2&gclid=EAIaIQobChMIq6Sb_rTVhwMVZ0RIAB0IfBk7EAEYASAAEgIMo_D_BwE", 
        "https://clickup.com/features/whiteboards?utm_campaign=yt_whiteboards-22&utm_medium=social&utm_source=youtube&utm_content=video_caveman-hero&utm_term=organic"]
    queries = [f"ads {domain}" for domain in domains]

    youtube_data = []
    for query in queries:
        videos = search_youtube_videos(query)
        youtube_data.extend(videos)

    if youtube_data:
        logging.info(f"Armazenando {len(youtube_data)} vídeos no banco de dados.")
        store_data_in_db(youtube_data)
    else:
        logging.warning("Nenhum dado de vídeo do YouTube para armazenar.")

if __name__ == "__main__":
    main()