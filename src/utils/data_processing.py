def clean_text(text):
    """
    Limpa e normaliza o texto, removendo espaços em branco extras e caracteres especiais.
    """
    if not isinstance(text, str):
        return text
    return ' '.join(text.split())

def normalize_video_data(video_data):
    """
    Normaliza os dados do vídeo para garantir consistência antes de armazenar no banco de dados.
    """
    for key in video_data:
        if isinstance(video_data[key], str):
            video_data[key] = clean_text(video_data[key])
    return video_data