# from odoo import http


# class PruebaAbel(http.Controller):
#     @http.route('/prueba_abel/prueba_abel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueba_abel/prueba_abel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueba_abel.listing', {
#             'root': '/prueba_abel/prueba_abel',
#             'objects': http.request.env['prueba_abel.prueba_abel'].search([]),
#         })

#     @http.route('/prueba_abel/prueba_abel/objects/<model("prueba_abel.prueba_abel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba_abel.object', {
#             'object': obj
#         })

