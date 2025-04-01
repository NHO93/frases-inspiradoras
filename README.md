# Frases Inspiradoras

## 📌 Visão Geral

Aplicação web que busca e exibe frases inspiradoras de diversos sites automaticamente, com opções para compartilhamento nas redes sociais. Desenvolvida em Python com Flask no backend e HTML/CSS/JavaScript no frontend.

## ✨ Funcionalidades

- 🔍 Busca automática de frases em múltiplos sites
- 🎨 Interface limpa e responsiva
- 📱 Compatível com dispositivos móveis e desktop
- 📋 Cópia fácil das frases para área de transferência
- 📤 Compartilhamento direto no WhatsApp, Facebook e Twitter
- 🏷️ Organização por categorias (amor, motivação, felicidade, etc.)
- 🔄 Atualização aleatória de frases

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3**
- **Flask** (Framework web)
- **BeautifulSoup4** (Web scraping)
- **Requests** (Requisições HTTP)

### Frontend
- HTML5
- CSS3 (com design responsivo)
- JavaScript (Vanilla)
- Font Awesome (Ícones)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- pip (Gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/NHO93/frases-inspiradoras.git
cd frases-inspiradoras
```

2. Crie e ative um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Execução
```bash
python app.py
```

A aplicação estará disponível em: [http://localhost:5000](http://localhost:5000)

## 🏗️ Estrutura do Projeto

```
frases-inspiradoras/
├── app.py                # Aplicação principal (Flask)
├── scraper.py            # Módulo de web scraping
├── requirements.txt      # Dependências do Python
├── README.md             # Este arquivo
├── templates/
│   └── index.html        # Template principal
└── static/
    ├── style.css         # Estilos CSS
    └── script.js         # JavaScript do frontend
```

## 🌐 Sites Suportados para Scraping

- Pensador.com
- Citacoes.in

*(A aplicação foi projetada para fácil adição de novos sites)*

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

**Nota**: Esta aplicação é destinada apenas para fins educacionais. O web scraping pode violar os termos de serviço de alguns sites. Use com responsabilidade.# frases-inspiradoras
# frases-inspiradoras
