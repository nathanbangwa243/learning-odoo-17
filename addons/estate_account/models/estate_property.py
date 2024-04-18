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

        return super().action_sold_property()