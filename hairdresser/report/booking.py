from odoo import api, models, _


class BookingReport(models.AbstractModel):
    _name = 'report.hairdresser.booking_report'
    _description = 'Booking Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("yes entered here in the function")
        if data['form']['user_id']:
            print("yes entered here in the function")
            bookings = self.env['hairdresser'].search([('user_id', '=', data['form']['user_id'][0])])
        else:
            bookings = self.env['hairdresser'].search([])
        booking_list = []
        for app in bookings:
            vals = {
                'customer': app.user_id,
                'service': app.service_ids,
                'booking_date': app.time
            }
            booking_list.append(vals)
        return {
            'doc_model': 'hairdresser',
            'bookings': bookings,
        }


