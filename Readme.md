# 🌸 Beautypy

**Beautypy** is a Django UI component library that provides pre-designed, reusable template tags for building modern, responsive UIs with Bootstrap 5. Create beautiful interfaces in minutes—no HTML or CSS required!

For more informatoin visit our official website [Beautypy](https://beautypy.pythonanywhere.com/)

---

## ✨ Features

- ✅ Clean, responsive, accessible Bootstrap 5 components
- ⚡ Lightning-fast integration with Django templates
- 💡 Simple custom template tags: `{% Button %}`, `{% Alert %}`, `{% Navbar %}`, `{% Tooltip %}`, and more
- ☕ Support development via [Buy Me a Coffee](https://www.buymeacoffee.com/avichaurasiya)

---

## 📦 Installation

```bash
pip install beautypy  # (Test version: see below)
```

**Currently under testing phase. Install the test version with:**

```bash
pip install -i https://test.pypi.org/simple/ beautypy
```

---

## 🎨 Bootstrap 5 Integration

Beautypy uses Bootstrap 5 for styling. You can include Bootstrap in your project via following this setup:

## ⚙️ Django Setup

1. **Add to INSTALLED_APPS**

```python
INSTALLED_APPS = [
    ...
    'beautypy',
]
```

2. **Templates Context Processor**
Make sure your TEMPLATES setting includes:

```python
'OPTIONS': {
    'context_processors': [
        ...
        'django.template.context_processors.request',
    ],
}
```

3. **Load Beautypy Tags**
In your templates top of your html page:

```django
{% load Components %}
```

4. **Load Bootstrap CSS/JS (if not already loaded globally)**

```django
{% LoadBeautypyCSS %}   {# Loads Bootstrap CSS #}
{% LoadBeautypyJS %}    {# Loads Bootstrap JS #}
```

---

# 🧩 Components & Template Tags

## 1. `{% LoadBeautypyCSS %}`

Loads Bootstrap CSS. Uses local static if available, otherwise falls back to CDN.

**Usage:**

```django
{% LoadBeautypyCSS %}
```

---

## 2. `{% LoadBeautypyJS %}`

Loads Bootstrap JS. Uses local static if available, otherwise falls back to CDN.

**Usage:**

```django
{% LoadBeautypyJS %}
```

---

## 3. `{% Button %}`

Renders a Bootstrap-styled button.

**Props:**

- `label` (required): Button text
- `type`: Button type (`button`, `submit`, etc.)
- `variant`: Bootstrap color variant (`primary`, `secondary`, `success`, `danger`, `warning`, `info`)
- `css_class`: Additional classes
- `tag_id`: Optional id

**Usage:**

```django
{% Button label="Submit" type="submit" variant="primary" %}
```

---

## 4. `{% Link %}`

Renders a Bootstrap-styled link (anchor).

**Props:**

- `url` (required): Href
- `label` (required): Link text
- `css_class`: Additional classes (default: `btn btn-link`)
- `tag_id`: Optional id

**Usage:**

```django
{% Link url="/home" label="Home" css_class="btn btn-primary" %}
```

---

## 5. `{% Alert %}`

Renders a Bootstrap-styled alert box.

**Props:**

- `message` (required): Alert text
- `alert_type`: `info`, `success`, `warning`, `error`
- `css_class`: Additional classes (default: `alert`)
- `tag_id`: Optional id

**Usage:**

```django
{% Alert message="Success!" alert_type="success" %}
```

---

## 6. `{% InputField %}`

Renders a Bootstrap input field.

**Props:**

- `name` (required)
- `value`: Default value
- `input_type`: Input type (default: `text`)
- `css_class`: Additional classes (default: `form-control`)
- `tag_id`: Optional id

**Usage:**

```django
{% InputField name="email" input_type="email" css_class="form-control" %}
```

---

## 7. `{% InputLabel %}`

Renders a Bootstrap label for an input.

**Props:**

- `name` (required): For attribute
- `label_text` (required): Label text
- `css_class`: Additional classes (default: `form-label`)
- `tag_id`: Optional id (default: `label`)

**Usage:**

```django
{% InputLabel name="email" label_text="Your Email" %}
```

---

## 8. `{% FormGroup %}`

Groups a label and input together in a Bootstrap form group.

**Props:**

- `label` (required): Label text
- `input_field` (required): Input field (rendered separately)

**Usage:**

```django
{% FormGroup label="email" input_field=input_field %}
```

---

## 9. `{% Toast %}`

Renders a Bootstrap-styled toast notification.

**Props:**

- `message` (required)
- `toast_type`: `info`, `success`, `warning`, `error`
- `tag_id`: Optional id

**Usage:**

```django
{% Toast message="Operation successful!" toast_type="success" %}
```

---

## 10. Block Tags

These tags wrap content in Bootstrap containers/sections/footers/navbars, etc.

### Section

```django
{% Section title="Section Title" css_class="mb-4" tag_id="section1" %}
  <!-- Content -->
{% endSection %}
```

### Container

```django
{% Container css_class="container my-4" tag_id="main-container" %}
  <!-- Content -->
{% endContainer %}
```

### Footer

```django
{% Footer css_class="text-center text-muted py-3" tag_id="footer" %}
  &copy; 2025 Beautypy
{% endFooter %}
```

### Navbar

<img src="/beautypy/static/images/nav.png">

```django
{% Navbar css_class="navbar navbar-expand-lg navbar-dark bg-primary p-4" tag_id="main-navbar" %}
  <!-- Logo / Nav links / Buttons -->
{% endNav %}
```

### Tooltip

```django
{% Tooltip title="Helpful info!" css_class="d-inline-block" %}
  <button class="btn btn-secondary">Hover me</button>
{% endTooltip %}
```

### Accordion

```django
{% Accordion title="Click to Expand" css_class="accordion" tag_id="accordion1" %}
  <p>This content is toggled.</p>
{% endAccordion %}
```

---

# 📷 Example Template

```django
{% load Components %}
<!DOCTYPE html>
<html>
  <head>
    <title>Beautypy Example</title>
    {% LoadBeautypyCSS %}
  </head>
  <body>
    {% Navbar css_class="navbar navbar-expand-lg navbar-dark bg-primary p-4" %}
      <!-- Content -->
    {% endNav %}

    {% Section title="Alerts" %}
      {% Alert message="Success!" alert_type="success" %}
    {% endSection %}

    {% Footer css_class="text-center text-muted py-3" %}
      &copy; 2025 Beautypy
    {% endFooter %}

    {% LoadBeautypyJS %}
  </body>
</html>
```

---

# 🤝 Contributing

1. Fork this repository
2. Create your feature branch:

```bash
git checkout -b feature/my-component
```

3. Commit your changes:

```bash
git commit -m 'Add my new component'
```

4. Push to the branch:

```bash
git push origin feature/my-component
```

5. Open a pull request

---

# 💖 Support

Beautypy is open-source. If you like the project, consider supporting it via [Buy Me a Coffee](https://coff.ee/webdevavi96).

# 🔗 License

MIT License © 2025 [webdevavi96 | Avinash](https://github.com/webdevavi96)
