# -*- coding: utf-8 -*-
from odoo import http

# class SpecialPie(http.Controller):
#     @http.route('/special_pie/special_pie/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/special_pie/special_pie/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('special_pie.listing', {
#             'root': '/special_pie/special_pie',
#             'objects': http.request.env['special_pie.special_pie'].search([]),
#         })

#     @http.route('/special_pie/special_pie/objects/<model("special_pie.special_pie"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('special_pie.object', {
#             'object': obj
#         })