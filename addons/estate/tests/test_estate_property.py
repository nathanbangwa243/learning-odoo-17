from odoo.exceptions import UserError
from odoo.tests import tagged, Form
from odoo.tests.common import TransactionCase


@tagged('post_install', '-at_install')
class EstateTestCase(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(EstateTestCase, cls).setUpClass()

        cls.partner_1 = cls.env['res.partner'].create({'name': 'Partner 1'})
        cls.partner_2 = cls.env['res.partner'].create({'name': 'Partner 2'})
        cls.partner_3 = cls.env['res.partner'].create({'name': 'Partner 3'})

        cls.properties = cls.env['estate.property'].create([
            {'name': 'Property 1', 'living_area': 20, 'garden_area': 10, 'expected_price': 100000},
            {'name': 'Property 2', 'living_area': 30, 'garden_area': 15, 'expected_price': 150000},
        ])

        cls.offers = cls.env['estate.property.offer'].create([
            {'property_id': cls.properties[0].id, 'price': 110000, 'status': 'offer_accepted',
             'partner_id': cls.partner_1.id},
            {'property_id': cls.properties[1].id, 'price': 150000, 'status': 'offer_refused',
             'partner_id': cls.partner_2.id},
        ])

    def test_creation_area(self):
        self.properties[0].living_area = 20
        self.properties[0].garden_area = 10
        self.properties[1].living_area = 30
        self.properties[1].garden_area = 15

        self.assertRecordValues(self.properties, [
            {'name': 'Property 1', 'total_area': 30},
            {'name': 'Property 2', 'total_area': 45},
        ])

    def test_action_sell(self):
        self.properties[0].action_sold_property()
        self.assertRecordValues(self.properties[0], [
            {'name': 'Property 1', 'state': 'sold'}
        ])

        with self.assertRaises(UserError):
            self.properties[1].action_sold_property()

    def test_offer_on_sold_property(self):
        self.properties[0].action_sold_property()

        with self.assertRaises(UserError):
            self.env['estate.property.offer'].create({
                'property_id': self.properties[0].id, 'price': 200000, 'partner_id': self.partner_3.id
            })

    def test_sell_without_accepted_offer(self):
        with self.assertRaises(UserError):
            self.properties[1].action_sold_property()

        # def test_garden_uncheck_resets_fields(self):
        #     property_1 = self.properties[0]
        #     property_1.garden = True
        #     property_1._onchange_garden()
        #     self.assertEqual(property_1.garden_area, 10)
        #     self.assertEqual(property_1.garden_orientation, 'North')
        #
        #     property_1.garden = False
        #     property_1._onchange_garden()
        #     self.assertEqual(property_1.garden_area, 0)
        #     self.assertEqual(property_1.garden_orientation, '')

        def test_garden_uncheck_resets_fields(self):
            property_1 = self.properties[0]

            with Form(property_1) as property_form:
                property_form.garden = True
            self.assertEqual(property_1.garden_area, 10)
            self.assertEqual(property_1.garden_orientation, 'North')

            with Form(property_1) as property_form:
                property_form.garden = False
            self.assertEqual(property_1.garden_area, 0)
            self.assertEqual(property_1.garden_orientation, '')
