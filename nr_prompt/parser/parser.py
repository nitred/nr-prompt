"""Parser."""
from pprint import pprint, pformat
from nr_common.configreader import read_config


def parse():
    """."""
    config = read_config("examples/sample_question.yaml")
    cli_items = config.get("cli", None)

    if cli_items is None:
        print("No 'cli' items provided!")

    if not isinstance(cli_items, list):
        raise TypeError("'cli' items are expected to be a list.")

    return cli_items[0]
