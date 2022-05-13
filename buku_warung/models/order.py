from odoo import api, fields, models


class WarungOrder(models.Model):
    _name = "warung.order"
    _description = "useful to track customer order"

    invoice_code = fields.Char(string='Invoice Number', required=True)
    amount = fields.Integer(string='Total Amount', required=True)
    shipping_cost = fields.Integer(string='Total Amount', required=True)

    shipping_service = fields.Selection([
        ('jne', 'JNE'),
        ('tiki', 'Tiki'),
        ('anteraja', 'AnterAja'),
        ('other', 'Other')  
    ], required=True, default='tiki')
    note = fields.Text(string='Description')