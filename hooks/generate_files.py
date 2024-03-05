"""Generate summary and other files in `docs_dir`.

Used by mkdocs-gen-files and other plugins.

## `university/*.md`需要的元数据

- `location`：所在地区，例如`北京`，默认`京外`。
"""
from __future__ import annotations

from pathlib import Path

import mkdocs_gen_files
from mkdocs.config import load_config
from mkdocs.utils.meta import get_data


def get_location_catalog(docs_dir: Path) -> dict[str | None, list[Path]]:
    """Get locations and universities in each."""
    catalog: dict[str | None, list[Path]] = {}
    for u in (docs_dir / "university").glob("*.md"):
        _, meta = get_data(u.read_text(encoding="utf-8"))
        location = meta.get("location", "京外")

        if location not in catalog:
            catalog[location] = []
        catalog[location].append(u)
    return catalog


def main() -> None:
    config = load_config()
    docs_dir = Path(config.docs_dir)

    catalog = get_location_catalog(docs_dir)
    # 为了控制显示顺序，人为指定 locations
    locations = ["北京", "京外"]
    assert (
        len(locations) == len(catalog)
    ), "人为规定的`locations`数量应当与实际相同。如果您给某个`university/*.md`加了新的`location`，应当更新`locations`。"

    with mkdocs_gen_files.open("SUMMARY.md", "w") as f:  # Used by mkdocs-literate-nav
        tab = " " * 4

        print("- [前言](index.md)", file=f)

        print("- [院校](university/index.md)", file=f)
        for u in (docs_dir / "university").glob("*.md"):
            path = u.relative_to(docs_dir).as_posix()
            print(f"{tab}- [{u.stem}]({path})", file=f)

        print(f"- 专业\n{tab}- major/*.md", file=f)

        print("- *.md", file=f)

    with mkdocs_gen_files.open("university/index.md", "w") as f:
        print("目前包含", end="", file=f)
        print(
            "、".join(f"{len(catalog[loc])}所[{loc}院校](#{loc})" for loc in locations),
            end="",
            file=f,
        )
        print("。", end="\n\n", file=f)

        for loc in locations:
            print(f"## {loc}", end="\n\n", file=f)
            for u in catalog[loc]:
                path = u.relative_to(docs_dir / "university").as_posix()
                print(f"- [{u.stem}]({path})", file=f)

    with mkdocs_gen_files.open("major/index.md", "w") as f:
        n = len(list((docs_dir / "major").glob("*.md")))
        print(f"目前包含{n}个专业文档信息。", file=f)


main()
