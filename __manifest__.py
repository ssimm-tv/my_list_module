{
    'name': "My List Module",
    'version': '1.0',
    'summary': 'Demonstrates asynchronous list loading with AJAX.',
    'description': """
        This module provides a main web page and an embedded list that is loaded
        asynchronously via an AJAX call to a separate controller.
    """,
    'author': "Your Name",
    'category': 'Website',
    'depends': ['web', 'website'],
    'data': [
        'views/template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'my_list_module/static/src/js/main.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}