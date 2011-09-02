from collective.sales import _
from plone.directives import form
from plone.namedfile.field import NamedImage
from zope import schema


class IShopCategory(form.Schema):
    """Schema interface for the shop category content type.
    """

    form.primary('title')
    title = schema.TextLine(
        title=_(u'title_label',
                default=u'Title'),
        description=_(u'title_help',
                      default=u''),
        required=True,
        )

    description = schema.Text(
        title=_(u'description_label',
                default=u'Description'),
        description=_(u'description_help',
                      default=u''),
        required=False,
        )

    cover_image = NamedImage(
        title=_(u'cover_image_label',
                default=u'Cover image'),
        description=_(u'cover_image_help',
                      default=u''),
        required=False,
        )
