# -*- coding: utf-8 -*-
from odoo import http

# class SequenceContact(http.Controller):
#     @http.route('/sequence_contact/sequence_contact/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sequence_contact/sequence_contact/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sequence_contact.listing', {
#             'root': '/sequence_contact/sequence_contact',
#             'objects': http.request.env['sequence_contact.sequence_contact'].search([]),
#         })

#     @http.route('/sequence_contact/sequence_contact/objects/<model("sequence_contact.sequence_contact"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sequence_contact.object', {
#             'object': obj
#         })