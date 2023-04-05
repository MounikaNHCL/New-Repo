{
    'name': 'Side Bar Testing',
    'summary': '''Side Bar Testing''',
    'description': '''Side Bar Testing''',
    'version': '14.1.0.1.1',
    'images': ['static/description/icon.png'],
    'company': '',
    'author': 'Mounika',
    'website': "",
    'depends': ['base', 'web'],
    'data': [
     ],
    'assets': {
        'web.assets_backend': [
            # 'side_bar_custom/static/src/views/asserts.xml',
            'side_bar_custom/static/src/scss/navbar.scss'
        ]},

    'application': False,
    "auto_install": False,
    'installable': True,
    "external_dependencies": {"python": [], "bin": []},
}
