# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Job(models.Model):
    _name = 'odonto.job'

    name = fields.Char('Nombre del puesto')
    people = fields.One2many('res.partner','job_id', 'x')


class Customer(models.Model):
    _inherit = 'res.partner'

    person_id = fields.Char(string="Cédula")
    job_id = fields.Many2one('odonto.job', string="Puesto")
