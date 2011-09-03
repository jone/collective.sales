from collective.sales import _
from plone.app.textfield import RichText
from plone.directives import form
from plone.namedfile.field import NamedImage
from zope import schema
from zope.interface import Interface
from zope.interface import alsoProvides


class ISimpleShopItem(Interface):
    pass


class IMultiShopItem(Interface):
    pass


class IMultiShopItemVariant(form.Schema):

    form.primary('title')
    title = schema.TextLine(
        title=_(u'item_title_label', default=u'Title'),
        description=_(u'item_title_help', default=u''),
        required=True,
        )

    variant_label = schema.TextLine(
        title=_(u'item_variant_label_label', default=u'Variant label'),
        description=_(u'item_variant_label_help', default=u''),
        required=False,
        )


@form.default_value(field=IMultiShopItemVariant['variant_label'])
def default_variant_label(data):
    for obj in data.context.objectValues():
        if IMultiShopItemVariant.providedBy(obj):
            return IMultiShopItemVariant(obj).variant_label

    return ''



class IShopItemBehavior(form.Schema):
    """Behavior schema interface for the shop item content type.
    """

    form.primary('title')
    title = schema.TextLine(
        title=_(u'item_title_label',
                default=u'Title'),
        description=_(u'item_title_help',
                      default=u''),
        required=True,
        )

    cover_image = NamedImage(
        title=_(u'category_cover_image_label',
                default=u'Cover image'),
        description=_(u'category_cover_image_help',
                      default=u''),
        required=False,
        )

    text = RichText(
        title=_(u'category_text_label',
                default=u'Text'),
        description=_(u'category_text_help',
                      default=u''),
        required=False,
        )


alsoProvides(IShopItemBehavior, form.IFormFieldProvider)


class IBuyableBehavior(form.Schema):
    """Behavior schema interface, mixing in additional fields for
    making item buyable.
    """

    itemnumber = schema.TextLine(
        title=_(u'itemnumber_label', default=u'Item number'),
        description=_(u'itemnumber_help', default=u''),
        required=True)

    price = schema.Float(
        title=_(u'price_label', default=u'Price'),
        description=_(u'price_help', default=u''),
        default=0.0,
        required=True)


alsoProvides(IBuyableBehavior, form.IFormFieldProvider)
