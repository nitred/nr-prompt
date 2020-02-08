"""Text Prompt."""
from prompt_toolkit.widgets import TextArea


def get_text(prompt):
    return TextArea(prompt=prompt, multiline=False)
