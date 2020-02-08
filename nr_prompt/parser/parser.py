"""Parser."""
from pprint import pprint, pformat
from nr_common.configreader import read_config


def parse():
    """."""
    pprint(read_config("examples/sample_question.yaml"))
