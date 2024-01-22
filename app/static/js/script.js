document.addEventListener("DOMContentLoaded", function () {
    const categorySvg = document.querySelector(".category > a > svg");
    const crossSvg = document.querySelector(".cross > a > svg");
    const menu = document.querySelector(".menu");

    categorySvg.addEventListener("click", function (event) {
        event.preventDefault();

        categorySvg.style.display = "none";
        crossSvg.style.display = "inline-block";
        menu.style.transition = "height 0.5s ease";
        menu.style.display = "flex";

        // Lock vertical scroll
        document.body.classList.add("lock-scroll");
    });

    crossSvg.addEventListener("click", function (event) {
        event.preventDefault();

        crossSvg.style.display = "none";
        categorySvg.style.display = "inline-block";
        menu.style.transition = "height 0.5s ease";
        menu.style.display = "none";

        // Unlock vertical scroll
        document.body.classList.remove("lock-scroll");
    });
});
