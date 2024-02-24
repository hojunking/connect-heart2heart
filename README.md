# connect-heart2heart  

### Quick Start
- You need to get OpenAI chatGPT token here:(https://platform.openai.com/api-keys)  
Paste on config file.
    ```
    ./flask/config/openai_config.py
    API_KEY = ""
    ```
- Python version==3.9+
- Install Flask and OpenAI.
    ```
    pip install flask openai
    ```
- Start flask service in local environment
    ```
    cd ./flask
    flask run
    ```
    The service will be run on http://127.0.0.1:5000