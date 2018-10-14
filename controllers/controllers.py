# -*- coding: utf-8 -*-
from odoo import http

# class Bka(http.Controller):
#     @http.route('/bka/bka/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bka/bka/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bka.listing', {
#             'root': '/bka/bka',
#             'objects': http.request.env['bka.bka'].search([]),
#         })

#     @http.route('/bka/bka/objects/<model("bka.bka"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bka.object', {
#             'object': obj
#         })