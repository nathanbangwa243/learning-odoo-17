# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from datetime import date

from odoo import fields, models
from odoo import api
from odoo import exceptions
from odoo.exceptions import ValidationError

from odoo import Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold_property(self):
        """

        """
        # Call the super method to perform the default action_sold_property logic
        result = super().action_sold_property()

        # Retrieve the partner_id from the current estate.property
        partner_id = self.buyer_id or False

        # Calculate the amounts for the invoice lines
        property_name = self.name

        selling_price = self.selling_price
        administrative_fee = 100.00

        line1_amount = selling_price * 0.06  # 6% of selling price
        line2_amount = administrative_fee

        # Create the account.move with the specified values
        move_values = {
            'partner_id': partner_id.id if partner_id else False,
            'move_type': 'out_invoice',  # Corresponds to 'Customer Invoice'
            "line_ids": [
                Command.create({
                    'name': property_name,
                    "quantity": 1,
                    "price_unit": selling_price,
                }),
                Command.create({
                    'name': 'Property Sale - 6% of Selling Price',
                    "quantity": 1,
                    "price_unit": line1_amount,
                }),
                Command.create({
                    'name': 'Administrative Fees',
                    "quantity": 1,
                    "price_unit": line2_amount,
                }),

            ],
        }
        self.env['account.move'].create(move_values)

        return result