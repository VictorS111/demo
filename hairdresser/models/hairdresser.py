from odoo import api, fields, models


class Hairdresser(models.Model):
    _name = 'hairdresser'
    _description = 'Hairdresser'

    name_hairdresser = fields.Char(string="Name hairdresser", required=False, help="Name of customer")
    state = fields.Selection(string="State", default="draft",
                             selection=[('draft', 'Draft'),
                                        ('approved', 'Approved'),
                                        ('rejected', 'Rejected')],
                             help="State of the booking")
    time = fields.Datetime(string="Date", required=True,
                           help="Start time of the order")
    phone = fields.Char(string="Phone", help="Phone number of customer.")
    email = fields.Char(string="E-Mail", help="Email of employee")
    service_ids = fields.Many2many(comodel_name='service',
                                   string="Services",
                                   help="Hairdresser services")
    amount = fields.Float(string="Total Amount")
    user_id = fields.Many2one(
        'customer', string="Customer",
        help="You can select the user from the Users Tab"
             "Last user from the Users Tab will be selected "
             "as the Current User.")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")

    def action_approve_booking(self):
        for rec in self:
            rec.state = 'approved'

    def action_reject_booking(self):
        for rec in self:
            rec.state = 'rejected'
