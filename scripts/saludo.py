import os
from datetime import datetime
from pytz import timezone

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <folder_path>")
        return

    folder_path = sys.argv[1]
    print("Folder path:", folder_path)

    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        exit()

    hora_server = datetime.now().hour

    print(f"La hora servidor es: {hora_server}")

    santiago_timezone = timezone('America/Santiago')
    current_time = datetime.now(santiago_timezone)
    current_hour = current_time.strftime("%H")
    current_hour = int(current_hour)

    print(f"La hora es: {current_hour}")

    if 6 <= current_hour < 12:
        greeting = "¡Buenos días! 🌅"
    elif 12 <= current_hour < 20:
        greeting = "¡Buenas tardes! ☀️"
    else:
        greeting = "¡Buenas noches! 🌙"

    # Define possible greetings that could be in the markdown file
    possible_greetings = ["# ¡Buenos días! 🌅", "# ¡Buenas tardes! ☀️", "# ¡Buenas noches! 🌙"]

    # Specify the path to the markdown file
    markdown_file = "README.MD"
    
    # Construct the full path to the markdown file
    markdown_file_path = os.path.join(folder_path, markdown_file)

    # Read the contents of the markdown file
    with open(markdown_file_path, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    # Replace any existing greeting with the new greeting
    for existing_greeting in possible_greetings:
        if existing_greeting in markdown_content:
            markdown_content = markdown_content.replace(existing_greeting, f"# {greeting}")

    # Write the updated markdown content back to the file
    with open(markdown_file_path, "w", encoding="utf-8") as file:
        file.write(markdown_content)

    print("Markdown file updated successfully!")

if __name__ == "__main__":
    main()
