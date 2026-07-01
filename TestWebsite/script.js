```js
// TestWebsite JavaScript

(() => {
  /* ---------- Utility ------------------------------------------------- */
  const $ = selector => document.querySelector(selector);
  const $$ = selector => Array.from(document.querySelectorAll(selector));

  /* ---------- Dark Mode ------------------------------------------------- */
  const toggleDarkMode = () => {
    const html = document.documentElement;
    const isDark = html.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', isDark);
  };

  const initDarkMode = () => {
    const isDark = localStorage.getItem('darkMode') === 'true';
    if (isDark) document.documentElement.classList.add('dark-mode');
    const btn = $('#dark-mode-toggle');
    if (btn) btn.addEventListener('click', toggleDarkMode);
  };

  /* ---------- Mobile Navigation ---------------------------------------- */
  const initNavToggle = () => {
    const btn = $('#nav-toggle');
    const menu = $('#nav-menu');

    if (!btn || !menu) return;

    btn.addEventListener('click', () => {
      menu.classList.toggle('open');
      btn.setAttribute('aria-expanded', menu.classList.contains('open'));
    });

    // Close menu when a link is clicked
    $$(`#${menu.id} a`).forEach(link => {
      link.addEventListener('click', () => {
        menu.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      });
    });
  };

  /* ---------- Form Handling -------------------------------------------- */
  const initContactForm = () => {
    const form = $('#contact-form');
    if (!form) return;

    form.addEventListener('submit', e => {
      e.preventDefault();
      const data = new FormData(form);
      const msg = {
        name: data.get('name'),
        email: data.get('email'),
        message: data.get('message'),
        timestamp: new Date().toISOString()
      };
      // Simple storage in localStorage (replace with API call in production)
      let msgs = JSON.parse(localStorage.getItem('contactMsgs') || '[]');
      msgs.push(msg);
      localStorage.setItem('contactMsgs', JSON.stringify(msgs));

      // Reset form and show feedback
      form.reset();
      $('#form-feedback').textContent = 'Thank you for your message!';
      setTimeout(() => { $('#form-feedback').textContent = ''; }, 5000);
    });
  };

  /* ---------- Demo API Fetch ------------------------------------------ */
  const initDemoAPI = () => {
    const container = $('#demo-data');
    if (!container) return;

    fetch('https://jsonplaceholder.typicode.com/posts?_limit=5')
      .then(resp => resp.json())
      .then(posts => {
        container.innerHTML = posts
          .map(
            post => `<article class="post">
          <h3>${post.title}</h3>
          <p>${post.body}</p>
        </article>`
          )
          .join('');
      })
      .catch(err => {
        container.textContent = 'Failed to load demo data.';
        console.error(err);
      });
  };

  /* ---------- Initialize All ------------------------------------------- */
  const init = () => {
    document.addEventListener('DOMContentLoaded', () => {
      initDarkMode();
      initNavToggle();
      initContactForm();
      initDemoAPI();
    });
  };

  init();
})();
```