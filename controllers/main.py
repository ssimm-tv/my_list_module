from odoo import http
from odoo.http import request
import logging
import json
from werkzeug.wrappers import Response

_logger = logging.getLogger(__name__)

class MyListController(http.Controller):

    @http.route('/my_main_page', type='http', auth='public', website=True)
    def my_main_page(self, **kw):
        """
        Renders the main page template with static content.
        The dynamic list container is initially empty.
        """
        _logger.info("Accessing /my_main_page (GET request)")
        return request.render('my_list_module.my_main_page_template', {
            'page_title': "My Main Page",
        })


    @http.route('/my_list_content', type='json', auth='public', website=True)
    def get_list_content(self, **kw):
        """
        Generates the list data, renders only the snippet template,
        and returns the HTML content as a JSON response.
        """
        _logger.info("Accessing /my_list_content (JSON POST request)")

        # Look at the request params
        #request_params = kw.get('params', kw)
        #_logger.info("Request parameters (from 'params' or kw): %s", request_params)

        try:

            my_items = [
                {'name': 'Asynchronous Item A', 'id': 1},
                {'name': 'Asynchronous Item B', 'id': 2},
                {'name': 'Asynchronous Item C', 'id': 3},
                {'name': 'Asynchronous Item D', 'id': 4},
            ]
            
            # Render the snippet template with the list data.
            html_content = request.env['ir.ui.view']._render_template(
                "my_list_module.my_list_snippet", {
                    'items_for_list': my_items,
                }
            )

            # Convert the rendered content to a standard string, just for debugging
            html_content = str(html_content)
            _logger.info("Rendered HTML content: %s", html_content)
            
            # Odoo's 'json' route type automatically handles the response
            # serialization, so we just return the dictionary.
            return {'html': html_content}

        except Exception as e:
            _logger.error("Error during list content rendering: %s", str(e))
            return {'error': str(e)}