from system.core.router import routes

routes['default_controller'] = 'Quotes'
routes['/quotes/index_json'] = 'Quotes#index_json'
routes['/quotes/index_html'] = 'Quotes#index_html'
# routes['POST']['/quotes/create'] = 'Quotes#create'
