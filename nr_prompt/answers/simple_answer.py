"""Simple answer."""


class SimpleValue:
    def __init__(self, id, prompt=None, value=None):
        """."""
        self.id = id
        self._prompt = prompt
        self._value = value

    @property
    def prompt(self):
        """Return prompt or string representation of this SimpleValue."""
        if self._prompt is None:
            return self.id
        else:
            return self._prompt

    @property
    def value(self):
        """Return actual value of this SimpleValue."""
        if self._value is None:
            return self.id
        else:
            return self._value
