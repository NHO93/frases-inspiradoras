from flask import Flask, render_template, request, jsonify
from scraper import FrasesScraper

app = Flask(__name__)
scraper = FrasesScraper()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        categoria = request.form.get('categoria')
        
        # Busca frase de qualquer site disponível
        frase, autor = scraper.get_random_frase(categoria)
        
        if not frase:
            return jsonify({
                'error': 'Não foi possível obter uma frase no momento. Tente novamente mais tarde.'
            }), 500
        
        return jsonify({
            'frase': frase,
            'autor': autor or "Autor desconhecido"
        })
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    