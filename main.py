import requests
import time

API_KEY = "fcHhwSxndZW3j5xPUzngKxyZQzKry3kTWjPKflSJEqMwmiRcTu23yWMu7gLQ"
STORE_ID = "Shop GaLo"
SEARCH_TERMS = ["câmera wifi", "segurança", "smart home", "eletrônicos"]

def buscar_produtos(term):
    url = f"https://api.mercado.com/produtos?search={term}"
    try:
        r = requests.get(url)
        return r.json()
    except:
        return []

def enviar_para_loja(produto):
    url = "https://api.cartpanda.com/add-product"
    payload = {
        "apikey": API_KEY,
        "store": STORE_ID,
        "title": produto["title"],
        "price": produto["price"],
        "image": produto["image"]
    }
    try:
        requests.post(url, json=payload)
    except:
        pass

def alien_bot():
    print("🤖 ALIEN BOT v1 iniciado...")
    while True:
        for termo in SEARCH_TERMS:
            produtos = buscar_produtos(termo)
            for p in produtos:
                enviar_para_loja(p)
        time.sleep(3600)

alien_bot()
