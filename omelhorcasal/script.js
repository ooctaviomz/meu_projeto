document.addEventListener('DOMContentLoaded', function () {
  // Smooth scroll for internal anchors
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var href = this.getAttribute('href');
      if (!href || href === '#') return;
      var id = href.slice(1);
      var target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        try { history.replaceState(null, '', '#' + id); } catch (err) {}
      }
    });
  });

  // Add simple visual feedback when clicking portfolio links
  document.querySelectorAll('.portifolio-link').forEach(function (el) {
    el.addEventListener('click', function (e) {
      // if the link points to '#', just give a brief pulse
      if (el.getAttribute('href') === '#') {
        e.preventDefault();
        el.classList.add('pulse');
        setTimeout(function () { el.classList.remove('pulse'); }, 400);
      }
    });
  });
});
