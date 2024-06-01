const navbarMenu = document.querySelector(".navbar .links");
const hamburgerBtn = document.querySelector(".hamburger-btn");
const hideMenuBtn = navbarMenu.querySelector(".close-btn");
// const showPopupBtn = document.querySelector(".login-btn");
const formPopup = document.querySelector(".form-popup");
// const hidePopupBtn = formPopup.querySelector(".close-btn");
// const signupLoginLink = formPopup.querySelectorAll(".bottom-link a");

hamburgerBtn.addEventListener("click", () => {
    navbarMenu.classList.toggle("show-menu");
});

hideMenuBtn.addEventListener("click", () =>  hamburgerBtn.click());

// showPopupBtn.addEventListener("click", () => {
//     document.body.classList.toggle("show-popup");
// });

hidePopupBtn.addEventListener("click", () => showPopupBtn.click());

signupLoginLink.forEach(link => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
        formPopup.classList.toggle("show-signup");
    });
});
