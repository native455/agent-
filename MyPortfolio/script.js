```javascript
/* ────────────────────────────────────────────────────────
   MyPortfolio – Core JavaScript
   (ES6+; no external dependencies)
──────────────────────────────────────────────────────── */

/* ==========================
   CONFIGURATION
   ========================== */
const API_ENDPOINT = '/contact/submit'; // Replace with your endpoint
const THEME_KEY = 'myPortfolioTheme';

/* ==========================
   UTILITIES
   ========================== */
const $ = selector => document.querySelector(selector);
const $$ = selector => Array.from(document.querySelectorAll(selector));
const on = (el, event, handler) =>
  el?.addEventListener(event, handler, { passive: false });

/* ==========================
   THEME TOGGLE
   ========================== */
const initTheme = () => {
  const stored = localStorage.getItem(THEME_KEY);
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)')
    .matches;
  const dark = stored === 'dark' || (!stored && prefersDark);

  if (dark) document.documentElement.classList.add('dark');
  else document.documentElement.classList.remove('dark');

  $('#theme-toggle')?.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark');
    const isDark = document.documentElement.classList.contains('dark');
    localStorage.setItem(THEME_KEY, isDark ? 'dark' : 'light');
  });
};

/* ==========================
   MOBILE NAVIGATION
   ========================== */
const initMobileNav = () => {
  const toggle = $('#nav-toggle');
  const menu = $('#nav-menu');

  on(toggle, 'click', () => menu.classList.toggle('open'));
  on(document, 'click', e => {
    if (!menu.contains(e.target) && !toggle.contains(e.target)) {
      menu.classList.remove('open');
    }
  });
};

/* ==========================
   SMOOTH SCROLL
   ========================== */
const initSmoothScroll = () => {
  const links = $$('a[href^="#"]');

  links.forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const target = $(link.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
        // Close mobile menu after navigation if open
        const menu = $('#nav-menu');
        if (menu.classList.contains('open')) menu.classList.remove('open');
      }
    });
  });
};

/* ==========================
   REVEAL ON SCROLL
   ========================== */
const initReveals = () => {
  const elements = $$('[data-reveal]');
  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    },
    {
      rootMargin: '0px 0px -50% 0px',
      threshold: 0,
    }
  );

  elements.forEach(el => observer.observe(el));
};

/* ==========================
   PORTFOLIO FILTERING
   ========================== */
const initFilters = () => {
  const buttons = $$('[data-filter]');
  const items = $$('[data-category]');

  const filter = category => {
    items.forEach(item => {
      const cat = item.getAttribute('data-category');
      if (!category || cat.includes(category)) {
        item.classList.remove('hidden');
      } else {
        item.classList.add('hidden');
      }
    });
  };

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.getAttribute('data-filter');
      filter(cat);
    });
  });

  // Default to showing all
  filter();
};

/* ==========================
   CONTACT FORM
   ========================== */
const initContactForm = () => {
  const form = $('#contact-form');
  if (!form) return;

  on(form, 'submit', async e => {
    e.preventDefault();
    const status = $('#contact-status');

    const formData = new FormData(form);
    try {
      status.textContent = 'Sending...';
      status.className = 'status pending';

      const res = await fetch(API_ENDPOINT, {
        method: 'POST',
        body: formData,
      });

      if (!res.ok) throw new Error('Network response was not ok');
      const data = await res.json();

      status.textContent =
        data.message || 'Thank you! Your message has been sent.';
      status.className = 'status success';
      form.reset();
    } catch (err) {
      console.error(err);
      status.textContent = 'Could not send message. Please try again later.';
      status.className = 'status error';
    }
  });
};

/* ==========================
   INITIALIZE APP
   ========================== */
const initApp = () => {
  initTheme();
  initMobileNav();
  initSmoothScroll();
  initReveals();
  initFilters();
  initContactForm();
};

document.addEventListener('DOMContentLoaded', initApp);
```