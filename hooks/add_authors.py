"""Add additional authors from pages' metadata.

## `*.md`需要的元数据

- `additional_authors`：仓库提交记录无法体现的额外作者，不填则不添加。

下面是些例子，更多细节请参考 [git-authors 的文档](https://timvink.github.io/mkdocs-git-authors-plugin/usage.html#in-theme-templates)。

```yaml
additional_authors:
  - 叶文洁
  - name: 王淼
    email: water@3body.com
    last_datetime: 2006-12-01 00:12:00 +0800
```
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from math import nan
from operator import itemgetter
from typing import TYPE_CHECKING

from mkdocs.plugins import get_plugin_logger

if TYPE_CHECKING:
    from typing import Any

    from mkdocs.config.defaults import MkDocsConfig
    from mkdocs.structure.nav import Navigation
    from mkdocs.structure.pages import Page
    from mkdocs.utils.templates import TemplateContext

DEFAULT_TIME_ZONE = timezone(timedelta(hours=8))

log = get_plugin_logger(__name__)


def _parse(author: dict[str, Any] | str) -> dict[str, Any]:
    """Parse an author in `page.meta`."""
    if isinstance(author, str):
        author = {"name": author}
    if "name" not in author:
        log.error(f"Everyone in additional_authors should have a name: {author}")

    defaults = {
        "email": "",
        "last_datetime": datetime.now(DEFAULT_TIME_ZONE).isoformat(
            sep=" ",
            timespec="seconds",
        ),
        "lines": nan,
        "contribution": "N/A",
    }

    return defaults | author


def on_page_context(
    context: TemplateContext,
    page: Page,
    config: MkDocsConfig,
    nav: Navigation,
) -> TemplateContext | None:
    """Append `git_info.page_authors` from page's metadata."""
    # How the plugin fills the context: https://github.com/timvink/mkdocs-git-authors-plugin/blob/859a90eeb5fe6f810463b4426e5d28575aee95b0/mkdocs_git_authors_plugin/plugin.py#L222-225
    # How the theme uses it: https://github.com/squidfunk/mkdocs-material/blob/860869be09b519da793cc4a56344f9b54d9c7e7c/src/templates/partials/source-file.html#L56-L67
    if "git_info" in context and (authors := page.meta.get("additional_authors")):
        context["git_info"]["page_authors"].extend(map(_parse, authors))
        context["git_info"]["page_authors"].sort(key=itemgetter("name"))
