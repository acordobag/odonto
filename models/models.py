# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    _inherit = 'res.partner'

    person_id = fields.Char(string="Cédula")
    work_place = fields.Char(string="Lugar de trabajo")
    birthdate = fields.Date(string="Fecha de nacimiento")
    marital_status = fields.Selection([(1, 'Soltero'), (2, 'Casado(a)'), (3, 'Divorciado(a)'), (2, 'Viudo(a)')], 'Estado civil')
    gender = fields.Selection([(1, 'Masculino'), (2, 'Femenino')], 'Género')
    quiz_id = fields.Many2one('odonto.quiz', string='Cuestionario')


class doctor(models.Model):
    _inherit = 'res.users'

    is_doctor = fields.Boolean(string='Es doctor?')
    events = fields.One2many('calendar.event','user_id',string='Citas')


class driver(models.Model):
    _inherit = 'calendar.event'

    #user_id = fields.Many2one('res.users', 'Médico responsable')

class quiz(models.Model):
    _name = 'odonto.quiz'
    
    q1 = fields.Boolean(string='¿Ha sido paciente en un hospital en los ultimnos años')
    why_q1 = fields.Char(string='Porque?')
    where_q1 = fields.Char(string='Donde?')

    q2 = fields.Boolean(string='¿Ha estado bajo atención médica durante los ultimos dos años?')
    why_q2 = fields.Char(string='Porque?')
    where_q2 = fields.Char(string='Donde?')
