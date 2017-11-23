====================
collective.superfish
====================

.. contents::

What is it?
===========

collective.superfish integrates the `jQuery Superfish plugin`_ into Plone.

Superfish is a really nice solution for dropdown menus using css, valid xhtml
and JavaScript which degrades gracefully if JavaScript is not available.

.. _`jQuery Superfish plugin`: https://superfish.joelbirch.co/


How do you use it?
==================

This package behaves as a "drop-in" replacement for ``plone.global_sections``.
Just install it :)


Customization
=============

Use Plone's Configuration Registry to change Superfish settings.
Filter for prefix ``ISuperfishSettings`` to see available options.

For integrators you can set the following records in ``registry.xml`` of your theme profile::

    <records interface='collective.superfish.interfaces.ISuperfishSettings' prefix='superfish'>
        <value key="add_portal_tabs">True</value>
        <value key="menu_depth">2</value>
        <value key="superfish_options">{ "delay": 800, "cssArrows": true }</value>
    </records>

See https://superfish.joelbirch.co/options/ for a complete
list of available ``superfish_options``.

