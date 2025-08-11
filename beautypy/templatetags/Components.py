from django import template
from django.utils.html import format_html
from django.template import Node, TemplateSyntaxError
from django.template.base import token_kwargs
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def LoadBeautypyJS():
    js_link = static("node_modules/bootstrap/dist/js/bootstrap.min.js")
    if js_link:
        return format_html('<script src="{}" defer></script>', js_link)
    else:
        return format_html('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js" integrity="sha384-ndDqU0Gzau9qJ1lfW4pNLlhNTkCfHzAVBReH9diLvGRem5+R9g2FzA8ZGN954O5Q" crossorigin="anonymous"></script>')

@register.simple_tag
def LoadBeautypyCSS():
    css_link = static("node_modules/bootstrap/dist/css/bootstrap.min.css")
    if css_link:
        return format_html('<link href="{}" rel="stylesheet">', css_link)
    else:
        return format_html(
            '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr" crossorigin="anonymous">'
        )

@register.simple_tag
def Button(label, type="button", variant="primary", css_class="", tag_id=None):
    variant_class = f"btn btn-{variant}" if variant else "btn btn-primary"
    classes = f"{variant_class} {css_class}".strip()
    return format_html(
        '<button type="{}" class="{}" id="{}">{}</button>',
        type,
        classes,
        tag_id or '',
        label,
    )

@register.simple_tag
def Link(url, label, css_class="btn btn-link", tag_id=None):
    return format_html(
        '<a href="{}" class="{}" id="{}">{}</a>',
        url,
        css_class,
        tag_id or '',
        label,
    )

@register.simple_tag
def Alert(message, alert_type="info", css_class="alert", tag_id=None):
    color_classes = {
        "info": "alert alert-info",
        "success": "alert alert-success",
        "warning": "alert alert-warning",
        "error": "alert alert-danger",
    }
    default_classes = color_classes.get(alert_type, "alert alert-info")
    classes = f"{default_classes} {css_class}".strip()
    return format_html(
        '<div class="{} d-flex justify-content-between align-items-center" role="alert" id="{}">'
        '<span>{}</span>'
        '<button type="button" class="btn-close ms-2" data-bs-dismiss="alert" aria-label="Close"></button>'
        '</div>',
        classes,
        tag_id or '',
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
        tag_id or '',
    )

@register.simple_tag
def InputLabel(name, label_text, css_class="form-label", tag_id="label"):
    return format_html(
        '<label for="{}" class="{}" id="{}">{}</label>', name, css_class, tag_id, label_text
    )

@register.simple_tag
def FormGroup(label, input_field):
    return format_html(
        '<div class="mb-3">{} {}</div>',
        InputLabel(label, label),
        input_field,
    )

@register.simple_tag
def Toast(message, toast_type="info", tag_id=None):
    color_classes = {
        "info": "bg-info text-white",
        "success": "bg-success text-white",
        "warning": "bg-warning text-dark",
        "error": "bg-danger text-white",
    }
    bg_color = color_classes.get(toast_type, "bg-secondary text-white")
    return format_html(
        '<div class="toast align-items-center {} border-0 show" role="alert" aria-live="assertive" aria-atomic="true" id="{}">'
        '<div class="d-flex">'
        '<div class="toast-body">{}</div>'
        '<button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>'
        '</div>'
        '</div>',
        bg_color,
        tag_id or '',
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
                '<section class="{} mb-4" id="{}">{}<div>{}</div></section>',
                f"{css_class} container-fluid".strip(),
                tag_id,
                f'<h2 class="h5 mb-3">{title}</h2>' if title else '',
                content,
            )
        elif self.tag_name == "Container":
            return format_html(
                '<div class="{}" id="{}">{}</div>',
                f"{css_class} container".strip(),
                tag_id,
                content,
            )
        elif self.tag_name == "Footer":
            return format_html(
                '<footer class="{} mt-5 py-3 bg-light text-center" id="{}">{}</footer>',
                css_class,
                tag_id,
                content,
            )
        elif self.tag_name == "Navbar":
            return format_html(
                '<nav class="{} navbar navbar-expand-lg" id="{}">{}</nav>',
                css_class,
                tag_id,
                content,
            )
        elif self.tag_name == "Tooltip":
            return format_html(
                '<span class="{}" data-bs-toggle="tooltip" title="{}">{}</span>',
                css_class,
                title,
                content,
            )
        elif self.tag_name == "Accordion":
            return format_html(
                '<div class="accordion {}" id="{}">'
                '<div class="accordion-item">'
                '<h2 class="accordion-header">'
                '<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-{}" aria-expanded="true" aria-controls="collapse-{}">{}</button>'
                '</h2>'
                '<div id="collapse-{}" class="accordion-collapse collapse show" aria-labelledby="heading-{}" data-bs-parent="#{}">'
                '<div class="accordion-body">{}</div>'
                '</div>'
                '</div>'
                '</div>',
                css_class,
                tag_id,
                tag_id,
                tag_id,
                title,
                tag_id,
                tag_id,
                tag_id,
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
