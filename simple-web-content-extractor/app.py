from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = '2002'

def get_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Extract text from the webpage (ignore the tag name)
        text = ""
        for tag in soup.find_all():
            text += tag.get_text() + "\n"

        return text.strip()
    except requests.exceptions.RequestException as e:
        print("Error fetching content:", e)
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        extracted_text = get_text_from_url(url)

        if extracted_text:
            return render_template('index.html', extracted_text=extracted_text)
        else:
            return render_template('index.html', error_message="Failed to extract text from the URL.")

    return render_template('index.html')

if __name__ == "__main__":
    app.run()