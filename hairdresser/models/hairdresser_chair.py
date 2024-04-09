# -*- coding: utf-8 -*-

from datetime import date
from odoo import api, fields, models, _


class HairdresserChair(models.Model):
    """Class to create 'chair' to manage chairs in hairdresser"""
    _name = 'chair'
    _description = 'Hairdresser Chair'

    name = fields.Char(string="Chair", required=True, readonly=True,
                       default="New", help="Name for chair")
    number_of_orders = fields.Integer(string="No.of Orders", help="Number of ")
    # collection_today = fields.Float(string="Today's Collection",
    #                                 help="Today's collection")
    user_id = fields.Many2one(
        'customer', string="Customer",
        help="You can select the user from the Users Tab")
    date = fields.Datetime(string="Date", help="Chair available date")

    chair_created_user = fields.Integer(string=" Chair Created User",
                                        default=lambda self: self._uid,
                                        help="Chair created user")


