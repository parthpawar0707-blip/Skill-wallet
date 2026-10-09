document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      const isVisible = navLinks.style.display === 'flex';
      navLinks.style.display = isVisible ? 'none' : 'flex';
      if (!isVisible) {
        navLinks.style.flexDirection = 'column';
        navLinks.style.position = 'absolute';
        navLinks.style.top = '4.25rem';
        navLinks.style.left = '0';
        navLinks.style.right = '0';
        navLinks.style.background = 'white';
        navLinks.style.padding = '1.5rem';
        navLinks.style.boxShadow = '0 10px 15px -3px rgba(0,0,0,0.1)';
      }
    });
  }

  // Smooth scroll for nav links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId && targetId !== '#') {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          e.preventDefault();
          targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
          if (window.innerWidth <= 768 && navLinks) {
            navLinks.style.display = 'none';
          }
        }
      }
    });
  });

  // Tableau Iframe Fallback & Reload Logic
  const reloadBtn = document.getElementById('reload-tableau');
  const tableauFrame = document.querySelector('.tableau-iframe');
  const tableauFallback = document.getElementById('tableau-fallback');

  if (reloadBtn && tableauFrame) {
    reloadBtn.addEventListener('click', () => {
      const currentSrc = tableauFrame.src;
      tableauFrame.src = '';
      setTimeout(() => {
        tableauFrame.src = currentSrc;
      }, 200);
    });
  }

  // Fetch verified summary.json to populate dynamic components if needed
  fetch('assets/data/summary.json')
    .then(res => res.json())
    .then(data => {
      console.log('Verified Student Mental Health Analytics loaded:', data.dataset_metadata);
    })
    .catch(err => {
      console.log('Static fallback active:', err);
    });
});
