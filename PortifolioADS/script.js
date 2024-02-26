document.addEventListener("DOMContentLoaded", function() {
    let pageContainer = document.querySelector('.container');
  
    // Intercepta o clique nos links
    document.querySelectorAll('.links').forEach(function(link) {
      link.addEventListener('click', function(event) {
        event.preventDefault(); // Impede o comportamento padrão do link (navegar para outra página)
        
        let nextPage = this.getAttribute('href');
        
        // Adiciona a classe 'fadeOut' para aplicar a transição de saída
        pageContainer.classList.add('fadeOut');
        
        // Aguarda um curto período para que a transição de saída tenha tempo para ser concluída
        setTimeout(function() {
          // Carrega a próxima página
          window.location.href = nextPage;
        }, 500); // Ajuste este valor para corresponder à duração da transição em CSS
      });
    });
  });
  