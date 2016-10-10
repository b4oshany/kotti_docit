# -*- coding: utf-8 -*-

"""
Created on 2016-09-20
:author: Oshane Bailey (oshane@alteroo.com)
"""

from kotti.resources import File, Image, Document
from pyramid.i18n import TranslationStringFactory

from kotti_pdf.resources import PDF

_ = TranslationStringFactory('kotti_docit')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_docit.kotti_configure

        to enable the ``kotti_docit`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_docit'
    settings['kotti.alembic_dirs'] += ' kotti_docit:alembic'
    settings['kotti.available_types'] += ' kotti_docit.resources.AdminManual'
    settings['kotti.fanstatic.view_needed'] += ' kotti_docit.fanstatic.css_and_js'
    File.type_info.addable_to.append('AdminManual')
    Image.type_info.addable_to.append('AdminManual')
    PDF.type_info.addable_to.append('AdminManual')
    Document.type_info.addable_to.append('AdminManual')


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('kotti_docit:locale')
    config.add_static_view('static-kotti_docit', 'kotti_docit:static')

    config.scan(__name__)
