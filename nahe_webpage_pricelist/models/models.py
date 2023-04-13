# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class nahe_webpage_pricelist(models.Model):
#     _name = 'nahe_webpage_pricelist.nahe_webpage_pricelist'
#     _description = 'nahe_webpage_pricelist.nahe_webpage_pricelist'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
