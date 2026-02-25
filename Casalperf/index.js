const photos = [
    "img/gramado.jpg",                // Foto inicial
    "img/ollhar.jpg",                  // Exemplo 2
    "img/zoada.jpg",      // Exemplo 3
    "img/masc.jpg",         // Exemplo 4
    "img/gramadoo.jpg"           // Exemplo5
  ];
  
  let currentIndex = 0;
  
  function nextPhoto() {
    currentIndex = (currentIndex + 1) % photos.length;
    const img = document.getElementById("photo");
    img.style.opacity = 0;
  
    setTimeout(() => {
      img.src = photos[currentIndex];
      img.style.opacity = 1;
    }, 300);
  }
  