# -*- coding: utf-8 -*-
from odoo import http

# class SequenceEmployee(http.Controller):
#     @http.route('/sequence_employee/sequence_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sequence_employee/sequence_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sequence_employee.listing', {
#             'root': '/sequence_employee/sequence_employee',
#             'objects': http.request.env['sequence_employee.sequence_employee'].search([]),
#         })

#     @http.route('/sequence_employee/sequence_employee/objects/<model("sequence_employee.sequence_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sequence_employee.object', {
#             'object': obj
#         })