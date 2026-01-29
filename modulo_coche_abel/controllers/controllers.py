# from odoo import http


# class ModuloCocheAbel(http.Controller):
#     @http.route('/modulo_coche_abel/modulo_coche_abel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_coche_abel/modulo_coche_abel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_coche_abel.listing', {
#             'root': '/modulo_coche_abel/modulo_coche_abel',
#             'objects': http.request.env['modulo_coche_abel.modulo_coche_abel'].search([]),
#         })

#     @http.route('/modulo_coche_abel/modulo_coche_abel/objects/<model("modulo_coche_abel.modulo_coche_abel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_coche_abel.object', {
#             'object': obj
#         })

