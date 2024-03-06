document.addEventListener("DOMContentLoaded", function() {
    var toggleButton = document.getElementById('navbar-toggle');
    var navLinks = document.getElementById('bulucu').querySelectorAll('.nav-link');

    toggleButton.addEventListener('click', function() {
        console.log(toggleButton);
        console.log(navLinks);
        navLinks.forEach(function(link) {
            link.classList.toggle('d-inline');
        });
    });
});