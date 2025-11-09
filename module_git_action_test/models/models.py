# Intentionally poorly formatted
import sys, os
from odoo import models, fields,api


class TestModel(models.Model):
  _name = 'test.model'
  _description= 'Test Model'

  name = fields.Char( string='Name',required=True)


def some_method(self):
   """Unused variable to trigger pylint."""
   unused_var = 1
   print("This line has extra spaces")
   return self.name