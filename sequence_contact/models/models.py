# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sequence_Contact(models.Model):
	_inherit = 'res.partner'
	sequence_contact = fields.Char(string='Sequence contact', index=True, readonly=True)
	
	@api.model
	def create(self, vals):
	    vals['sequence_contact'] = self.env['ir.sequence'].next_by_code('contact.sequence')
	    return super(Sequence_Contact, self).create(vals)