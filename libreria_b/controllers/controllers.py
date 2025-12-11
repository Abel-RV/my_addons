# from odoo import http


# class LibreriaB(http.Controller):
#     @http.route('/libreria_b/libreria_b', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libreria_b/libreria_b/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('libreria_b.listing', {
#             'root': '/libreria_b/libreria_b',
#             'objects': http.request.env['libreria_b.libreria_b'].search([]),
#         })

#     @http.route('/libreria_b/libreria_b/objects/<model("libreria_b.libreria_b"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libreria_b.object', {
#             'object': obj
#         })

