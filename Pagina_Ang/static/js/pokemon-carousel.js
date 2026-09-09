document.addEventListener('DOMContentLoaded', () => {
    const slides = Array.from(document.querySelectorAll('.pokemon-item'));
    const previousButton = document.querySelector('.pokemon-prev');
    const nextButton = document.querySelector('.pokemon-next');
    const counter = document.querySelector('.pokemon-counter');
    const carousel = document.querySelector('.pokemon-carousel');

    if (!slides.length || !previousButton || !nextButton || !counter) {
        return;
    }

    let currentSlide = 0;
    let autoplayId;

    // Actualiza la tarjeta visible, el estado accesible y el contador.
    const showSlide = (slideIndex) => {
        currentSlide = (slideIndex + slides.length) % slides.length;

        slides.forEach((slide, index) => {
            const isActive = index === currentSlide;
            slide.classList.toggle('active', isActive);
            slide.setAttribute('aria-hidden', String(!isActive));
        });

        counter.textContent = `${currentSlide + 1} / ${slides.length}`;
    };

    // Los botones permiten recorrer los Pokémon en ambas direcciones.
    const showPreviousSlide = () => showSlide(currentSlide - 1);
    const showNextSlide = () => showSlide(currentSlide + 1);

    previousButton.addEventListener('click', showPreviousSlide);
    nextButton.addEventListener('click', showNextSlide);

    // El teclado también permite usar el carrusel cuando tiene el foco.
    carousel.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowLeft') {
            showPreviousSlide();
        }

        if (event.key === 'ArrowRight') {
            showNextSlide();
        }
    });

    // Cambia automáticamente cada cinco segundos y se pausa al interactuar.
    const startAutoplay = () => {
        autoplayId = window.setInterval(showNextSlide, 5000);
    };

    const stopAutoplay = () => {
        window.clearInterval(autoplayId);
    };

    carousel.addEventListener('mouseenter', stopAutoplay);
    carousel.addEventListener('mouseleave', startAutoplay);
    carousel.addEventListener('focusin', stopAutoplay);
    carousel.addEventListener('focusout', startAutoplay);

    showSlide(0);
    startAutoplay();
});
