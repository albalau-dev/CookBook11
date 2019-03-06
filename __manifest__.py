{
    'name': 'Library Book',
    'summary': 'Module My_module',
    'description': """Long description""",
    'author': "albarracinlau",
    'license': "AGPL-3",
    'website': "http://www.lauraweb.com.ve",
    'category': 'Uncategorized',
    'version': '11.0.1.0.0',
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
                             },
    
    'depends': [
        'base',
               ],
    'data': [
        'views/library_book.xml',
        'security/groups.xml',
        'security/ir.model.access.csv'
            ],
}