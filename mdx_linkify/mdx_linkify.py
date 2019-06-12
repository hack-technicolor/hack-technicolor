import bleach

from markdown.postprocessors import Postprocessor
from markdown import Extension


class LinkifyPostprocessor(Postprocessor):
    def __init__(self, md, linkify_callbacks=[]):
        super(Postprocessor, self).__init__(md)
        self._callbacks = linkify_callbacks

    def run(self, text):
        text = bleach.linkify(text,
                              callbacks=self._callbacks,
                              skip_tags=['code'])
        return text


class LinkifyExtension(Extension):
    config = {'linkify_callbacks': [[], 'Callbacks to send to bleach.linkify']}

    def extendMarkdown(self, md):
        md.postprocessors.register(
            LinkifyPostprocessor(md, self.getConfig('linkify_callbacks')),
            "linkify",
            50)


def makeExtension(*args, **kwargs):
    return LinkifyExtension(*args, **kwargs)
