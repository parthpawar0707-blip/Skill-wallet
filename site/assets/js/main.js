document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('active');
      mobileToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close mobile nav when clicking any link
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
          navLinks.classList.remove('active');
          mobileToggle.setAttribute('aria-expanded', 'false');
        }
      });
    });

    // Close mobile nav with Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && navLinks.classList.contains('active')) {
        navLinks.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', 'false');
        mobileToggle.focus();
      }
    });
  }

  // Smooth scroll for nav anchor links
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
        }
      }
    });
  });

  // Tableau Iframe Fallback & Reload Logic
  const reloadBtn = document.getElementById('reload-tableau');
  const tableauFrame = document.getElementById('tableau-frame');
  const tableauFallback = document.getElementById('tableau-fallback');
  const tableauWrapper = document.getElementById('tableau-wrapper');

  let iframeLoaded = false;

  if (tableauFrame) {
    tableauFrame.addEventListener('load', () => {
      iframeLoaded = true;
      if (tableauFallback && tableauWrapper) {
        tableauFallback.classList.remove('is-visible');
        tableauWrapper.classList.remove('has-fallback');
      }
    });

    // Fallback trigger if iframe load is blocked or takes too long
    setTimeout(() => {
      if (!iframeLoaded && tableauFallback && tableauWrapper) {
        // If still not loaded after 7 seconds, display the fallback card
        tableauFallback.classList.add('is-visible');
        tableauWrapper.classList.add('has-fallback');
      }
    }, 7000);
  }

  if (reloadBtn && tableauFrame) {
    reloadBtn.addEventListener('click', () => {
      const currentSrc = tableauFrame.src;
      tableauFrame.src = '';
      if (tableauFallback && tableauWrapper) {
        tableauFallback.classList.remove('is-visible');
        tableauWrapper.classList.remove('has-fallback');
      }
      setTimeout(() => {
        tableauFrame.src = currentSrc;
      }, 250);
    });
  }

  // Video Chapter Quick-Jump Navigation
  const videoPlayer = document.querySelector('.video-player');
  const chapterPills = document.querySelectorAll('.chapter-pill');
  if (videoPlayer && chapterPills.length > 0) {
    chapterPills.forEach(pill => {
      pill.addEventListener('click', () => {
        const targetSeconds = parseFloat(pill.getAttribute('data-time'));
        if (!isNaN(targetSeconds)) {
          videoPlayer.currentTime = targetSeconds;
          videoPlayer.play().catch(() => {});
        }
      });
    });
  }

  // Load summary statistics log
  fetch('assets/data/summary.json')
    .then(res => res.json())
    .then(data => {
      if (data && data.dataset_metadata) {
        console.log('Verified Student Mental Health Analytics loaded:', data.dataset_metadata);
      }
    })
    .catch(() => {
      console.log('Local summary data fallback active.');
    });
});

