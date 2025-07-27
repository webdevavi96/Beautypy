# 🌸 Beautypy

**Beautypy** is a Django UI component library that simplifies your front-end development by offering pre-designed, reusable template tags like `{% Button %}`, `{% Alert %}`, `{% ContactForm %}`, and more.

With just a few template tags, you can create modern, accessible, and responsive UIs in minutes — without writing a single line of HTML or CSS!

---

## ✨ Features

- ✅ Clean, responsive, accessible components
- 🎨 TailwindCSS-inspired styling
- ⚡ Lightning-fast integration with Django templates
- 💡 Simple custom template tags: `{% Button %}`, `{% Alert %}`, `{% Navbar %}`, etc.
- ☕ Support development via [Buy Me a Coffee](https://www.buymeacoffee.com/avichaurasiya)

---

## 📦 Installation

```bash
 pip install beautypy        #This command will not work beacuse the library is under testing phase. You will find the test version    download command bellow -->
```

**Currently this library is under testing phase so the test versoin download command is**:

```bash
pip install -i https://test.pypi.org/simple/ beautypy
```

## This library needs tailwind for styling, Install by this command

```bash
npm install -D tailwindcss@3.3.5 postcss autoprefixer
npx tailwindcss init
```

### Then configure tailwind.config.js and include the output CSS in your HTML or templates

**tailwind.config.js**:

```bash
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "beautypy/templates/**/*.html",
    "./beautypy/**/*.html",
    "./templatetags/**/*.py",
    "./templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};

```

**postcss.config.js**

```bash
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}

```

**style.css**

```bash
@tailwind base;
@tailwind components;
@tailwind utilities;

```

**Use the Tailwind CLI to compile your CSS**:

```bash
npx tailwindcss -i ./static/css/style.css -o ./static/css/output.css --watch

```

Then add "beautypy" to your INSTALLED_APPS in settings.py:

```bash
    INSTALLED_APPS = [
        ...
        'beautypy',
    ]
```

## 🛠 Setup

1.Templates Directory:

Make sure your project’s TEMPLATES setting includes django.template.context_processors.request:

```bash
'OPTIONS': {
    'context_processors': [
        ...
        'django.template.context_processors.request',
    ],
}
```

Load the Beautypy tags:

In your templates, start by loading the custom tags:

```bash
{% load Components %}
```

## 🧩 Components

 **🔘Button**:

```bash
{% Button label="Submit" type="submit" variant="primary" %}

```

### Variants

primary, secondary, success, danger, warning, info

### Props

label, type, variant, css_class, tag_id

 **🔗 Link**:
Creates an anchor styled like a button.

```bash
{% Link url="/home" label="Home" css_class="text-blue-600" %}


```

 **🚨 Alert**:

### Types

info, success, warning, error

```bash
{% Alert message="Success!" alert_type="success" %}


```

 **📦 Section**:
Wrap content inside a semantic section block with optional title:

```bash
{% Section title="Buttons Section" %}
  <!-- Content -->
{% endSection %}


```

 **📦 Conatiner**:
Centers content inside a container:

```bash
{% Container css_class="max-w-4xl mx-auto" %}
  <!-- Content -->
{% endContainer %}


```

 **⌨️ InputFeild**:

```bash
{% InputField name="email" input_type="email" css_class="..." %}



```

 **🏷️ InputLabel**:

```bash
{% InputLabel name="email" label_text="Your Email" %}


```

**🔁 FormGroup**:
Groups a label and input together:

```bash
{% FormGroup label="email" input_field=input_field %}

```

**💬 Tooltip**:

```bash
{% Tooltip title="Helpful info!" %}
  <button>Hover me</button>
{% endTooltip %}

```

**📣 Toast**:

```bash
{% Toast message="Operation successful!" toast_type="success" %}

```

**📂 Accordion**:

```bash
{% Accordion title="Click to Expand" %}
  <p>This content is toggled.</p>
{% endAccordion %}

```

**📚 Navbar**:
Build a responsive navbar:

```bash
{% Navbar css_class="bg-blue-600 p-4" %}
  <!-- Logo / Nav links / Buttons -->
{% endNav %}

```

**🦶 Footer**:
Build a responsive navbar:

```bash
{% Footer css_class="text-center text-sm text-gray-500" %}
  &copy; 2025 Beautypy
{% endFooter %}

```

**📷 Example Template**:

```bash
{% load Components %}
<!DOCTYPE html>
<html>
  <head>
    <title>Beautypy Example</title>
    <script src="https://cdn.tailwindcss.com"></script>
    {% LoadBeautypyCSS %}
  </head>
  <body>
    {% Navbar css_class="bg-blue-500 p-4" %}
      <!-- Content -->
    {% endNav %}

    {% Section title="Alerts" %}
      {% Alert message="Success!" alert_type="success" %}
    {% endSection %}

    {% Footer css_class="text-center py-4 text-gray-600" %}
      &copy; 2025 Beautypy
    {% endFooter %}

    {% LoadBeautypyJS %}
  </body>
</html>

```

**🤝 Contributing**:

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

**💖 Support**
Beautypy is open-source. If you like the project, consider supporting it via [Buy Me a Coffee](https://coff.ee/webdevavi96).

**🔗 License**:
MIT License © 2025 [webdevavi96 | Avinash](https://github.com/webdevavi96)
