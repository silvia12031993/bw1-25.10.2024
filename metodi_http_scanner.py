import http.client
import requests

host = ("http://" + input("ip host: "))
port = input("porta (default:80): ")

if (port == ""):
	port = 80

# Indirizzo completo dell'host
url = host + ":" + str(port)

# Fare la richiesta HTTP
response = requests.options(url)
    
# Controllare se ci sono metodi HTTP attivi
if 'allow' in response.headers:
    print("\nI metodi HTTP supportati sono:", response.headers['allow'])
else:
    print("\nNon ci sono metodi HTTP attivi.")
