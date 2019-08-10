# -*- coding: utf-8 -*-
from odoo import models, fields, api

class customer(models.Model):
    _inherit = 'res.partner'

    person_id = fields.Char('Cédula')
