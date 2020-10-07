import requests
import fire
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound
from os import system
from googletrans import Translator

#languages use ISO language codes. 
#examples of language codes:
#French = 'fr'
#English = 'en'
#Hindi = 'hi'
#Spanish = 'es'

def play_article(url, lang='en'):
    system('clear')
    url = url
    page = requests.get(url).text
    soup = BeautifulSoup(page, features="lxml")

    title = soup.find("h1").get_text()

    p_tags = soup.find_all("p")
    p_text = [tag.get_text().strip() for tag in p_tags]
    sentence_list = [sentence for sentence in p_text if not "\n" in sentence]
    sentence_list_final = [
        sentence for sentence in sentence_list if "." in sentence
    ]

    article_text = " ".join(sentence_list_final)
    #creating an instance of the Translator class from googletrans library
    #in order to translate the article to the chosen language.
    translator = Translator()
    article_text_translated = translator.translate(article_text, dest=lang)
    
    print('The article is being downloaded and translated for text to speech. This may take some time... ')
    
    try:
        tts = gTTS(article_text_translated.text, lang=lang)
        tts.save("article.mp3")
        playsound("article.mp3")
    except ValueError:
        print(f'ERROR: The selected language "{lang}" is not supported.')
    
    

if __name__ == '__main__':
    fire.Fire(play_article)
    