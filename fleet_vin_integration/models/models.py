import urllib3
import json

from odoo import models, fields, api, http
from odoo.http import request
from odoo.addons.website.controllers.main import Website
from odoo.addons.portal.controllers.web import Home


class FleetVehicleExtend(models.Model):
    """Fleet Vehicle Extend."""

    _inherit = 'fleet.vehicle'

    @api.onchange('btn_function')
    def get_details(self):
        http = urllib3.PoolManager()
        URL = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/' + str(
            self.vin_number) + '?format=json&modelyear=2011'
        datas = http.request('GET', URL)
        datas = json.loads(datas.data.decode('utf-8'))
        datas = datas.get('Results')
        details = {}
        for dicts in datas:
            if dicts.get('VariableId') == 26:
                details['brand'] = dicts.get('Value')
            if dicts.get('VariableId') == 28:
                details['model_id'] = dicts.get('Value')
            if dicts.get('VariableId') == 29:
                details['model_year'] = dicts.get('Value')
            if dicts.get('VariableId') == 21:
                details['engine_power'] = dicts.get('Value')
            if dicts.get('VariableId') == 37:
                details['transmission_style'] = dicts.get('Value')
            if dicts.get('VariableId') == 18:
                details['engine_model'] = dicts.get('Value')
            if dicts.get('VariableId') == 9:
                details['no_of_cylinder'] = dicts.get('Value')
            if dicts.get('VariableId') == 33:
                details['no_of_seats'] = dicts.get('Value')
            if dicts.get('VariableId') == 14:
                details['no_of_doors'] = dicts.get('Value')
            if dicts.get('VariableId') == 2:
                details['battery_type'] = dicts.get('Value')
            if dicts.get('VariableId') == 58:
                details['battery_voltage'] = dicts.get('Value')
            if dicts.get('VariableId') == 59:
                details['battery_energy'] = dicts.get('Value')
            if dicts.get('VariableId') == 24:
                details['fuel_type'] = dicts.get('Value')
        brand_id = 0
        try:
            if details.get('brand'):
                nameupperc = details.get('brand')
                nameproper = nameupperc[0:1] + nameupperc[1:].lower()
                brand_id = self.env['fleet.vehicle.model.brand'].search([('name', '=', nameproper)], limit=1).id
                if brand_id:
                    pass
                else:
                    try:
                        brand_id = self.env['fleet.vehicle.model.brand'].create({'name': nameproper})

                    except:
                        pass
            if details.get('engine_power'):
                self.horsepower = int(float(details.get('engine_power')))
            if details.get('engine_model'):
                self.engine_size = str(details.get('engine_model'))
            if details.get('no_of_cylinder'):
                self.cylinders = int(details.get('no_of_cylinder'))
            if details.get('no_of_seats'):
                self.seats = int(details.get('no_of_seats'))
            if details.get('no_of_doors'):
                self.doors = int(details.get('no_of_doors'))
            if details.get('battery_type'):
                self.battery_type = str(details.get('battery_type'))
            if details.get('battery_voltage'):
                self.battery_voltage = str(details.get('battery_voltage'))
            if details.get('battery_energy'):
                self.battery_energy = str(details.get('battery_energy'))
        except:
            pass
        try:
            if details.get('fuel_type'):
                fuel_type = str(details['fuel_type'])
                try:
                    self.fuel_type = fuel_type.lower()
                except:
                    pass

            if details.get('model_id'):

                model = details.get('model_id')
                print("model name ", model)
                model_id = self.env["fleet.vehicle.model"].search([('name', '=', model)], limit=1).id

                if model_id:
                    self.model_id = model_id
                else:
                    self.model_id = self.env["fleet.vehicle.model"].create({'name': model, 'brand_id': brand_id.id})
            if details.get('model_year'):
                self.model_year = details.get('model_year')
        except:
            pass

        return
        {
        'type': 'ir.actions.client',
        'tag': 'reload',
        }



