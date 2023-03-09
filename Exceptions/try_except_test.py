import requests

urls= ["https://www.syntraab.be", "https://www.syntra-ab.be"]

def chec_url(url):
    try:
        response = requests.get(url)
        print(response.status_code)
    except requests.ConnectionError:
        print("2e error")
    except:
        print(f"{url} not found")
    finally:
        print("F--------INAL")

for url in urls:
    chec_url(url)