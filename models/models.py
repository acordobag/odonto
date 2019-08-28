# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    _inherit = 'res.partner'

    person_id = fields.Char(string="Cédula")
    job_id = fields.Many2one('odonto.job', string="Job")


class Job(models.Model):
    _name = 'odonto.job'

    name = fields.Char('Nombre del puesto')
