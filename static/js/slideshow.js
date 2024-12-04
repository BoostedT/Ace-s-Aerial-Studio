let slideIndex = 1;
showSlides(slideIndex);

// Next/Previous Controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail Controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let slides = document.getElementsByClassName("slide");
    let thumbnails = document.getElementsByClassName("thumbnail-gallery")[0].getElementsByTagName("img");

    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    for (let i = 0; i < thumbnails.length; i++) {
        thumbnails[i].classList.remove("active");
    }

    slides[slideIndex - 1].style.display = "block";
    thumbnails[slideIndex - 1].classList.add("active");
}

