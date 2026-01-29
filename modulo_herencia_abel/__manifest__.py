{
    'name': "modulo_herencia_abel",

    'summary': "Modulo de gestión de multas utilizando herencia para el modulo Sistemas de Gestión Empresarial",

    'description': """
        Módulo de Odoo para gestionar multas en una empresa, utilizando herencia para extender las funcionalidades del módulo Sistemas de Gestión Empresarial.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # Dependencias necesarias
    'depends': ['base', 'hr'],

    # Archivos a cargar
    'data': [
        'security/ir.model.access.csv',  # Descomentado para cargar permisos de acceso
        'views/hr_employee_views.xml',   # Agregado
        'views/multa_views.xml',         # Agregado
        'views/templates.xml',
    ],
    # Solo en modo demostración
    'demo': [
        'demo/demo.xml',
    ],
}