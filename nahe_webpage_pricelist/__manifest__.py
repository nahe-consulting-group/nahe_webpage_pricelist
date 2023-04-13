# -*- coding: utf-8 -*-
{
    'name': "nahe_webpage_pricelist",

    'summary': """
        Pagina para sitio web que contenga la informacion de productos y precios depende el tipo de lista de precio  """,

    'description': """
        Pagina para sitio web que contenga la informacion de productos y precios depende el tipo de lista de precio. 
        Si el cliente loguea con su usuario mayorista que incluya esa lista de precios en este caso la lista mayorista es la de ID 3 
        Eso se edita en el codigo de la vista.
    """,

    'author': "Nähe Consulting Group",
    'website': "http://www.nahe.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
