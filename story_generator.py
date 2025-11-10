from dotenv import load_dotenv
import os
from google import genai 
from gtts import gTTS
from io import BytesIO 


load_dotenv()

gemini_api_key=os.getenv("GOOGLE_API_KEY")

if not gemini_api_key:
    raise ValueError("API key not found")

client=genai.Client(api_key=gemini_api_key)



def create_advanced_prompt(style):
    # --- Base prompt ---
    base_prompt = f"""
    **Goal:** Write a short story in the '{style}' genre.

    **Core Task:** Create one single story that connects all the provided images in order. The story must be easy to understand and written in plain English.

    **Instructions:**
    -   **Title:** Start with a simple title.
    -   **Length:** The story must be a maximum of three paragraphs.
    -   **Content:** Include a key detail from every image.
    -   **Setting:** Use only Indian names, characters, and places.
    """


    # --- Add Style-Specific Instructions ---
    style_instruction = ""
    if style == "Morale":
        style_instruction = "\n**Special Section:** After the story, add a section starting with `[MORAL]:` followed by the single-sentence moral of the story."
    elif style == "Mystery":
        style_instruction = "\n**Special Section:** After the story, add a section starting with `[SOLUTION]:` that reveals the culprit and the key clue."
    elif style == "Thriller":
        style_instruction = "\n**Special Section:** After the story, add a section starting with `[TWIST]:` that reveals a final, shocking twist."


    return base_prompt + style_instruction


def generate_story_from_images(images,style):
    response=client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=[images,create_advanced_prompt(style)]
    )
    return response.text 


def narate_stroy(story_text):
    try:
        tts=gTTS(text=story_text,lang="en",slow=False)
        audio_fp=BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0) # by this it come to starting points reading 
        return audio_fp
    except Exception as e:
        return f"An unExpected error has occured {e}"
   





