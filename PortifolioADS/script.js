document.addEventListener("DOMContentLoaded", function() {
    let pageContainer = document.querySelector('.container');

    const SAVED_LINKS = 'selectLinks';

    const links = document.querySelectorAll('.links');

    const selectLinks = localStorage.getItem(SAVED_LINKS);

    if (selectLinks) {
        document.getElementById(selectLinks).classList.add('currentLink');
    }
  
    // Intercepta o clique nos links

    links.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Impede o comportamento padrão do link (navegar para outra página)
            
            let nextPage = this.getAttribute('href');
            
            // Adiciona a classe 'fadeOut' para aplicar a transição de saída
            pageContainer.classList.add('fadeOut');

            links.forEach(link => {
                link.classList.remove('currentLink'); // Remove a classe 'currentLink' dos links
            });

            // Adiciona a classe 'currentLink' apenas ao link clicado
            this.classList.add('currentLink');

            localStorage.setItem(SAVED_LINKS, this.id);
            
            // Aguarda um curto período para que a transição de saída tenha tempo para ser concluída
            setTimeout(function() {
                // Carrega a próxima página
                window.location.href = nextPage;
            }, 500); // Ajuste este valor para corresponder à duração da transição em CSS
        });
    });
});