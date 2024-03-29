History
=======

2.2 (unreleased)
----------------

- Nothing changed yet.


2.1 (2023-05-05)
----------------

- Python 3 support.


2.0 (2018-08-02)
----------------

- make final release.


2.0a1 (2017-11-24)
------------------

- migrate superfish resources to Plone 5 resource registry (see upgrade step)
  [petschki]
- behave as "drop-in" replacement for global_sections
  [petschki]
- add uninstall profile
  [petschki]
- update superfish resources to 1.7.9 and hoverIntent to 1.9.0
  [petschki]

1.1 (2016-06-23)
----------------

- Update superfish.js from 1.7.3 to 1.7.5,
  and hoverIntend from r7 (1.7.0) to 1.8.1
  [fRiSi]

- Don't break JS when jQuery is undefined. This happened for eg. on
  wildcard.foldercontents folder_content view
  [petschki]

1.0 - 2014-05-08
----------------

- Update superfish.js from 1.4.8 to 1.7.3
  and hoverIntent.js from r5 to r7
  [fRiSi]

  .. ATTENTION:: This update breaks css compatibility with the previous version!

- Add default formatting for superfish menu based on the `DEMO SKIN`
  in the `superfish default css
  <https://github.com/joeldbirch/superfish/blob/master/dist/css/superfish.css>`_
  to make it fit the `Sunburst Theme`

  Superfish Menu Layout changed from

  ``<li><span class="selected"><a .../></span></li>`` to

  ``<li class="selected"><a .../></li>``

  since javascript could not handle the
  additional span tag for setting the `.sf-with-ul` class.
  [fRiSi]


0.6 - 2010-08-11
----------------

- fixed dropdown for IE7 and IE8
  [fRiSi]

- replace `'` with ``&#39;`` instead of ``&apos;`` since
  IE7/8 can't handle this xhtml entity
  (http://inthemaze.net/post/2008/04/08/46-ie7-and-apos)
  [fRiSi]


0.5 - 2010-06-17
----------------

-  use `official hoverIntent.js`_ with docstring and versioninfo
   and replaced ``(function($){})(jQuery);`` with
   ``jQuery(function($){});`` syntax so the script does not conflict with
   collective.carousel (when both are merged to the same file by portal_javascript).
   [fRiSi]

   .. _`official hoverIntent.js`: http://cherne.net/brian/resources/jquery.hoverIntent.js

0.4 - 2010-05-12
----------------

- removed desc.replace(...) and added a custom entities method to fix #1.
  [saily]

- don't use version in metadata.xml for the package version in setup.py.
  the metadata version this is meant to reflect the version of the GS profile
  and must not be mixed up with the package version.  [fRiSi]

0.3 - 2010-03-17
----------------

- Replace " with &quot; to keep valid HTML if description contains quotes.
  [saily]

- Made id-generation more resistent against duplicated id's. We now use
  normalized urls to generate the item id.  [saily]

- added support to include portal_tabs in the superfish navigation by setting
  ``ADD_PORTAL_TABS = True`` in subclasses [fRiSi]

- added some documentation targeted at integrators [fRiSi]

- don't render superfish_init.js with ``inline=True`` since this leads to
  strange errors in
  Products.ResourceRegistries-2.0b2-py2.6.egg/Products/ResourceRegistries/browser/scripts.pt
  eg when adding a `StaticText Portlet`

  ``AttributeError: 'DirContainedFileResource5' object has no attribute 'POST'``

  according to the `resourceregistry documentation`_ it's better to set inline to `False`
  in any case.

  .. _`resourceregistry documentation`: http://plone.org/documentation/kb/working-with-resourceregistries/registry-entry-parameters

- Removed caching after some discussions with fRiSi.
  We left the code but disabled it by default, enable it again uncommenting
  the ram.cache line::

    #@ram.cache(_render_sections_cachekey)
    def render(self):
        return self.index()

- Displaying superfish menu only when installed in portal_quickinstaller by
  adding a superfish-browserlayer through browserlayer.xml file.  [saily]

- Changed default values for 'interval' and 'timeout' of hoverIntent which
  controls the show and hide process of the submenu. Read more about
  configuration of hoverIntent here: http://cherne.net/brian/resources/jquery.hoverIntent.html

0.2 - 2009-06-12
----------------

- Moved from full to safe compression for javascript files.
  [saily]

- Removed unused class attributes for SuperFishViewlet.
  [saily]

- Added caching to improve rendering performance.
  [saily]

0.1 - 2009-06-09
----------------

- Initial import and idea  [saily]

