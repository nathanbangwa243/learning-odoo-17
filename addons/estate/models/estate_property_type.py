# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = "Properties type"

    name = fields.Char(string="Name", required=True, help="Property type")

    # constraints
    _sql_constraints = [
        ('unique_property_type_name', 'UNIQUE(name)', 'A property cannot have duplicate types.'),
    ]