"""
Display Hooks for pycairo, cairocffi Surfaces and Contexts.
"""
from io import BytesIO
from IPython.core import display


def display_cairo_surface(surface):
    """Displayhook function for Surfaces Images, rendered as PNG."""
    b = BytesIO()

    surface.write_to_png(b)
    b.seek(0)
    data = b.read()

    ip_img = display.Image(data=data, format='png', embed=True)
    return ip_img._repr_png_()


def display_cairo_context(ctx):
    """Displayhook function for cairo Context Images, target is rendered as PNG."""
    surface = ctx.get_target()
    return display_cairo_surface(surface)



def load_ipython_extension(ipython):
    # register display func with PNG formatter:
    png_formatter = get_ipython().display_formatter.formatters['image/png']
    try:
        import cairo
        dpi = png_formatter.for_type(cairo.Surface, display_cairo_surface)
        dpi = png_formatter.for_type(cairo.Context, display_cairo_context)
    except ImportError:
        pass
    
    try:
        import cairocffi
        dpi = png_formatter.for_type(cairocffi.surfaces.ImageSurface, display_cairo_surface)
        dpi = png_formatter.for_type(cairocffi.Surface, display_cairo_surface)
        dpi = png_formatter.for_type(cairocffi.Context, display_cairo_context)
    except ImportError:
        pass

def unload_ipython_extension(ipython):
    pass
