from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CreateBookingWizard(models.TransientModel):
    _name = "create.booking.wizard"
    _description = "Create Booking Wizard"

    time = fields.Date(string='Time', required=False)
    user_id = fields.Many2one('customer', string="Customer", required=False)

    def action_create_booking(self):
        print('Button Is Clicked')
        vals = {
            'user_id': self.user_id.id,
            'time': self.time,
        }
        booking_rec = self.env['hairdresser'].create(vals)
        print("appointment_id", booking_rec)

        return {
            'name': _('Hairdresser'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hairdresser',
            'res_id': booking_rec.id,
            'target': 'new',
        }




