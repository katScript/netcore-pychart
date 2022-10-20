// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

$(document).ready(function(){
    const el = $(".col-img");

    Array.from(el).forEach(function (element) {
        element.addEventListener('mouseover', function handleMouseOver() {
            this.querySelector(".tech-content").style.display = 'block';
        });
    });

    Array.from(el).forEach(function (element) {
        element.addEventListener('mouseout', function handleMouseOver() {
            this.querySelector(".tech-content").style.display = 'none';
        });
    });
    
    const aj = $('#ai-jobs');

    aj.hover(function(){
        $('#sec3-img').fadeIn(1000);
    });
});

