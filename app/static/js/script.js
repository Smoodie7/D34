document.addEventListener("DOMContentLoaded", function () {
    // Get references to the elements
    const categorySvg = document.querySelector(".category > a > svg");
    const crossSvg = document.querySelector(".cross > a > svg");
    const menu = document.querySelector(".menu");

    // Add click event listener to category SVG
    categorySvg.addEventListener("click", function (event) {
        event.preventDefault();

        // Hide category SVG
        categorySvg.style.display = "none";

        // Show cross SVG
        crossSvg.style.display = "inline-block";

        // Show menu with smooth transition
        menu.style.transition = "height 0.5s ease";
        menu.style.display = "flex";
    });

    // Add click event listener to cross SVG
    crossSvg.addEventListener("click", function (event) {
        event.preventDefault();

        // Hide cross SVG
        crossSvg.style.display = "none";

        // Show category SVG
        categorySvg.style.display = "inline-block";

        // Hide menu with smooth transition
        menu.style.transition = "height 0.5s ease";
        menu.style.display = "none";
    });
});
