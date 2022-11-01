# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Assets(models.Model):
    _inherit = 'stock.production.lot'

    # Create a repair order from a button on the asset
    def asset_repair(self):
        '''Button to trigger a new repair order directly from the asset'''
        for record in self:
            repair = {
                'description': f"Repair {record.name}",
                'product_id': record.product_id.id,
                'product_uom': record.product_uom_id.id,
                'location_id': record.last_location_id.id,
                'name': 'Repair of asset',
                'invoice_method': 'none',
                'product_qty': 1,
                'lot_id': self.id}

            create_repair = self.env['repair.order'].sudo().create(
                repair)

            # Open the newly created repair order in a new form view
            return{
                'name': 'Repair Order',
                'res_model': 'repair.order',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'context': {},
                'target': 'current',
                'res_id': create_repair.id,
            }
