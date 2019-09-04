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
    quiz_id = fields.Many2one('odonto.quiz', 'Cuestionario')


class doctor(models.Model):
    _inherit = 'res.users'

    is_doctor = fields.Boolean(string='Es doctor?')
    events = fields.One2many('calendar.event','user_id','Citas')


class driver(models.Model):
    _inherit = 'calendar.event'

    #user_id = fields.Many2one('res.users', 'Médico responsable')

class quiz(models.Model):
    _name = 'odonto.quiz'
    
    was_patient = fields.Boolean(string='¿Ha sido paciente en un hospital en los ultimnos años')
    why_was_patient = fields.Char(string='Porque?')
    whe_was_patient = fields.Char(string='Donde?')

    was_hospitalized = fields.Boolean(string='¿Ha estado bajo atención médica durante los ultimos dos años?')
    why_was_hospitalized = fields.Char(string='Porque?')
    whe_was_hospitalized = fields.Char(string='Donde?')
