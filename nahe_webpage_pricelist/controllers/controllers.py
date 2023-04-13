# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class NaheWebpagePricelist(http.Controller):

    @http.route('/lista', type="http", auth="public", website=True)
    def listado(self, page=1, search=None, **kw):
        print("Execution Here.........................")
        todos_partners_id = request.env['res.partner'].sudo().search([])
        partner_id_logeado = request.env.user.partner_id

        # Filtrar productos según la búsqueda
        domain = []
        if search:
            domain = [('name', 'ilike', search)]

        # Manejar la paginación
        limit = 50
        offset = (int(page) - 1) * limit
        count = request.env['product.template'].sudo().search_count(domain)
        totalPages = (count // limit) + (1 if count % limit else 0)

        productos = request.env['product.template'].sudo().search(domain, limit=limit, offset=offset)

        return http.request.render('nahe_webpage_pricelist.webpage_pricelist', {
            'partner_id': partner_id_logeado,
            'productos': productos,
            'search': search,
            'page': int(page),
            'totalPages': totalPages,
        })
