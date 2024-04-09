# -*- coding: utf-8 -*-
################################################################################
from odoo import fields, models


class Customer(models.Model):
    _name = "customer"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hairdresser customer"

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    is_child = fields.Boolean(string="Is Child ?", tracking=True)
    phone = fields.Char(string="Phone")
    notes = fields.Text(string="Notes")


