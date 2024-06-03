import requests
import os
import sys
import re

def truncate_title(title, max_length=27):
    if len(title) <= max_length:
        return title
    truncated = title[:max_length].rsplit(' ', 1)[0]
    if len(truncated) == 0:
        truncated = title[:max_length]
    return truncated + '...'

def main():
    if len(sys.argv) < 3:
        print("Usage: python publicaciones.py <file_path> <key>")
        return

    file_path = sys.argv[1]
    key = sys.argv[2]
    print("File path:", file_path)

    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        exit()
    
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "key": key,
        "channelId": "UCenmk0ASesMbzWXMl610aDw",  # Reemplaza con tu canal de YouTube
        "part": "snippet,id",
        "order": "date",
        "maxResults": 3
    }

    response = requests.get(url, params=params)
    data = response.json()

    videos = []
    for item in data["items"]:
        title = item["snippet"]["title"]
        truncated_title = truncate_title(title)
        video_id = item["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        thumbnail_url = item["snippet"]["thumbnails"]["medium"]["url"]
        videos.append((truncated_title, video_url, thumbnail_url))


    markdown_content = "## Últimos Videos en YouTube\n\n"
    for title, url, thumbnail in videos:
        markdown_content += f'  <a href="{url}"><img src="{thumbnail}" alt="{title}" width="33%"></a>\n'

    # Lee el contenido existente del archivo
    with open(file_path, "r", encoding="utf-8") as file:
        existing_content = file.read()

    # Verifica si la sección ya existe y actualízala
    section_pattern = r"(## Últimos Videos en YouTube\n\n.*?)(?=\n## |\Z)"
    if re.search(section_pattern, existing_content, re.DOTALL):
        updated_content = re.sub(section_pattern, markdown_content, existing_content, flags=re.DOTALL)
    else:
        updated_content = existing_content + "\n" + markdown_content

    # Guarda el contenido actualizado en el archivo
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print("Markdown content generated and appended successfully!")

if __name__ == "__main__":
    main()
