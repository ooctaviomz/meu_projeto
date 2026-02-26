         let button = document.getElementById("button");

button.addEventListener('mousemove', (e) => {
    x = e.offsetX;
    y = e.offsetY;
    button.style.setProperty('--mouse-x', x + "px");
    button.style.setProperty('--mouse-y', y + "px");
})

document.addEventListener('DOMContentLoaded', function () {
  const sections = document.querySelectorAll('section');

  sections.forEach(section => {
      const title = section.querySelector('h2');
      const content = section.querySelector('p');

      title.addEventListener('click', () => {
          content.classList.toggle('hidden');
          
      });
 
    });
});