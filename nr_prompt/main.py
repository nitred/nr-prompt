"""Main entrypoint."""
from pprint import pprint
from nr_prompt.parser.parser import parse
from nr_prompt.prompt.widgets import get_text
from nr_prompt.prompt.layout import get_layout
from nr_prompt.prompt.app import get_app
import sys


def abort():
    print("Aborted!")
    sys.exit(0)


def run():
    """."""
    item = parse()

    text_widget = get_text(item["prompt"])

    layout = get_layout(text_widget)

    app = get_app(layout)

    app_status = app.run()

    if not app_status:
        abort()

    pprint(f"App is done with status: {app_status}")
    return app_status
