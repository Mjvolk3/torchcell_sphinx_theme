import os.path as osp

__version__ = '0.1.0'


def setup(app):
    app.add_html_theme('torchcell_sphinx_theme', osp.abspath(osp.dirname(__file__)))
