from odoo import api, fields, models


class WarungCustomer(models.Model):
    _name = "warung.customer"
    _description = "useful to track customer identity"


    # simple field
    name = fields.Char(string='Name', required=True)
    phone = fields.Text(string='Phone Number')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')