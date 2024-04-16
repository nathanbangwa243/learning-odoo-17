# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from datetime import date

from odoo import fields, models
from odoo import api
from odoo import exceptions

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = "Properties Offer"

    price = fields.Float(string="Price", help="Buyer Offer")
    validity = fields.Integer(string="validity (days)", default=7, help="validity")
    date_deadline = fields.Date(string="Deadline", compute='_compute_date_deadline', inverse='_inverse_date_deadline', help='Validity date')

    status = fields.Selection(
        string="Status",
        selection=[("Accepted", "Accepted"), ("Refused", "Refused"),],
        copy=False,
        help="State of the property advertisement")
    
    partner_id = fields.Many2one('res.partner', string="Partner", required=True, help="Person who make the offer")
    property_id = fields.Many2one('estate.property', string="Property", required=True, help="Property")


    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = date.today() + timedelta(days=record.validity)
    
    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date:
                record.validity = (record.date_deadline - record.create_date.date()).days
            else:
                record.validity = record.date_deadline - datetime.now().date()
    
    def action_accept_offer(self):
        for record in self:
            record.status = 'Accepted'
        
        return True
    
    def action_refuse_offer(self):
        for record in self:
            record.status = 'Refused'
            
        return True