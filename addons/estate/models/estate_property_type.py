# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = "Properties type"
    _order = "name"

    name = fields.Char(string="Name", required=True, help="Property type")

    property_ids = fields.One2many('estate.property', 'type_id', string='Properties', help='Type properties')

    # constraints
    _sql_constraints = [
        ('unique_property_type_name', 'UNIQUE(name)', 'A property cannot have duplicate types.'),
    ]