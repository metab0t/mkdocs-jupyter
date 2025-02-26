import os

import pytest

from mkdocs_jupyter import __about__  as mkj_about
from mkdocs_jupyter.config import settings

pytestmark = [pytest.mark.pkg]


def test_import():
    assert mkj_about.__version__ is not None
    assert mkj_about.__version__ != "0.0.0"
    assert len(mkj_about.__version__) > 0


def test_assets_included():
    mkdocs_html = os.path.join(settings.templates_dir, "mkdocs_html")
    assert os.path.exists(os.path.join(mkdocs_html, "conf.json"))
    assert os.path.exists(os.path.join(mkdocs_html, "notebook.html.j2"))

    html_assets = os.path.join(mkdocs_html, "assets")
    assert os.path.exists(os.path.join(html_assets, "clipboard.umd.js"))
    assert os.path.exists(os.path.join(html_assets, "mkdocs-jupyter.css"))
    assert os.path.exists(os.path.join(html_assets, "mkdocs-jupyter.css.map"))
    assert os.path.exists(os.path.join(html_assets, "mkdocs-jupyter.js"))
    # assert os.path.exists(os.path.join(html_assets, "mkdocs-jupyter.js.map"))

    mkdocs_md = os.path.join(settings.templates_dir, "mkdocs_md")
    assert os.path.exists(os.path.join(mkdocs_md, "conf.json"))
    assert os.path.exists(os.path.join(mkdocs_md, "md-no-codecell.md.j2"))
