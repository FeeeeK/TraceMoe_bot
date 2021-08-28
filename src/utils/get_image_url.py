from typing import List

from vkbottle.bot import Message
from vkbottle_types.objects import MessagesMessageAttachment, PhotosPhotoSizes


def get_max_size(sizes: List[PhotosPhotoSizes]) -> str:
    if getattr(sizes[0], "type", None):
        size_values = list("opqrsmxklyzcwid")
        max_size = sorted(sizes, key=lambda x: size_values.index(x.type.value))[-1]
    else:
        max_size = sorted(sizes, key=lambda x: x.width + x.height)[-1]

    return getattr(max_size, "url", None) or getattr(max_size, "src", None)


def parse_attachments(att: List[MessagesMessageAttachment]):
    url = None

    if att[0].doc and att[0].doc.ext == "gif":
        url = get_max_size(att[0].doc.preview.photo.sizes)

    elif att[0].photo:
        url = get_max_size(att[0].photo.sizes)

    elif att[0].graffiti:
        url = att[0].graffiti.url

    elif att[0].video:
        url = get_max_size(att[0].video.image)

    elif att[0].type.value == "wall" and att[0].wall and att[0].wall.attachments:
        url = parse_attachments(att[0].wall.attachments)

    elif att[0].type.value == "sticker" and att[0].sticker:
        url = get_max_size(att[0].sticker.images)

    return url


def get_image_url(message: Message):
    url = None
    att = None

    if not (
        message.attachments
        and (message.attachments[0].type.value in ("doc", "wall", "photo", "video"))
        or hasattr(message, "reply_message")
        or hasattr(message, "fwd_messages")
    ):
        return None

    elif message.attachments:
        att = message.attachments

    elif message.reply_message:
        att = message.reply_message.attachments

    elif message.fwd_messages:
        for msg in message.fwd_messages:
            url = parse_attachments(msg.attachments)
            if url:
                return url
    if not att:
        return
    url = parse_attachments(att)
    return url
