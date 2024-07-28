import json

from odoo import http
from odoo.http import request, Response


class EstatePropertyController(http.Controller):

    @http.route('/estate/properties', type='http', auth='user', methods=['GET'], csrf=True)
    def get_properties(self):
        properties = request.env['estate.property'].search([])
        property_list = []
        for property in properties:
            property_list.append({
                'name': property.name,
                'living_area': property.living_area,
                'total_area': property.total_area,
                'state': property.state,
                # add other fields as necessary
            })
        return Response(json.dumps({'properties': property_list}), content_type='application/json', status=200)

    @http.route('/estate/properties/demo', type='http', auth='public', methods=['GET'], csrf=True)
    def get_properties_demo(self):
        property_list = [{'name': 'Property {}'.format(property_id), 'living_area': property_id * 10,
                          'state': 'sold' if property_id % 2 == 0 else 'new'} for property_id in range(3)]

        return Response(json.dumps({'properties': property_list}), content_type='application/json', status=200)

    @http.route('/estate/properties/opendemo', type='http', auth='none', methods=['GET'], csrf=True)
    def get_properties_open_demo(self):
        property_list = [{'name': 'Property {}'.format(property_id), 'living_area': property_id * 10,
                          'state': 'sold' if property_id % 2 == 0 else 'new'} for property_id in range(3)]

        return Response(json.dumps({'properties': property_list}), content_type='application/json', status=200)

    @http.route('/estate/properties/opendemolist', type='http', auth='none', methods=['GET'], csrf=True)
    def get_properties_open_demo_list(self):
        property_list = [{'name': 'Property {}'.format(property_id), 'living_area': property_id * 10,
                          'state': 'sold' if property_id % 2 == 0 else 'new'} for property_id in range(3)]

        # try json no-named datas : list
        return Response(json.dumps(property_list), content_type='application/json', status=200)

class RestrictEstateProperty(EstatePropertyController):

    @http.route(auth='user')
    def get_properties_demo(self):
        return super().get_properties_demo()
