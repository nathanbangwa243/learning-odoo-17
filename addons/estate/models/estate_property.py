# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from odoo import fields, models

from odoo import api
from odoo import exceptions

# local debug
from . import debug

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "ESTATE Properties"

    name = fields.Char(string="Title", required=True, help="Property name")

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
    
    # links
    type_id = fields.Many2one('estate.property.type', string="Type")
    tag_ids = fields.Many2many('estate.property.tag', string="Tag")

    salesperson_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user, help="Salesperson")
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False, help="Buyer Person")

    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers', help='List of offers')

    # computed fields
    total_area = fields.Integer(string="Total Area (sqm)", compute='_compute_total_area')

    best_price = fields.Float(string="Best Offer", compute='_compute_best_offer')

    # constraints

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)', 'A property expected price must be strictly positive'),
        ('check_selling_price', 'CHECK(selling_price >= 0)', 'A property selling price must be positive'),
    ]

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        """
            Compute and update total area.
        """
        # debug.print_logs(self._compute_total_area, msg=self)

        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        """
            Compute and update best offer
        """
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'))
    
    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'North'
        else:
            self.garden_area = 0
            self.garden_orientation = ''

            # non-blocking message
            return {'warning': {
                'title': "Non-blocking Warning",
                'message': 'Relax, is just a fun test for non-blocking message'}}
        
    def action_sold_property(self):
        for record in self:
            if record.state == 'Canceled':
                # Canceled property cannot be Sold
                raise exceptions.UserError("Canceled property cannot be Sold")
            else:
                record.state = 'Sold'
        
        return True
    
    def action_cancel_property(self):
        for record in self:
            if record.state == 'Sold':
                # Sold property cannot be Canceled
                raise exceptions.UserError("Sold property cannot be Canceled")

            else:
                record.state = 'Canceled'
            
        return True