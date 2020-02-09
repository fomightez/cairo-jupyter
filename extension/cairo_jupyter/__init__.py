"""
Display Hooks for pycairo, cairocffi Surfaces and Contexts.
"""
import logging
import os

from io import BytesIO
from IPython import display, get_ipython

CAIRO_JUPYTER_LOG = "CAIRO_JUPYTER_LOG"


def setup_logging():
    logger = logging.getLogger(CAIRO_JUPYTER_LOG)
    level = os.environ.get(CAIRO_JUPYTER_LOG)
    if level in ["debug", "info", "warning", "error"]:
        logger.setLevel(level)
    elif level == "1":
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.ERROR)


def cairo_surface_as_png_data(surface):
    """
    Render surface with write_to_png and return the data
    so that PNGFormatter can render it.
    """
    # Fill buffer with png data then rewind buffer to start
    buffer = BytesIO()
    surface.write_to_png(buffer)
    buffer.seek(0)

    return buffer.read()


def cairo_context_as_png_data(context):
    """
    Get the target surface and render to png, return data
    suitable for PNGFormatter to render.
    """
    surface = context.get_target()
    return cairo_surface_as_png_data(surface)


def load_ipython_extension(ipython):
    # register display func with PNG formatter:
    png_formatter = get_ipython().display_formatter.formatters["image/png"]
    try:
        import cairo
    except ImportError:
        cairo = None
        logger.debug("import cairocffi failed")
    else:
        png_formatter.for_type(cairo.Surface, cairo_surface_as_png_data)
        png_formatter.for_type(cairo.Context, cairo_context_as_png_data)

    try:
        import cairocffi
    except ImportError:
        cairocffi = None
        logger.debug("import cairocffi failed")
    else:
        png_formatter.for_type(
            cairocffi.surfaces.ImageSurface, cairo_surface_as_png_data
        )
        png_formatter.for_type(cairocffi.Surface, cairo_surface_as_png_data)
        png_formatter.for_type(cairocffi.Context, cairo_context_as_png_data)

    if not any([cairo, cairocffi]):
        logger.error("Cairo or CairoCFFI not found.")


def unload_ipython_extension(ipython):
    pass


setup_logging()
