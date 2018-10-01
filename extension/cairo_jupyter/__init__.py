"""
Display Hooks for pycairo, cairocffi Surfaces and Contexts.
"""
import logging
import os

from io import BytesIO
from IPython.core import display

CAIRO_JUPYTER_LOG = "CAIRO_JUPYTER_LOG"

def setup_logging():
    logger = logging.getLogger("CAIRO_JUPYTER_LOG")
    level = os.environ.get(CAIRO_JUPYTER_LOG) 
    if level in ['debug', 'info', 'warning', 'error']:
        logger.setLevel(level)
    else:
        logger.addHandler(logging.NullHandler())


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
        png_formatter.for_type(cairo.Surface, display_cairo_surface)
        png_formatter.for_type(cairo.Context, display_cairo_context)
    except ImportError:
        cairo = None
        logger.debug("import cairocffi failed")

    try:
        import cairocffi
        png_formatter.for_type(cairocffi.surfaces.ImageSurface, display_cairo_surface)
        png_formatter.for_type(cairocffi.Surface, display_cairo_surface)
        png_formatter.for_type(cairocffi.Context, display_cairo_context)
    except ImportError:
        cairocffi = None
        logger.debug("import cairocffi failed")

    if not any([cairo, cairocffi]):
        logger.error("Cairo or CairoCFFI not found")

def unload_ipython_extension(ipython):
    pass


setup_logging()
