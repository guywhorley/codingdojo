from system.core.router import routes

routes['default_controller'] = 'Products'
routes['/show/<int:id>'] = 'Products#show'
routes['/edit/<int:id>'] = 'Products#edit'
routes['POST']['/create'] = 'Products#process_create'
routes['/create'] = 'Products#new'
routes['POST']['/destroy'] = 'Products#destroy'
routes['POST']['/update'] = 'Products#update'
