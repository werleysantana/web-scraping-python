import os
import requests
import json
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
from utils.cache import cache_get, cache_set

def search_youtube_videos(query, max_results=10):
    api_key = os.getenv("YOUTUBE_API_KEY")
    api_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&maxResults={max_results}&key={api_key}"

    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Erro ao acessar a API do YouTube para a consulta '{query}'")
        return []

    data = response.json()
    videos = []

    for item in data.get('items', []):
        video_id = item['id'].get('videoId')
        if video_id:
            video_details = get_youtube_video_details(video_id)
            videos.append(video_details)

    return videos

def get_youtube_video_details(video_id):
    cached_data = cache_get(video_id)
    if cached_data:
        return json.loads(cached_data)
    
    api_key = os.getenv("YOUTUBE_API_KEY")
    details = {}

    api_url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=snippet,contentDetails,statistics&key={api_key}"
    
    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Erro ao acessar os detalhes do vídeo do YouTube para {video_id}")
        return details

    data = response.json()
    if not data['items']:
        print(f"Nenhum dado encontrado para o vídeo {video_id}")
        return details

    video_data = data['items'][0]

    details['title'] = video_data['snippet']['title']
    details['channel_title'] = video_data['snippet']['channelTitle']
    details['duration'] = video_data['contentDetails']['duration']
    details['views'] = video_data['statistics']['viewCount']
    details['likes'] = video_data['statistics'].get('likeCount', 0)
    details['thumbnail'] = video_data['snippet']['thumbnails']['high']['url']
    details['is_shorts'] = 'shorts' in video_data['snippet']['categoryId']
    details['published_at'] = video_data['snippet']['publishedAt']
    details['video_url'] = f"https://www.youtube.com/watch?v={video_id}"

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        details['transcript'] = ' '.join([t['text'] for t in transcript])
    except NoTranscriptFound:
        details['transcript'] = 'Transcrição não encontrada'
        print(f"Transcrição não encontrada para o vídeo: {video_id}")
    except TranscriptsDisabled:
        details['transcript'] = 'Transcrições desativadas'
        print(f"Transcrições desativadas para o vídeo: {video_id}")
    except Exception as e:
        details['transcript'] = 'Erro ao obter transcrição'
        print(f"Erro ao obter transcrição do vídeo {video_id}: {e}")

    cache_set(video_id, json.dumps(details))
    return details