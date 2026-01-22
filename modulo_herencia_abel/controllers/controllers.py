# from odoo import http


# class ModuloHerenciaAbel(http.Controller):
#     @http.route('/modulo_herencia_abel/modulo_herencia_abel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_herencia_abel/modulo_herencia_abel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_herencia_abel.listing', {
#             'root': '/modulo_herencia_abel/modulo_herencia_abel',
#             'objects': http.request.env['modulo_herencia_abel.modulo_herencia_abel'].search([]),
#         })

#     @http.route('/modulo_herencia_abel/modulo_herencia_abel/objects/<model("modulo_herencia_abel.modulo_herencia_abel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_herencia_abel.object', {
#             'object': obj
#         })

