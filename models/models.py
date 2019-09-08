# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class quiz(models.Model):
#     _name = 'odonto.quiz'

#     # customers = fields.One2many('res.partner', 'quiz_id', string='Clientes')
#     #Prueba
#     was_patient = fields.Boolean(string='¿Ha sido paciente en un hospital en los ultimnos años')
#     why_was_patient = fields.Char(string='Porque?')
#     whe_was_patient = fields.Char(string='Donde?')

#     was_hospitalized = fields.Boolean(string='¿Ha estado bajo atención médica durante los ultimos dos años?')
#     why_was_hospitalized = fields.Char(string='Porque?')
#     whe_was_hospitalized = fields.Char(string='Donde?')


class Customer(models.Model):
    _inherit = 'res.partner'

    person_id = fields.Char(string="Cédula")
    work_place = fields.Char(string="Lugar de trabajo")
    birthdate = fields.Date(string="Fecha de nacimiento")
    marital_status = fields.Selection([(1, 'Soltero'), (2, 'Casado(a)'), (3, 'Divorciado(a)'), (2, 'Viudo(a)')], 'Estado civil')
    gender = fields.Selection([(1, 'Masculino'), (2, 'Femenino')], 'Género')
    # quiz_id = fields.Many2one('odonto.quiz', string='Cuestionario')
    
    #Medical quiz
    was_patient = fields.Boolean(string='¿Ha sido paciente en un hospital en los ultimnos años')
    why_was_patient = fields.Char(string='¿Porque?')
    whe_was_patient = fields.Char(string='¿Donde?')

    was_hospitalized = fields.Boolean(string='¿Ha estado bajo atención médica durante los ultimos dos años?')
    why_was_hospitalized = fields.Char(string='¿Porque?')
    whe_was_hospitalized = fields.Char(string='¿Donde?')

    was_consuming_drugs = fields.Boolean(string='¿Ha tomado algún medicamento o droga durante el último año?')
    whi_was_consuming_drugs = fields.Char(string='¿Cual?')
    why_was_consuming_drugs = fields.Char(string='¿Porque?')

    is_allergic_anesthesia = fields.Boolean(string='¿Ha tomado algún medicamento o droga durante el último año?')
    which_ones_is_allergic = fields.Char(string='¿Cuales?')

    has_an_hemorrhage = fields.Boolean(string='¿Ha tenido alguna hemorragia que haya tenido que ser tratada?')

    has_another_disease = fields.Boolean(string="¿Ha tenido alguna otra enfermedad?")
    which_another_disease = fields.Char(string="¿Cual?")

    are_pregnant = fields.Boolean(string="¿Está embarazada?")
    how_many_weeks = fields.Char(string="¿Cuántas semanas?")
    
    are_breastfeeding = fields.Boolean(string="¿Está amamandatndo?")

    treatment_for_osteoporosis = fields.Boolean(string="¿Reciba tratamiento para la osteoporosis o con con bifosfonatos?")
    wich_one_medicament = fields.Char(string="¿Cuál medicamento?")
    #Medical quiz

class doctor(models.Model):
    _inherit = 'res.users'

    is_doctor = fields.Boolean(string='Es doctor?')
    events = fields.One2many('calendar.event', 'user_id', string='Citas')


class driver(models.Model):
    _inherit = 'calendar.event'

    #user_id = fields.Many2one('res.users', string='Médico responsable')
