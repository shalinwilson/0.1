# -*- coding: utf-8 -*-
from odoo import http

# class VehicleApi(http.Controller):
#     @http.route('/vehicle_api/vehicle_api/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vehicle_api/vehicle_api/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vehicle_api.listing', {
#             'root': '/vehicle_api/vehicle_api',
#             'objects': http.request.env['vehicle_api.vehicle_api'].search([]),
#         })

#     @http.route('/vehicle_api/vehicle_api/objects/<model("vehicle_api.vehicle_api"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vehicle_api.object', {
#             'object': obj
#         })