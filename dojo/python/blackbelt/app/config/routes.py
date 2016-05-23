from system.core.router import routes

routes['default_controller'] = 'Quotes'

# PROCESS REGISTRATION AND LOGIN
routes['POST']['/process_login'] = 'Quotes#process_login'
routes['POST']['/process_registration'] = 'Quotes#process_registration'

# ADD QUOTE, ADD FAVORITE
routes['POST']['/process_add_quote'] = 'Quotes#process_add_quote'
routes['/add_favorite_quote/<int:id>/<int:q_id>'] = 'Quotes#add_favorite_quote'

# REMOVE FAVORITE
routes['/remove_favorite_quote/<int:id>/<int:q_id>'] = 'Quotes#remove_favorite_quote'

# SHOW USER DETAILS
routes['/user/<int:id>'] = 'Quotes#show_user_details'

# LOGOUT
routes['/logout'] = 'Quotes#logout'
