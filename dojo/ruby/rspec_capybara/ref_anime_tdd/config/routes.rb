Rails.application.routes.draw do

  get '/animes' => 'animes#index'

  get '/animes/index'

  get '/animes/new'

  post '/animes' => 'animes#create'

  get '/animes/:id' => 'animes#show'

  get '/animes/:id/edit' => 'animes#edit'

  delete '/animes/:id' => 'animes#destroy'

  # You can have the root of your site routed with "root"
  root 'animes#index'

end
