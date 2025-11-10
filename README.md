# AI Story Teller

This app creates a unique story from your images. Just upload one or more pictures, choose a style (like Mystery, Morale, or Thriller), and click "Tell a Story." The AI will generate a short story in text and provide an audio version you can listen to.

## Quick Start

### 1. Get Your API Key

You need a Google API key to run this app.

1.  Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Sign in and click **Get API key**.
3.  Select **Create API key in new project**.
4.  Copy the key that is generated.

### 2. Set Up the Project

First, get the code onto your machine.

Clone the project (replace with your repository URL)

`git clone https://github.com/Chetax/ai_story_teller.git'`  
`cd ai_story_teller`

Create a virtual environment

`python3 -m venv venv`  
`source venv/bin/activate # On Windows: .\venv\Scripts\activate`

Install required packages

`pip install -r requirements.txt`


### 3. Add Your API Key

Create a file named `.env` in the main project folder and add your key like this:

GOOGLE_API_KEY="PASTE_YOUR_API_KEY_HERE"

### 4. Run the App

Start the application with this command:

`streamlit run main.py`

Now you can open the app in your web browser at the local URL provided (usually `http://localhost:8501`).
