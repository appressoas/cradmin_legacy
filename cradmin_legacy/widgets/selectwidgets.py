from django.forms import widgets


class WrappedSelect(widgets.Select):
    def __init__(self, *args, **kwargs):
        self.wrapper_css_class = kwargs.pop("wrapper_css_class", "")
        super(WrappedSelect, self).__init__(*args, **kwargs)

    def render(self, *args, **kwargs):
        rendered_widget = super(WrappedSelect, self).render(*args, **kwargs)
        return '<div class="{}">{}</div>'.format(self.wrapper_css_class, "".join(rendered_widget))
