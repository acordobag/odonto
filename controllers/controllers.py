# -*- coding: utf-8 -*-
from odoo import http

# class Odonto(http.Controller):
#     @http.route('/odonto/odonto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odonto/odonto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odonto.listing', {
#             'root': '/odonto/odonto',
#             'objects': http.request.env['odonto.odonto'].search([]),
#         })

#     @http.route('/odonto/odonto/objects/<model("odonto.odonto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odonto.object', {
#             'object': obj
#         })