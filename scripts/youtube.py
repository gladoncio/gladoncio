import requests
import os
import sys
import re

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
        video_id = item["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        thumbnail_url = item["snippet"]["thumbnails"]["medium"]["url"]
        videos.append((title, video_url, thumbnail_url))

    # Define el tamaño de las imágenes
    thumbnail_width = 290
    thumbnail_height = 160

    # Genera el contenido en Markdown usando HTML
    markdown_content = "## Últimos Videos en YouTube\n\n"
    markdown_content += '<div style="display: flex; justify-content: space-around;">\n'
    for title, url, thumbnail in videos:
        markdown_content += f'  <div style="text-align: center; margin: 10px;">\n'
        markdown_content += f'    <a href="{url}"><img src="{thumbnail}" alt="{title}" width="{thumbnail_width}" height="{thumbnail_height}"></a>\n'
        markdown_content += f'    <p>{title}</p>\n'
        markdown_content += '  </div>\n'
    markdown_content += '</div>\n'

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
