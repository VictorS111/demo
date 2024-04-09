# -*- coding: utf-8 -*-

from odoo import fields, models


class HairdresserWorkingHours(models.Model):
    """'Hairdresser working_hours_xml hours' to store working_hours_xml hours of hairdresser"""
    _name = 'working.hours'
    _description = 'Hairdresser Working Hours'

    name = fields.Char(string="Day", help="Name of working_hours_xml hours")
    from_time = fields.Float(string="Starting Time", help="Starting time of "
                                                          "hairdresser")
    to_time = fields.Float(string="Closing Time", help="Hairdresser work ending time")
