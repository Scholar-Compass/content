from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs_macros.plugin import MacrosPlugin


def define_env(env: MacrosPlugin):
    @env.macro
    def still_migrating():
        """仍在迁移"""
        return f"""
!!! warning ":material-file-move-outline: 仍在迁移"

    此文档尚未完成迁移，排版可能不正常。建议您暂时参阅[**:material-file-document-outline:原先的飞书版本**]({env.page.meta['feishu_url']})。

    如果您有兴趣帮助迁移，可以[:material-file-edit-outline:编辑此页]({env.page.edit_url})。
    （记得到 [:octicons-issue-opened-24:议题#6](https://github.com/Scholar-Compass/content/issues/6) 说一声，以免和同学撞车。）
"""

    @env.macro
    def work_in_progress():
        """尚未完成

        如果原先已在飞书完成，只是仍在迁移，应使用`still_migrating()`。
        """
        return f"""
!!! warning ":octicons-git-pull-request-draft-24: 尚未完成"

    此文档尚未完成，可能缺失关键信息。

    如果您有兴趣帮助完善，可以[:material-file-edit-outline:编辑此页]({env.page.edit_url})。
"""

    @env.macro
    def b23_tv(bvid: str) -> str:
        """哔哩哔哩视频

        # 示例

        ```
        {{ b23_tv("BV1ua4y1E7uf") }}
        ```

        # 参数

        - `bvid`：BV号，以`BV`开头，例如`BV1ua4y1E7uf`。

        # 相关链接

        [模板:`BilibiliVideo` - 萌娘百科 万物皆可萌的百科全书](https://zh.moegirl.org.cn/Template:BilibiliVideo)
        """
        # 依赖`extra.css`
        return f"""
<aside class="b23-tv">
    <iframe loading="lazy" src="https://player.bilibili.com/player.html?autoplay=0&as_wide=1&bvid={bvid}"></iframe>
</aside>
"""

    @env.macro
    def just_kidding(text: str, title: str = "只为博君一笑，不必照单全收XD") -> str:
        """胡话

        一段被划掉的文字，适合标注玩笑话、胡话，或者虽然真实但完全只因幽默效果而被提及的内容。

        请勿滥用。（为此还特意采用了比 markdown（`~~`）更复杂的语法）

        请尽量保持语句连贯——无论是否真的划掉文字，最好语句都通顺，且标点符号也正确。

        # 示例

        ```
        中国人民大学简称“人大”{{ just_kidding("（不是“人民代表大会”）") }}，是中国共产党创办的第一所新型正规大学。
        ```

        # 参数

        - `text`：要划掉的文字。
        - `title`：鼠标放到文字上显示的内容，默认为“只为博君一笑，不必照单全收XD”。

        # 相关链接

        [模板:`胡话` - 萌娘百科 万物皆可萌的百科全书](https://zh.moegirl.org.cn/Template:胡话)
        """
        # 依赖`extra.css`
        return f'<s class="just-kidding" title="{title}">{text}</s>'
