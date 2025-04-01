import requests
from bs4 import BeautifulSoup
import random
import time

class FrasesScraper:
    def __init__(self):
        self.sites = [
            {
                'name': 'pensador',
                'url': 'https://www.pensador.com/{categoria}/',
                'selectors': {
                    'frases': 'p.fr',
                    'autor': 'span.author-name'
                }
            },
            {
                'name': 'citacoes',
                'url': 'https://www.citacoes.in/{categoria}/',
                'selectors': {
                    'frases': 'div.citacao p',
                    'autor': 'div.citacao small'
                }
            }
        ]
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
        })

    def get_random_frase(self, categoria):
        # Tenta sites em ordem aleatória
        sites = random.sample(self.sites, len(self.sites))
        
        for site in sites:
            frase, autor = self._scrape_site(site, categoria)
            if frase:
                return frase, autor
        
        return None, None

    def _scrape_site(self, site, categoria):
        try:
            time.sleep(random.uniform(1, 3))  # Evitar bloqueio
            
            url = site['url'].format(categoria=categoria)
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            frases = soup.select(site['selectors']['frases'])
            autores = soup.select(site['selectors']['autor'])
            
            if not frases:
                return None, None
                
            idx = random.randint(0, len(frases)-1)
            return (
                frases[idx].get_text(strip=True),
                autores[idx].get_text(strip=True) if idx < len(autores) else None
            )
            
        except Exception as e:
            print(f"Erro no site {site['name']}: {str(e)}")
            return None, None
import requests
from bs4 import BeautifulSoup
import random
import time

class FrasesScraper:
    def __init__(self):
        self.sites = [
            {
                'name': 'pensador',
                'url': 'https://www.pensador.com/{categoria}/',
                'selectors': {
                    'frases': 'p.fr',
                    'autor': 'span.author-name'
                }
            },
            {
                'name': 'citacoes',
                'url': 'https://www.citacoes.in/{categoria}/',
                'selectors': {
                    'frases': 'div.citacao p',
                    'autor': 'div.citacao small'
                }
            }
        ]
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
        })

    def get_random_frase(self, categoria):
        # Tenta sites em ordem aleatória
        sites = random.sample(self.sites, len(self.sites))
        
        for site in sites:
            frase, autor = self._scrape_site(site, categoria)
            if frase:
                return frase, autor
        
        return None, None

    def _scrape_site(self, site, categoria):
        try:
            time.sleep(random.uniform(1, 3))  # Evitar bloqueio
            
            url = site['url'].format(categoria=categoria)
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            frases = soup.select(site['selectors']['frases'])
            autores = soup.select(site['selectors']['autor'])
            
            if not frases:
                return None, None
                
            idx = random.randint(0, len(frases)-1)
            return (
                frases[idx].get_text(strip=True),
                autores[idx].get_text(strip=True) if idx < len(autores) else None
            )
            
        except Exception as e:
            print(f"Erro no site {site['name']}: {str(e)}")
            return None, None