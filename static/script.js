document.addEventListener('DOMContentLoaded', function() {
    const buscarBtn = document.getElementById('buscar');
    const copiarBtn = document.getElementById('copiar');
    const compartilharBtn = document.getElementById('compartilhar');
    const modal = document.getElementById('share-modal');
    const closeBtn = document.querySelector('.close');
    
    // Buscar frase
    buscarBtn.addEventListener('click', async function() {
        const categoria = document.getElementById('categoria').value;
        
        document.getElementById('frase').textContent = "Buscando frase inspiradora...";
        document.getElementById('autor').textContent = "";
        
        try {
            const response = await fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `categoria=${encodeURIComponent(categoria)}`
            });
            
            const data = await response.json();
            
            if (data.error) {
                document.getElementById('frase').textContent = data.error;
                return;
            }
            
            document.getElementById('frase').textContent = data.frase;
            document.getElementById('autor').textContent = data.autor ? `— ${data.autor}` : "";
        } catch (error) {
            document.getElementById('frase').textContent = "Erro ao conectar com o servidor. Tente novamente.";
            console.error(error);
        }
    });
    
    // Copiar frase
    copiarBtn.addEventListener('click', function() {
        const frase = document.getElementById('frase').textContent;
        const autor = document.getElementById('autor').textContent;
        
        if (frase && !frase.includes("Clique no botão") && !frase.includes("Buscando")) {
            const texto = `"${frase}" ${autor}`;
            
            navigator.clipboard.writeText(texto)
                .then(() => {
                    const originalText = copiarBtn.innerHTML;
                    copiarBtn.innerHTML = '<i class="fas fa-check"></i> Copiado!';
                    
                    setTimeout(() => {
                        copiarBtn.innerHTML = originalText;
                    }, 2000);
                })
                .catch(err => {
                    console.error('Erro ao copiar:', err);
                    alert("Não foi possível copiar a frase.");
                });
        }
    });
    
    // Compartilhar frase
    compartilharBtn.addEventListener('click', function() {
        const frase = document.getElementById('frase').textContent;
        const autor = document.getElementById('autor').textContent;
        
        if (frase && !frase.includes("Clique no botão") && !frase.includes("Buscando")) {
            modal.style.display = 'block';
            
            // Configurar botões de compartilhamento
            const textoCompartilhamento = encodeURIComponent(`"${frase}" ${autor}`);
            
            document.querySelector('.whatsapp').onclick = () => {
                window.open(`https://api.whatsapp.com/send?text=${textoCompartilhamento}`, '_blank');
                modal.style.display = 'none';
            };
            
            document.querySelector('.facebook').onclick = () => {
                window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(window.location.href)}&quote=${textoCompartilhamento}`, '_blank');
                modal.style.display = 'none';
            };
            
            document.querySelector('.twitter').onclick = () => {
                window.open(`https://twitter.com/intent/tweet?text=${textoCompartilhamento}`, '_blank');
                modal.style.display = 'none';
            };
            document.querySelector('.instagram').onclick = () => {
                window.open(`https://www.instagram.com/?url=${encodeURIComponent(window.location.href)}`, '_blank');
                modal.style.display = 'none';
            }
            document.querySelector('.linkedin').onclick = () => {
                window.open(`https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(window.location.href)}&title=${textoCompartilhamento}`, '_blank');
                modal.style.display = 'none';
            };
        }
    });
    
    // Fechar modal
    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });
    
    // Fechar modal ao clicar fora
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});