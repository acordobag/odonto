# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    _inherit = 'res.partner'

    person_id = fields.Char(string="Cédula")
    work_place = fields.Char(string="Lugar de trabajo")
    birthdate = fields.Date(string="Fecha de nacimiento")
    marital_status = fields.Selection(
        [(1, 'Soltero'), (2, 'Casado(a)'), (3, 'Divorciado(a)'), (2, 'Viudo(a)')], 'Estado civil')
    gender = fields.Selection([(1, 'Masculino'), (2, 'Femenino')], 'Género')


class doctor(models.Model):
    _inherit = 'res.users'

    is_doctor = fields.Boolean('Es doctor?')
    events = fields.One2many('calendar.event','user_id','Citas')


class driver(models.Model):
    _inherit = 'calendar.event'

    user_id = fields.Many2one('res.users', 'Doctor')
