import inspect

import six
import mongoengine


# def get_reverse_fields(model):
#     for name, attr in model.__dict__.items():
#         # Django =>1.9 uses 'rel', django <1.9 uses 'related'
#         related = getattr(attr, 'rel', None) or \
#             getattr(attr, 'related', None)
#         if isinstance(related, RelatedObject):
#             # Hack for making it compatible with Django 1.6
#             new_related = RelatedObject(related.parent_model, related.model, related.field)
#             new_related.name = name
#             yield new_related
#         elif isinstance(related, models.ManyToOneRel):
#             yield related
#         elif isinstance(related, models.ManyToManyRel) and not related.symmetrical:
#             yield related


def get_model_fields(model):
    # reverse_fields = get_reverse_fields(model)
    # all_fields += list(reverse_fields)

    all_fields = list([field for field in six.itervalues(model._fields)])

    return all_fields


def is_valid_mongoengine_model(model):
    return inspect.isclass(model) and (
        issubclass(model, mongoengine.Document)
    )


def import_single_dispatch():
    try:
        from functools import singledispatch
    except ImportError:
        singledispatch = None

    if not singledispatch:
        try:
            from singledispatch import singledispatch
        except ImportError:
            pass

    if not singledispatch:
        raise Exception(
            "It seems your python version does not include "
            "functools.singledispatch. Please install the 'singledispatch' "
            "package. More information here: "
            "https://pypi.python.org/pypi/singledispatch"
        )

    return singledispatch
