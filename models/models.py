class customer(models.Model):
    _inherit = 'res.partner'

    person_id = fields.Char('Cédula')
