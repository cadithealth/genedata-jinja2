# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# lib:  genedata.test_jinja2
# auth: Philip J Grabner <grabner@cadit.com>
# date: 2013/07/03
# copy: (C) Copyright 2013 Cadit Health Inc., All Rights Reserved.
#------------------------------------------------------------------------------

import unittest, os.path
import genedata, genedata.engine
from genedata.util import adict

#------------------------------------------------------------------------------
class TestGenedataJinja2(unittest.TestCase):

  maxDiff = None

  #----------------------------------------------------------------------------
  def test_jinja2(self):
    src  = '''\
<html>
 <head>
  <title>{{title}}</title>
 </head>
 <body>
  <h1>{{title}}</h1>
  <h2>{{doc.title}}</h2>
{% for section in sections %}\
   <h3>{{section.title}}</h3>
   <p>{{section.text}}</p>
{% endfor %}\
 </body>
</html>
'''
    tpl = genedata.engine.Template(
      source='string:' + src,
      renderer='jinja2')
    out = tpl.render('html', adict(
        title='Genedata',
        doc=adict(title='Jinja2'),
        sections=[
          adict(title='Overview', text='Good'),
          adict(title='Details', text='Poor'),
          adict(title='Utility', text='Excellent'),
          ]))
    chk = '''\
<html>
 <head>
  <title>Genedata</title>
 </head>
 <body>
  <h1>Genedata</h1>
  <h2>Jinja2</h2>
   <h3>Overview</h3>
   <p>Good</p>
   <h3>Details</h3>
   <p>Poor</p>
   <h3>Utility</h3>
   <p>Excellent</p>
 </body>
</html>\
'''
    self.assertMultiLineEqual(out, chk)

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
