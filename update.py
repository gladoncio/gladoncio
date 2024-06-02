import os
from datetime import datetime

# Specify the path to the folder and the markdown file
folder_path = "./"
markdown_file = "README.MD"

# Verify if the folder exists
if not os.path.exists(folder_path):
          print(f"Folder '{folder_path}' does not exist.")
          exit()

# Determine the current greeting based on the time of day
current_hour = datetime.now().hour

print(f"La hora es: {current_hour}")

if 6 <= current_hour < 12:
          greeting = "¡Buenos días! 🌅"
elif 12 <= current_hour < 18:
          greeting = "¡Buenas tardes! ☀️"
else:
          greeting = "¡Buenas noches! 🌙"

# Define possible greetings that could be in the markdown file
possible_greetings = ["# ¡Buenos días! 🌅", "# ¡Buenas tardes! ☀️", "# ¡Buenas noches! 🌙"]

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
