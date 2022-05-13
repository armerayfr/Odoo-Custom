from odoo import api, fields, models


class WarungPayment(models.Model):
    _name = "warung.payment"
    _description = "Choose payment method for simplify the payment process"

    method_payments = fields.Selection([
        ('qris', 'QRIS'),
        ('cash', 'Cash'),
        ('gopay', 'Gopay'),
        ('other', 'Other')
    ],  required=True, default='qris')
    note = fields.Text(string='Description')
