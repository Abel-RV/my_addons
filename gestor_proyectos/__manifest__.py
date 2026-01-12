{
    'name': "Gestor de Proyectos Abel",

    'summary': "Planificar, organizar y hacer seguimiento de proyectos, trabajos y actividades",

    'description': """
Módulo para gestionar proyectos desglosados en trabajos y actividades.
Permite seguimiento de estados, fechas, responsables y progreso.
    """,

    'author': "Alumno 2º DAM",
    'website': "https://example.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/proyecto_view.xml',
        'views/trabajo_view.xml',
        'views/actividad_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'icon': 'static/description/icon.png',
}

