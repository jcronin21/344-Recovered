const data = [
  {
    image_url: "https://picsum.photos/450/300?n=1",
    caption: "Photo 1",
  },
  {
    image_url: "https://picsum.photos/450/300?n=2",
    caption: "Photo 2",
  },
  {
    image_url: "https://picsum.photos/450/300?n=3",
    caption: "Photo 3",
  },
  {
    image_url: "https://picsum.photos/450/300?n=4",
    caption: "Photo 4",
  },
  {
    image_url: "https://picsum.photos/450/300?n=5",
    caption: "Photo 5",
  },
  {
    image_url: "https://picsum.photos/450/300?n=6",
    caption: "Photo 6",
  },
  {
    image_url: "https://picsum.photos/450/300?n=7",
    caption: "Photo 7",
  },
  {
    image_url: "https://picsum.photos/450/300?n=8",
    caption: "Photo 8",
  },
  {
    image_url: "https://picsum.photos/450/300?n=9",
    caption: "Photo 9",
  },
  {
    image_url: "https://picsum.photos/450/300?n=10",
    caption: "Photo 10",
  }
];
const carousel = document.querySelector(".carousel");
const carouselInner = document.querySelector(".carousel-inner");
const nextButton = document.querySelector(".forward");
const prevButton = document.querySelector(".back");
const slides = carouselInner.children;
const totalSlides = slides.length;
let currentSlide = 0

carouselInner.style.transform= "translateX(0%)";

function loadSlides(photoList) {
  for (let i = 0; i < photoList.length; i++) {
    const slide = document.createElement("section");
    slide.classList.add("carousel-item");
    slide.setAttribute("role", "group");
    slide.setAttribute("aria-label", `slide ${i + 1} of ${photoList.length}`);

    const img = document.createElement("img");
    img.setAttribute("src", photoList[i].image_url);
    img.setAttribute("alt", photoList[i].caption);
    img.addEventListener("click", showNextSlide);

    const caption = document.createElement("p");
    caption.textContent = photoList[i].caption;
    caption.classList.add("carousel-caption");

    slide.appendChild(img);
    slide.appendChild(caption);
    carouselInner.appendChild(slide);
  }
  slides[0].setAttribute("aria-hidden", "false");
}


function showNextSlide() {
  let nextSlide = currentSlide + 1;
  if (nextSlide >= totalSlides) {
    nextSlide = 0;
  }
  goToSlide(nextSlide);
}


function showPrevSlide() {
  let prevSlide = currentSlide - 1;
  if (prevSlide < 0) {
    prevSlide = totalSlides - 1;
  }
  goToSlide(prevSlide);
}


function goToSlide(slideNumber) {
  slides[currentSlide].setAttribute("aria-hidden", "true");
  slides[slideNumber].setAttribute("aria-hidden", "false");
  carouselInner.style.transform = `translateX(-${slideNumber * 100}%)`;
  currentSlide = slideNumber;
}


nextButton.addEventListener("click", showNextSlide);
prevButton.addEventListener("click", showPrevSlide);
