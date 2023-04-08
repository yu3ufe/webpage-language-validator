# Webpage Language Validator

Webpage Language Validator is a Flask web application that checks if a list of URLs have been translated into a specific language. The application uses Selenium, BeautifulSoup, and Google Cloud Translate API to navigate to each URL, parse its HTML content, and detect the language of text within certain HTML tags. The results of the URL checks are displayed to the user in an easy-to-read format.

## Installation

To run this script, you will need to have Python 3 installed on your system. You will also need to install the following Python packages:

- Flask
- BeautifulSoup
- Selenium
- google-cloud-translate

You can install these packages using `pip` by running the following command:

```
pip install Flask beautifulsoup4 selenium google-cloud-translate
```

You will also need to have a Google Cloud account and a JSON file containing your Google Cloud API credentials. You can learn more about how to set up a Google Cloud account and obtain API credentials [here](https://cloud.google.com/translate/docs/setup).

## Usage

To run this script, navigate to the directory where the script is located and run the following command:

```
python language_validator.py --google-credentials /path/to/GOOGLE_CREDENTIALS.json
```

Make sure to replace `/path/to/GOOGLE_CREDENTIALS.json` with the actual path to your Google Cloud API credentials JSON file.

The script accepts several command-line arguments that allow you to customize its behavior:

- `-l`, `--language`: The language code to check for translation (default: `en`)
- `-c`, `--css-class`: The CSS class to search for (default: `container`)
- `-d`, `--debug`: Enable debug mode (default: `False`)
- `-t`, `--host`: The host IP address (default: `127.0.0.1`)
- `-p`, `--port`: The port number (default: `5000`)
- `-s`, `--google-credentials`: The path to the Google credentials JSON file (required)

You can provide values for these arguments when running the script to customize its behavior. For example, to run the script in debug mode and check for translation into French, you can use the following command:

```
python language_validator.py -s /path/to/GOOGLE_CREDENTIALS.json --debug --language fr
```

Once the script is running, you can access the web application by opening a web browser and navigating to `http://localhost:5000`. This will display a form where you can enter a list of URLs separated by newline characters. After entering the URLs, click the "check" button to submit the form and see the results of the URL checks.

## Customization

You can customize this script to fit your specific needs by modifying its code. For example, you can change the list of HTML tags that are searched for text by modifying the `tags` variable. You can also change the number of tags that are checked by modifying the loop condition in the `index` function.

If you want to check for other conditions besides translation, you can add additional checks in the `index` function. For example, you could check if the page contains certain keywords or if it has a specific structure.

Make sure to thoroughly test any changes you make to ensure that they work as intended.

## Contributions

Contributions are welcome! If you find any bugs or have suggestions for improving the script, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
