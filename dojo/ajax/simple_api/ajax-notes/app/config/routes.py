from system.core.router import routes

routes['default_controller'] = 'Posts'
routes['/posts/index_json'] = 'Posts#index_json'
routes['/posts/index_html'] = 'Posts#index_html'
# routes['POST']['/posts/create'] = 'Posts#create'
