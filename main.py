import telebot
import requests
from bs4 import BeautifulSoup
import cfg

bot = telebot.TeleBot(cfg.TOKEN)


def get_short_url(url_to_shorten):
    post_form = {'u': url_to_shorten}  # form for making post request
    url = "https://www.shorturl.at/shortener.php"
    r = requests.post(url, post_form)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        short_url = soup.find('input', attrs={'id': 'shortenurl'})['value']
    except TypeError:
        return f'Perhaps user input is not URL'
    return short_url


@bot.message_handler(commands=['start', 'help'])  # When command is received bot will return message
def main(message):
    bot.send_message(message.chat.id, "Введите URL: ")


@bot.message_handler(content_types=['text'])
def long_url(message):  # When text is received bot will call get_short_url function and output short url
    user_long_url = message.text  # Get message from user
    output_shortrurl = get_short_url(user_long_url)
    bot.send_message(message.chat.id, output_shortrurl)


if __name__ == '__main__':
    bot.polling(none_stop=True)
