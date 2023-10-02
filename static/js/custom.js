// Function to update the parallax background position
function updateParallax() {
    const scrollY = window.scrollY;
    const hero = document.querySelector('.hero');

    // Adjust the background position based on the scroll position
    hero.style.backgroundPosition = `center ${-scrollY * 0.5}px`;
}

function navScroll() {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('navbar-scrolled');
    } else {
        navbar.classList.remove('navbar-scrolled');
    }
}

function pageScroll(){
    updateParallax();
    navScroll();
}

// Listen for scroll events to update the parallax effect
window.addEventListener('scroll', pageScroll);
