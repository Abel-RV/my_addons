# from odoo import http


# class GestorProyectos(http.Controller):
#     @http.route('/gestor_proyectos/gestor_proyectos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestor_proyectos/gestor_proyectos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestor_proyectos.listing', {
#             'root': '/gestor_proyectos/gestor_proyectos',
#             'objects': http.request.env['gestor_proyectos.gestor_proyectos'].search([]),
#         })

#     @http.route('/gestor_proyectos/gestor_proyectos/objects/<model("gestor_proyectos.gestor_proyectos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestor_proyectos.object', {
#             'object': obj
#         })

