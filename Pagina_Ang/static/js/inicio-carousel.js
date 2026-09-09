document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('#slideDest');
    const slides = track ? Array.from(track.querySelectorAll('.item')) : [];
    const carousel = document.querySelector('.carrusel-container');

    if (!track || !slides.length || !carousel) {
        return;
    }

    let currentSlide = 0;
    let autoplayId;

    // Mueve la pista y activa visualmente el slide seleccionado.
    const showSlide = (slideIndex) => {
        currentSlide = (slideIndex + slides.length) % slides.length;
        track.style.transform = `translateX(-${currentSlide * 100}%)`;

        slides.forEach((slide, index) => {
            slide.classList.toggle('active', index === currentSlide);
        });
    };

    // Estas funciones quedan globales porque los botones usan onclick en la plantilla.
    window.prevSlide = () => showSlide(currentSlide - 1);
    window.nextSlide = () => showSlide(currentSlide + 1);

    // Avanza automáticamente y se detiene mientras el usuario interactúa.
    const startAutoplay = () => {
        window.clearInterval(autoplayId);
        autoplayId = window.setInterval(window.nextSlide, 5000);
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
