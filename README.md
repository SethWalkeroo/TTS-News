# Text To Speech News!

An easy to use text to speech application that reads news articles! This application uses a combination of Python's BeautifulSoup library, Google Translate, and Google's text to speech engine to audibly read news articles on the internet in any desired language! (or any other type of article).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
pip3 install -r requirements.txt
```

## Example Usage

 Just enter the tts-news directory and simply enter a url as an argument to the "--url" parameter and then enter a language code as an argument to the "--lang" parameter. A list of ISO 639-1 language codes can be found _here:_ https://www.loc.gov/standards/iso639-2/php/code_list.php

```bash
python3 ttsnews.py --url="https://rb.gy/wtqtor" --lang="en"
```

The script will download and store an mp3 file in the current directory. You can choose what to do with that :)