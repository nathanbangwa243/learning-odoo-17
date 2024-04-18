# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from datetime import date

from odoo import fields, models
from odoo import api
from odoo import exceptions
from odoo.exceptions import ValidationError

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold_property(self):
        """

        """
        # Call the super method to perform the default action_sold_property logic
        result = super().action_sold_property()

        # Retrieve the partner_id from the current estate.property
        partner_id = self.buyer_id or False

        # Create the account.move with the specified values
        move_values = {
            'partner_id': partner_id.id if partner_id else False,
            'move_type': 'out_invoice',  # Corresponds to 'Customer Invoice'
            # Add other required fields here
        }
        self.env['account.move'].create(move_values)

        return result