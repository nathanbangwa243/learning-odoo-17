# -*- coding: utf-8 -*-

from odoo import fields, models

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "ESTATE Properties"

    name = fields.Text(string="Name", required=True, help="Property name")

    description = fields.Text(string="Description", help="Property description")

    postcode = fields.Text(string="Post code", help="Property Post code")

    date_availability = fields.Date(string="Date Availability", help="Property Date Availability")

    expected_price = fields.Float(string="Expected Price", required=True, help="Property Expected Price")

    selling_price = fields.Float(string="Selling Price", help="Property Selling Price")

    bedrooms = fields.Integer(string="Bedrooms", help="Property Bedrooms")

    living_area = fields.Integer(string="Living Area", help="Property Living Area")

    facades = fields.Integer(string="Facades", help="Property Facades")

    garage = fields.Boolean(string="Garage", help="Property Garage")

    garden = fields.Boolean(string="Garden", help="Property Garden")

    garden_area = fields.Integer(string="Garden Area", help="Property Garden Area")

    garden_orientation = fields.Selection(
        string="Orientation",
        selection=[("North", "North"), ("South", "South"), ("East", "East"), ("West", "West")],
        help="Orientation help to define the garden orientation")