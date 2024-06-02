import os
from datetime import datetime

# Specify the path to the markdown file
markdown_file = "./README.MD"

# Determine the current greeting based on the time of day
current_hour = datetime.now().hour

if 6 <= current_hour < 12:
    greeting = "¡Buenos días! 🌅"
elif 12 <= current_hour < 18:
    greeting = "¡Buenas tardes! ☀️"
else:
    greeting = "¡Buenas noches! 🌙"

# Define possible greetings that could be in the markdown file
possible_greetings = ["# ¡Buenos días! 🌅", "# ¡Buenas tardes! ☀️", "# ¡Buenas noches! 🌙"]

# Read the contents of the markdown file
with open(markdown_file, "r", encoding="utf-8") as file:
    markdown_content = file.read()

# Replace any existing greeting with the new greeting
for existing_greeting in possible_greetings:
    if existing_greeting in markdown_content:
        markdown_content = markdown_content.replace(existing_greeting, f"# {greeting}")

# Write the updated markdown content back to the file
with open(markdown_file, "w", encoding="utf-8") as file:
    file.write(markdown_content)

print("Markdown file updated successfully!")
