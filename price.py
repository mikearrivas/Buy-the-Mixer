#Buy the Mixer if it's less than $1,900.00
import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.musiciansfriend.com/pro-audio/rane-seventy-two-battle-ready-2-channel-dj-mixer-with-touchscreen-and-serato-dj")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("var", {"class": "hidden price", "itemprop": "price"})
string_price = (element.text.strip())
price_without_symbol = string_price[0:]
price = (float(price_without_symbol))
threshold = (int(1900))

if price < threshold:
    print("Buy the Rane SEVENTY-TWO Battle-Ready 2-channel DJ Mixer with Touchscreen and Serato DJ")
    print("The current price is {}.".format(string_price))
    print("It's less than ${}.".format(threshold))
else:
    print("Don't buy the Rane SEVENTY-TWO Battle-Ready 2-channel DJ Mixer with Touchscreen and Serato DJ!")
    print("It's more than ${}.".format(threshold))
