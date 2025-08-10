from django import template
from django.utils.html import format_html
from django.template import Node, TemplateSyntaxError
from django.template.base import token_kwargs
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def LoadBeautypyJS():
    js_link = static("Bundles/JSBundles/beautypy.js")
    return format_html('<script src="{}" defer></script>', js_link)


@register.simple_tag
def LoadBeautypyCSS(url=None):
    css_link = static(url)

    if css_link == None:
        cdn = "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"
        return format_html('<script src="{}"></script>', cdn)
    else:
        return format_html('<link href="{}" rel="stylesheet">', css_link)


@register.simple_tag
def Button(label, type="button", variant="primary", css_class="", tag_id=None):
    color_classes = {
        "primary": "bg-blue-600 text-white",
        "secondary": "bg-gray-600 text-white",
        "success": "bg-green-600 text-white",
        "danger": "bg-red-600 text-white",
        "warning": "bg-yellow-600 text-white",
        "info": "bg-blue-400 text-white",
    }
    variant_class = color_classes.get(variant, "")
    classes = f"{variant_class} {css_class}".strip()

    return format_html(
        '<button type="{}" class="{} py-2 px-4 rounded-md hover:bg-opacity-80 transition duration-300" id="{}">{}</button>',
        type,
        classes,
        tag_id,
        label,
    )


@register.simple_tag
def Link(url, label, css_class="btn btn-link", tag_id=None):
    return format_html(
        '<a href="{}" class="{} rounded-md hover:bg-opacity-80 transition dureation-300" id="{}">{}</a>',
        url,
        css_class,
        tag_id,
        label,
    )


@register.simple_tag
def Alert(message, alert_type="info", css_class="alert", tag_id=None):
    color_classes = {
        "info": "bg-blue-100 border border-blue-400 text-blue-700",
        "success": "bg-green-100 border border-green-400 text-green-700",
        "warning": "bg-yellow-100 border border-yellow-400 text-yellow-700",
        "error": "bg-red-100 border border-red-400 text-red-700",
    }
    default_classes = color_classes.get(alert_type, "")
    classes = f"{css_class} {default_classes}".strip()
    return format_html(
        """
        <div class="{} px-4 py-3 rounded relative flex justify-between" role="alert" id="{}">
          <span class="block sm:inline">{}</span>
          <button id=closeBtn>Close</button>
        </div>
        """,
        classes,
        tag_id,
        message,
    )


@register.simple_tag
def InputField(
    name, value="", input_type="text", css_class="form-control", tag_id=None
):
    return format_html(
        '<input type="{}" name="{}" value="{}" class="{}" id="{}">',
        input_type,
        name,
        value,
        css_class,
        tag_id,
    )


@register.simple_tag
def InputLabel(name, label_text, css_class="form-label", tag_id="label"):
    return format_html(
        '<label for="{}" class="{}" id="{}">{}</label>', name, css_class, label_text
    )


@register.simple_tag
def FormGroup(label, input_field):
    return format_html(
        '<div class="form-group">{} {}</div>',
        InputLabel(label, label),
        input_field,
    )


@register.simple_tag
def Toast(message, toast_type="info", tag_id=None):
    colors = {
        "info": "bg-blue-500",
        "success": "bg-green-500",
        "warning": "bg-yellow-500",
        "error": "bg-red-500",
    }
    bg_color = colors.get(toast_type, "bg-gray-500")
    return format_html(
        '<div class="{} text-white px-4 py-2 rounded shadow-md flex justify-between" id="{}"> <span>{}</span> <button id=closeBtn>Close</button></div>',
        bg_color,
        tag_id,
        message,
    )


class BlockNode(Node):
    def __init__(self, nodelist, tag_name, css_class=None, title=None, tag_id=None):
        self.nodelist = nodelist
        self.tag_name = tag_name
        self.css_class = css_class
        self.title = title
        self.tag_id = tag_id

    def render(self, context):
        content = self.nodelist.render(context)
        css_class = self.css_class.resolve(context) if self.css_class else ""
        title = self.title.resolve(context) if self.title else ""
        tag_id = self.tag_id.resolve(context) if self.tag_id else ""

        if self.tag_name == "Section":
            return format_html(
                '<section class="{}" id="{}"><h2 class="text-lg font-semibold mb-2">{}</h2>{}</section>',
                css_class,
                tag_id,
                title,
                content,
            )
        elif self.tag_name == "Container":
            return format_html(
                '<div class="{}" id="{}">{}</div>',
                css_class,
                tag_id,
                content,
            )
        elif self.tag_name == "Footer":
            return format_html(
                '<footer class="{}" id="{}">{}</footer>',
                css_class,
                tag_id,
                content,
            )
        elif self.tag_name == "Navbar":
            return format_html(
                '<nav class="{}" id="{}">{}</nav>',
                css_class,
                tag_id,
                content,
            )
        elif self.tag_name == "Tooltip":
            return format_html(
                '<div class="relative group inline-block cursor-pointer {}">{}<div class="absolute hidden group-hover:block bg-black text-white text-xs rounded py-1 px-2 mt-1">{}</div></div>',
                css_class,
                content,
                title,
            )
        elif self.tag_name == "Accordion":
            return format_html(
                '<div class="{} border rounded-md overflow-hidden" id="{}"><button class="w-full px-4 py-2 text-left bg-gray-100 hover:bg-gray-200" id="accordion-btn">{}</button><div class="p-4">{}</div></div>',
                css_class,
                tag_id,
                title,
                content,
            )
        return content


def block_tag(tag_name, end_tag_name):
    def tag_func(parser, token):
        bits = token.split_contents()
        args = bits[1:]

        kwargs = token_kwargs(args, parser)

        css_class = kwargs.get("css_class", None)
        tag_id = kwargs.get("tag_id", None)
        title = kwargs.get("title", None)

        nodelist = parser.parse((end_tag_name,))
        parser.delete_first_token()
        return BlockNode(nodelist, tag_name, css_class, title, tag_id)

    return tag_func


register.tag("Section", block_tag("Section", "endSection"))
register.tag("Container", block_tag("Container", "endContainer"))
register.tag("Footer", block_tag("Footer", "endFooter"))
register.tag("Navbar", block_tag("Navbar", "endNav"))
register.tag("Tooltip", block_tag("Tooltip", "endTooltip"))
register.tag("Accordion", block_tag("Accordion", "endAccordion"))
