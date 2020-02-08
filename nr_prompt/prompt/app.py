"""."""
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous


def get_app(layout):
    bindings = KeyBindings()
    bindings.add(Keys.Tab)(focus_next)
    bindings.add(Keys.Enter)(focus_next)
    bindings.add(Keys.BackTab)(focus_previous)
    # CTRL-C to quit the prompt-app.
    @bindings.add("c-c")
    def exit_c(event):
        """Ctrl-C to quit."""
        event.app.exit(result=False)

    return Application(layout=layout, key_bindings=bindings, full_screen=False)
