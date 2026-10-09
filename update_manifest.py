import os

manifest_content = """const GalleryManifest = [
    {
        path: "images/adithya_college.png",
        title: "Main Campus View",
        caption: "A view of the main building of Adithya College of Arts and Science.",
        category: "campus"
    },
"""

categories = ['campus', 'events', 'library']

# we have 23 images
for i in range(1, 24):
    category = "campus"
    title = f"Campus Image {i}"
    caption = "A beautiful view of the Adithya College campus."
    
    if i in [18, 19, 20]:
        category = "library"
        title = f"College Library {i-17}"
        caption = "The well-equipped digital library for students."
    elif i in [5, 6, 21, 22, 23]:
        category = "events"
        title = f"College Event {i}"
        caption = "Students participating in college events and activities."
        
    manifest_content += f"""    {{
        path: "images/gallery/acas-gallery-{i}.jpg",
        title: "{title}",
        caption: "{caption}",
        category: "{category}"
    }},
"""

manifest_content += "];\n"

with open(r'C:\Users\veera\.gemini\antigravity\scratch\AI_Student_Chatbot\AI_Student_Chatbot\data\gallery-manifest.js', 'w') as f:
    f.write(manifest_content)

print("Gallery manifest updated!")
