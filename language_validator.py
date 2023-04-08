from flask import Flask, request, render_template
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from google.cloud import translate_v2 as translate
import argparse

# set arguments
parser = argparse.ArgumentParser(description='Process command-line arguments.')
parser.add_argument('-l', '--language', type=str, default='en', help='Language code to check for translation')
parser.add_argument('-c', '--css-class', type=str, default='container', help='CSS class to search for')
parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')
parser.add_argument('-t' ,'--host', type=str, default='127.0.0.1', help='Host IP address')
parser.add_argument('-p', '--port', type=int, default=5000, help='Port number')
parser.add_argument('-s', '--google-credentials', type=str, required=True, help='Path to the Google credentials JSON file')

args = parser.parse_args()

# Set the environment variable for your Google Cloud API key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = args.google_credentials

# Instantiates a client
translate_client = translate.Client()
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
tags = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        urls = request.form['urls'].split('\n')
        results = []
        for url in urls:
            try:
                driver.get(url)
                # Get the content of the final page
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')

                if soup.find(class_=args.css_class):
                    # Translation Check
                    translated = False
                    for tag_name in tags:
                        for i, tag in enumerate(soup.find_all(tag_name)):
                            if i >= 5:
                                break
                            text = tag.string
                            if text is not None:
                                source_language = translate_client.detect_language(text)['language']
                                if source_language == args.language:
                                    translated = True
                                    break
                        if translated:
                            break

                    # Conditions Check
                    if translated:
                        results.append(f'{url} | PASS')
                    else:
                        results.append(f'{url} | FAIL | page is not translated')
                else:
                    results.append(f'{url} | FAIL | wrong page')
            except:
                results.append(f'{url} | FAIL | the URL is likely broken')
        return render_template('index.html', results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host=args.host, port=args.port, debug=args.debug)