# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from odoo import fields, models

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "ESTATE Properties"

    name = fields.Text(string="Title", required=True, help="Property name")

    description = fields.Text(string="Description", help="Property description")

    postcode = fields.Text(string="Postcode", help="Property Post code")

    date_availability = fields.Date(string="Available From", default=lambda self: (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d'), copy=False, help="Property Date Availability")

    expected_price = fields.Float(string="Expected Price", required=True, help="Property Expected Price")

    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False, help="Property Selling Price")

    bedrooms = fields.Integer(string="Bedrooms", default=2, help="Property Bedrooms")

    living_area = fields.Integer(string="Living Area (sqm)", help="Property Living Area")

    facades = fields.Integer(string="Facades", help="Property Facades")

    garage = fields.Boolean(string="Garage", help="Property Garage")

    garden = fields.Boolean(string="Garden", help="Property Garden")

    garden_area = fields.Integer(string="Garden Area", help="Property Garden Area")

    garden_orientation = fields.Selection(
        string="Orientation",
        selection=[("North", "North"), ("South", "South"), ("East", "East"), ("West", "West")],
        help="Orientation help to define the garden orientation")
    
    active = fields.Boolean(string="Active", default=True, help="Property is available")

    state = fields.Selection(
        string="State",
        selection=[("New", "New"), ("Offer Received", "Offer Received"), ("Offer Accepted", "Offer Accepted"), ("Sold", "Sold"), ("Canceled", "Canceled")],
        default="New",
        help="State of the property advertisement")
