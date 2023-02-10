import argparse
import logging
import sys


from mia import executive


CORE_VENV_DEPS = ('pip', 'setuptools')
logger = logging.getLogger(__name__)


def main(argv=None):
    executive.executive_function()
