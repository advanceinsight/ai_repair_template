# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date
import africastalking


class RepairTemplate(models.Model):
    _inherit = 'repair.order'
    _rec_name = 'description'

    # Define a repair order to be a template
    is_template = fields.Boolean(string='Is Template')

    # You can only select a repair order template that has been created for this product
    template_id = fields.Many2one(
        'repair.order',
        'Template',
        domain="[('is_template', '=', True),('product_id', '=', product_id)]",
        default=False)

    def get_template(self):
        '''Pull data from a predefined repair order template into an existing repair order'''
        for record in self:
            repair_id = self.id

            # Copy fields from the selected template to the new Repair Order
            record.tag_ids = record.template_id.tag_ids
            record.internal_notes = record.template_id.internal_notes
            record.quotation_notes = record.template_id.quotation_notes

            # Clear the repair_line and fee_line fields before adding data from the template
            record.operations = [(5, 0, 0)]
            record.fees_lines = [(5, 0, 0)]

            # Copy the operations from the selected template to the new Repair Order
            for operation in record.template_id.operations:
                repair_line = self.env['repair.line'].create({
                    'location_dest_id': operation.location_dest_id.id,
                    'location_id': operation.location_id.id,
                    'name': operation.name,
                    'price_unit': operation.product_id.list_price,
                    'product_id': operation.product_id.id,
                    'product_uom': operation.product_uom.id,
                    'product_uom_qty': operation.product_uom_qty,
                    'repair_id': repair_id,
                    'state': operation.state,
                    'type': operation.type, })

            # Copy the fees from the selected template to the new Repair Order
            for line in record.template_id.fees_lines:
                fee_line = self.env['repair.fee'].create({
                    'name': line.name,
                    'price_unit': line.product_id.list_price,
                    'product_id': line.product_id.id,
                    'product_uom': line.product_uom.id,
                    'product_uom_qty': line.product_uom_qty,
                    'repair_id': repair_id,
                })
