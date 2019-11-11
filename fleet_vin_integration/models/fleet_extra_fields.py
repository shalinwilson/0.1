from odoo import api,fields,models


class FleetExtraFields(models.Model):
    _inherit = 'fleet.vehicle'
    _description = 'Extra fields for fleet details to fill'

    vin_number = fields.Char("Vin Number")
    model_id = fields.Many2one('fleet.vehicle.model', 'Model',
                               track_visibility="onchange", required=True, help='Model of the vehicle')
    btn_function = fields.Boolean(string="fill details")
    battery_type1 = fields.Char(string="Battery Type")
    battery_voltage = fields.Integer(string="Battery Voltage")
    battery_energy = fields.Integer(string="Battery Energy")
