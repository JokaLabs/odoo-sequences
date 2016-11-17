# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sequence_Employee(models.Model):
	_inherit = 'hr.employee'
	sequence_employee = fields.Char(string='Sequence employee', index=True, readonly=True)
	@api.model
	def create(self, vals):
	    vals['sequence_employee'] = self.env['ir.sequence'].next_by_code('employee.sequence')
	    return super(Sequence_Employee, self).create(vals)