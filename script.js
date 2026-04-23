/* ============================================================
   MANHAJ AL AMBIYA — MAIN SCRIPT
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initMobileMenu();
  initScrollAnimations();
  initCounters();
  initLightbox();
});

/* --- Navbar Scroll Behavior --- */
function initNavbar() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;

  const onScroll = () => {
    if (window.scrollY > 80) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* --- Mobile Menu --- */
function initMobileMenu() {
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  const overlay = document.getElementById('mobileOverlay');

  if (!hamburger || !mobileMenu) return;

  hamburger.addEventListener('click', () => {
    const isOpen = mobileMenu.classList.contains('open');
    if (isOpen) {
      closeMobileMenu();
    } else {
      mobileMenu.classList.add('open');
      overlay.classList.add('open');
      hamburger.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  });

  if (overlay) {
    overlay.addEventListener('click', () => {
      closeMobileMenu();
    });
  }

  // Close on link click
  const mobileLinks = mobileMenu.querySelectorAll('a:not([onclick])');
  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      closeMobileMenu();
    });
  });
}

function closeMobileMenu() {
  const mobileMenu = document.getElementById('mobileMenu');
  const overlay = document.getElementById('mobileOverlay');
  const hamburger = document.getElementById('hamburger');

  if (mobileMenu) mobileMenu.classList.remove('open');
  if (overlay) overlay.classList.remove('open');
  if (hamburger) hamburger.classList.remove('open');
  document.body.style.overflow = '';
}

function toggleMobileAccordion(event, id) {
  event.preventDefault();
  const accordion = document.getElementById(id);
  if (accordion) {
    accordion.classList.toggle('open');
  }
}

/* --- Scroll Animations (IntersectionObserver) --- */
function initScrollAnimations() {
  const elements = document.querySelectorAll('.fade-up, .fade-in, .stagger');

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.15,
      rootMargin: '0px 0px -40px 0px'
    });

    elements.forEach(el => observer.observe(el));
  } else {
    // Fallback: show all
    elements.forEach(el => el.classList.add('visible'));
  }
}

/* --- Counter Animation --- */
function initCounters() {
  const counters = document.querySelectorAll('.impact__number[data-count]');
  if (counters.length === 0) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => observer.observe(counter));
}

function animateCounter(el) {
  const target = parseInt(el.dataset.count, 10);
  const duration = 2000;
  const startTime = performance.now();
  const suffix = '+';

  function easeOutQuart(t) {
    return 1 - Math.pow(1 - t, 4);
  }

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const easedProgress = easeOutQuart(progress);
    const current = Math.floor(easedProgress * target);

    if (target >= 1000) {
      el.textContent = current.toLocaleString() + suffix;
    } else {
      el.textContent = current + suffix;
    }

    if (progress < 1) {
      requestAnimationFrame(update);
    } else {
      if (target >= 1000) {
        el.textContent = target.toLocaleString() + suffix;
      } else {
        el.textContent = target + suffix;
      }
    }
  }

  requestAnimationFrame(update);
}

/* --- Lightbox --- */
const galleryCaptions = [
  'Arabic Academy — Students in class',
  'Quran Hifz Circle — Weekly session',
  'Ration Distribution Drive — Mangaluru',
  'Teen Series — Saturday Program for Girls',
  'Eid Kiswa Distribution — Families receiving clothing',
  'Da\'wah Workshop — Community lecture'
];

function openLightbox(index) {
  const lightbox = document.getElementById('lightbox');
  const caption = document.getElementById('lightboxCaption');

  if (lightbox) {
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  if (caption && galleryCaptions[index]) {
    caption.textContent = galleryCaptions[index];
  }
}

function closeLightbox() {
  const lightbox = document.getElementById('lightbox');
  if (lightbox) {
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
  }
}

// Close lightbox on Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeLightbox();
    closeMobileMenu();
  }
});

// Close lightbox on background click
document.addEventListener('click', (e) => {
  const lightbox = document.getElementById('lightbox');
  if (e.target === lightbox) {
    closeLightbox();
  }
});

/* --- Bank Transfer Accordion --- */
function toggleBankAccordion() {
  const toggle = document.getElementById('bankToggle');
  const content = document.getElementById('bankContent');

  if (toggle && content) {
    toggle.classList.toggle('open');
    content.classList.toggle('open');
  }
}

/* --- Smooth Scroll for Anchor Links --- */
document.addEventListener('click', (e) => {
  const link = e.target.closest('a[href^="#"]');
  if (!link) return;

  const targetId = link.getAttribute('href').slice(1);
  if (!targetId) return;

  const target = document.getElementById(targetId);
  if (target) {
    e.preventDefault();
    const navHeight = 80;
    const targetPos = target.getBoundingClientRect().top + window.scrollY - navHeight;

    window.scrollTo({
      top: targetPos,
      behavior: 'smooth'
    });

    closeMobileMenu();
  }
});

/* --- Contact Form Validation --- */
function validateContactForm(event) {
  event.preventDefault();

  const form = event.target;
  const name = form.querySelector('#fullName');
  const email = form.querySelector('#email');
  const message = form.querySelector('#message');
  let isValid = true;

  // Clear previous errors
  form.querySelectorAll('.form-error').forEach(el => el.remove());

  // Validate name
  if (!name.value.trim()) {
    showError(name, 'Full name is required');
    isValid = false;
  }

  // Validate email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!email.value.trim() || !emailRegex.test(email.value)) {
    showError(email, 'Please enter a valid email address');
    isValid = false;
  }

  // Validate message
  if (!message.value.trim() || message.value.trim().length < 20) {
    showError(message, 'Message must be at least 20 characters');
    isValid = false;
  }

  if (isValid) {
    // Show success
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.textContent;
    btn.textContent = 'Message Sent!';
    btn.style.background = '#059669';
    btn.style.borderColor = '#059669';
    setTimeout(() => {
      btn.textContent = originalText;
      btn.style.background = '';
      btn.style.borderColor = '';
      form.reset();
    }, 3000);
  }
}

function showError(input, msg) {
  const error = document.createElement('div');
  error.className = 'form-error';
  error.style.cssText = 'color: #DC2626; font-size: 0.82rem; margin-top: 6px;';
  error.textContent = msg;
  input.parentNode.appendChild(error);
  input.style.borderColor = '#DC2626';
  input.addEventListener('input', () => {
    input.style.borderColor = '';
    const err = input.parentNode.querySelector('.form-error');
    if (err) err.remove();
  }, { once: true });
}

/* --- Anchor Nav Active State --- */
function initAnchorNav() {
  const anchors = document.querySelectorAll('.anchor-nav__link');
  if (anchors.length === 0) return;

  const sections = [];
  anchors.forEach(a => {
    const id = a.getAttribute('href')?.replace('#', '');
    const section = id ? document.getElementById(id) : null;
    if (section) sections.push({ el: section, link: a });
  });

  if (sections.length === 0) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        anchors.forEach(a => a.classList.remove('active'));
        const match = sections.find(s => s.el === entry.target);
        if (match) match.link.classList.add('active');
      }
    });
  }, { threshold: 0.3, rootMargin: '-100px 0px -60% 0px' });

  sections.forEach(s => observer.observe(s.el));
}

// Initialize anchor nav on pages that have it
if (document.querySelector('.anchor-nav')) {
  document.addEventListener('DOMContentLoaded', initAnchorNav);
}
