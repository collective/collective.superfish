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


How do i use it?
================

This package behaves as a "drop-in" replacement for ``plone.global_sections``.
Just install it :)


Customization
=============

Use Plone's Configuration Registry to change Superfish settings.
Filter for prefix ``ISuperfishSettings`` to see available options.


Do not show arrows
------------------

To not show the arrows for menuitems with subitems,
customize the Javascript initialization::


    jQuery('ul.sf-menu').superfish({
        cssArrows: false
    });

See https://superfish.joelbirch.co/options/ for a complete
list of available options.


CSS Styles
----------

By using superfish.css you should have everyting in place to get a working
superfish navigation.

Specific fixes and colors for plone's ``Barceloneta Theme`` can be found in
superfish-plone.css (you might deactivate these styles for your custom theme
layer to not need to override these styles)

You might want to have a look at the examples provided in the
`superfish download <https://github.com/joeldbirch/superfish/releases>`_

eg: https://github.com/joeldbirch/superfish/tree/1.7.4/examples

