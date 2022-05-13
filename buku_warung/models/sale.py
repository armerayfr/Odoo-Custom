from odoo import api, fields, models


class WarungCustomer(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Char(string='Sale Description')
    payment_address = fields.Text(string='Payment Address')