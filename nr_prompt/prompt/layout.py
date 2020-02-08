"""."""
from prompt_toolkit.layout.containers import VSplit, HSplit
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import (
    Frame,
    Button,
)
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.application.current import get_app
import sys
from prompt_toolkit import prompt


def get_handler():
    return get_app().exit(result="Done!")


def get_layout(widget):
    root_container = VSplit(
        width=80,
        children=[
            HSplit(
                padding=1,
                children=[
                    Frame(
                        title="Database Table Details:", body=HSplit(width=80, children=[widget]),
                    ),
                    VSplit(children=[Button("Done", handler=get_handler, width=80)]),
                ],
            ),
        ],
    )

    return Layout(root_container)
