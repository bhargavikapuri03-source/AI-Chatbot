# My AI Assistant (Streamlit + Gemini)

Simple Streamlit chatbot that uses Google's Gemini generative models.

Requirements

- Python 3.10+ (you have Python 3.13 in this workspace)
- Install dependencies:

```bash
python -m pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install minimal packages:

```bash
python -m pip install streamlit google-generativeai python-dotenv
```

Running locally

Start the app with Streamlit (recommended):

```bash
python -m streamlit run app.py
```
# open in browser:
http://localhost:8501

Environment

Create a `.env` file to store your API key. Example `.env` contents:

```
GEMINI_API_KEY=your_api_key_here
```

Note: the repository currently reads the key from the `gemini` environment variable in `app.py`. Consider updating `app.py` to use `GEMINI_API_KEY` for clarity.

Notes

- The code currently imports `google.generativeai`, which is deprecated and prints a warning at runtime. Consider migrating to `google.genai`.

Files

- `app.py`: Streamlit app
- `.gitignore`: ignores virtualenvs, caches, `.env`, and Streamlit artifacts
