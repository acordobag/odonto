# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Customer(models.Model):
    _inherit = 'res.partner'

    person_id = fields.Char(string="Cédula", required=True)
