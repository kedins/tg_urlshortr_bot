import telebot
import requests
from bs4 import BeautifulSoup

TOKEN = '917017264:AAF-xT2zkWBXFv08fBmVQj6IejUlYGXYCRY'
bot = telebot.TeleBot(TOKEN)


def get_short_url(url_to_shorten):
    post_form = {'u': url_to_shorten}
    url = "https://www.shorturl.at/shortener.php"
    r = requests.post(url, post_form)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        short_url = soup.find('input', attrs={'id': 'shortenurl'})['value']
    except:
        return f'Perhaps user input is not URL'
    return short_url


@bot.message_handler(commands=['start', 'help'])
def main(message):
    bot.send_message(message.chat.id, "Введите URL: ")


@bot.message_handler(content_types=['text'])
def long_url(message):
    user_long_url = message.text
    output_shortrurl = get_short_url(user_long_url)
    bot.send_message(message.chat.id, output_shortrurl)


if __name__ == '__main__':
    bot.polling(none_stop=True)
