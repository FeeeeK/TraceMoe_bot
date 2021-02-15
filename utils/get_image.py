from typing import List, Union
from vkbottle_types.objects import MessagesMessageAttachment, PhotosPhotoSizes


def get_max_size(sizes: List[PhotosPhotoSizes]) -> str:
    if getattr(sizes[0], "type", None):
        size_values = list("smxopqrklyzcwid")
        max_size = sorted(sizes, key=lambda x: size_values.index(x.type.value))[-1]

    else:
        max_size = sorted(sizes, key=lambda x: x.width + x.height)[-1]

    return getattr(max_size, "url", None) or getattr(max_size, "src", None)


def parse_attachments(att: List[MessagesMessageAttachment]) -> Union[str, None]:
    url = None

    if not att:
        return

    if att[0].doc and att[0].doc.ext == "gif":
        url = get_max_size(att[0].doc.preview.photo.sizes)

    elif att[0].photo:
        url = get_max_size(att[0].photo.sizes)

    elif att[0].video:
        url = get_max_size(att[0].video.image)

    elif att[0].wall and att[0].wall.attachments:
        url = parse_attachments(att[0].wall.attachments)

    elif att[0].sticker:
        url = get_max_size(att[0].sticker.images)

    return url


def get_image_url(ans) -> Union[str, None]:
    url = None
    att = None

    if not (
        ans.attachments
        and (ans.attachments[0].type.value in ("doc", "wall", "photo", "video"))
        or getattr(ans, "reply_message", None)
        or getattr(ans, "fwd_messages", None)
    ):
        return None

    elif ans.attachments:
        att = ans.attachments

    elif ans.reply_message:
        att = ans.reply_message.attachments

    elif ans.fwd_messages:
        for msg in ans.fwd_messages:
            url = parse_attachments(msg.attachments)

            if url:
                return url

    url = parse_attachments(att)
    return url
