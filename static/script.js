const toggleButton = document.getElementsByClassName("toggle")[0];
const navbarNav = document.getElementsByClassName("navbar-nav")[0];

toggleButton.addEventListener('click', () => {
    navbarNav.classList.toggle('active')
  })