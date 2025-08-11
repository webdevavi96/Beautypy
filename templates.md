# Beautypy Templates

Ready-to-use Django templates built with `beautypy/templatetags/Components.py`. Copy, adjust, and drop into your project.

---

## 1) Starter Base Template (recommended)

```django
{% load Components %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}My Site{% endblock %}</title>
    {% LoadBeautypyCSS %}
  </head>
  <body>
    {% Navbar css_class="navbar navbar-expand-lg navbar-dark bg-primary" tag_id="site-navbar" %}
      <div class="container-fluid">
        <a class="navbar-brand" href="#">MySite</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item">{% Link url="#home" label="Home" css_class="nav-link" %}</li>
            <li class="nav-item">{% Link url="#features" label="Features" css_class="nav-link" %}</li>
            <li class="nav-item">{% Link url="#contact" label="Contact" css_class="nav-link" %}</li>
          </ul>
        </div>
      </div>
    {% endNav %}

    <main class="container py-4">
      {% block content %}{% endblock %}
    </main>

    {% Footer css_class="text-center text-muted py-3" %}
      &copy; {{ now|date:"Y" }} My Company
    {% endFooter %}

    {% LoadBeautypyJS %}
  </body>
</html>
```

---

## 2) Landing Page Sections

```django
{% extends "base.html" %}
{% load Components %}
{% block title %}Landing · My Site{% endblock %}
{% block content %}
  {% Section title="Welcome" css_class="mb-5" tag_id="home" %}
    <p class="lead mb-3">Build UIs faster with Beautypy + Bootstrap 5.</p>
    <div class="d-flex flex-wrap gap-2">
      {% Button label="Get Started" variant="primary" %}
      {% Button label="Learn More" variant="secondary" %}
    </div>
  {% endSection %}

  {% Section title="Features" css_class="mb-5" tag_id="features" %}
    <div class="row g-4">
      <div class="col-md-4">
        {% Container css_class="p-3 border rounded" %}
          <h3 class="h6">Simple</h3>
          <p class="mb-0">Use tags like buttons, alerts, tooltips, and more.</p>
        {% endContainer %}
      </div>
      <div class="col-md-4">
        {% Container css_class="p-3 border rounded" %}
          <h3 class="h6">Bootstrap</h3>
          <p class="mb-0">Clean, responsive, accessible by default.</p>
        {% endContainer %}
      </div>
      <div class="col-md-4">
        {% Container css_class="p-3 border rounded" %}
          <h3 class="h6">Django</h3>
          <p class="mb-0">Drop-in templates for your projects.</p>
        {% endContainer %}
      </div>
    </div>
  {% endSection %}

  {% Section title="Contact" css_class="mb-5" tag_id="contact" %}
    <form method="post" class="row g-3">
      {% csrf_token %}
      <div class="col-md-6">
        {% InputLabel name="name" label_text="Your Name" %}
        {% InputField name="name" input_type="text" css_class="form-control" %}
      </div>
      <div class="col-md-6">
        {% InputLabel name="email" label_text="Email" %}
        {% InputField name="email" input_type="email" css_class="form-control" %}
      </div>
      <div class="col-12 d-flex gap-2">
        {% Button label="Send" type="submit" variant="success" %}
        {% Button label="Reset" type="reset" variant="secondary" %}
      </div>
    </form>
  {% endSection %}
{% endblock %}
```

---

## 3) Authentication: Login Page

```django
{% load Components %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login</title>
    {% LoadBeautypyCSS %}
  </head>
  <body class="bg-light">
    <div class="container py-5">
      <div class="row justify-content-center">
        <div class="col-md-6 col-lg-5">
          {% Section title="Sign In" css_class="mb-4" %}{% endSection %}
          <form method="post" class="card card-body shadow-sm">
            {% csrf_token %}
            <div class="mb-3">
              {% InputLabel name="username" label_text="Username" %}
              {% InputField name="username" input_type="text" css_class="form-control" %}
            </div>
            <div class="mb-3">
              {% InputLabel name="password" label_text="Password" %}
              {% InputField name="password" input_type="password" css_class="form-control" %}
            </div>
            <div class="d-grid">
              {% Button label="Login" type="submit" variant="primary" %}
            </div>
          </form>
        </div>
      </div>
    </div>
    {% LoadBeautypyJS %}
  </body>
</html>
```

---

## 4) Dashboard with Alerts, Toasts, Tooltip, Accordion

```django
{% extends "base.html" %}
{% load Components %}
{% block title %}Dashboard{% endblock %}
{% block content %}
  {% Section title="Status" css_class="mb-4" %}
    <div class="d-grid gap-2">
      {% Alert message="Welcome back!" alert_type="success" %}
      {% Alert message="New updates available." alert_type="info" %}
    </div>
  {% endSection %}

  {% Section title="Quick Actions" css_class="mb-4" %}
    <div class="d-flex flex-wrap gap-2">
      {% Button label="Create" variant="primary" %}
      {% Button label="Export" variant="secondary" %}
    </div>
  {% endSection %}

  {% Section title="Help" css_class="mb-4" %}
    {% Tooltip title="Opens help docs" css_class="d-inline-block" %}
      <span class="text-decoration-underline" role="button">Hover for help</span>
    {% endTooltip %}
  {% endSection %}

  {% Section title="FAQ" css_class="mb-4" %}
    {% Accordion title="How do I reset my password?" tag_id="faq1" %}
      <p class="mb-0">Go to settings → security → reset password.</p>
    {% endAccordion %}
  {% endSection %}

  {% Section title="Notifications" css_class="mb-4" %}
    {% Toast message="Changes saved successfully" toast_type="success" tag_id="successToast" %}
  {% endSection %}

  <script>
    // Enable Bootstrap tooltips
    document.addEventListener('DOMContentLoaded', function() {
      var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
      tooltipTriggerList.map(function (tooltipTriggerEl) { return new bootstrap.Tooltip(tooltipTriggerEl); });

      // Auto-show toast example (3 seconds)
      var toastEl = document.getElementById('successToast');
      if (toastEl) new bootstrap.Toast(toastEl, { delay: 3000 }).show();
    });
  </script>
{% endblock %}
```

---

## 5) Minimal Standalone Page

```django
{% load Components %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Minimal</title>
    {% LoadBeautypyCSS %}
  </head>
  <body>
    {% Navbar css_class="navbar navbar-expand-lg navbar-dark bg-dark" %}
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Brand</a>
      </div>
    {% endNav %}

    {% Section title="Hello" css_class="container my-4" %}
      <p class="mb-3">This is a minimal page using Beautypy.</p>
      {% Button label="Primary" variant="primary" %}
    {% endSection %}

    {% Footer css_class="text-center text-muted py-3" %}
      &copy; 2025
    {% endFooter %}

    {% LoadBeautypyJS %}
  </body>
</html>
```

---

## Notes
- Ensure `beautypy` is in `INSTALLED_APPS` and `{% load Components %}` is at the top of templates using Beautypy tags.
- Use `{% LoadBeautypyCSS %}` and `{% LoadBeautypyJS %}` to include Bootstrap assets (local or CDN fallback).
- Initialize tooltips/toasts with small scripts where needed (examples provided above).
