# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from odoo import fields, models

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = "Properties Offer"

    price = fields.Float(string="Price", help="Buyer Offer")
    status = fields.Selection(
        string="Status",
        selection=[("Accepted", "Accepted"), ("Refused", "Refused"),],
        copy=False,
        help="State of the property advertisement")
    
    partner_id = fields.Many2one('res.partner', string="Partner", required=True, help="Person who make the offer")
    property_id = fields.Many2one('estate.property', string="Property", required=True, help="Property")
