# -*- coding: utf-8 -*-

from odoo import fields, models


class Service(models.Model):
    """Creates 'service' to store services"""
    _name = 'service'
    _description = 'Hairdresser Service'

    name = fields.Char(string="Name", required=True, help="Name of service")
    currency_id = fields.Many2one(comodel_name='res.currency',
                                  string='Currency', required=True,
                                  default=lambda self: self.env
                                  .user.company_id.currency_id.id,
                                  help="Currency for the service")
    price = fields.Monetary(string="Price", help="Amount for the service",
                            required=True)
    time_taken = fields.Float(string="Time", help="Approximate time required "
                                                  "for this service in Hours")
