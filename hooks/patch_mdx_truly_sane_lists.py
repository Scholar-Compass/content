"""Patch mdx_truly_sane_lists to recognize the number used in ordered lists

Usage: [Sane Lists — Python-Markdown documentation](https://python-markdown.github.io/extensions/sane_lists/)
"""

# https://github.com/radude/mdx_truly_sane_lists/issues/21#issuecomment-2028015918
from mdx_truly_sane_lists.mdx_truly_sane_lists import TrulySaneOListProcessor

TrulySaneOListProcessor.LAZY_OL = False
