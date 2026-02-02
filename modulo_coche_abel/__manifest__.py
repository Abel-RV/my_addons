{
    'name': "modulo_coche_abel",

    'summary': "Modulo de herencia para gestión de coches, para la asignatura de SGE",

    'description': """
Modulo de herencia para la gestión de coches, que permite crear y gestionar diferentes modelos de coches, así como sus características y funcionalidades.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',             
        'views/vehiculos_view.xml',
        'views/multa_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

