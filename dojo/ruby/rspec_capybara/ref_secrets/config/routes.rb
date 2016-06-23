Rails.application.routes.draw do
  get 'secrets/index'

  resources :sessions, only: [:new, :create, :destroy]
  resources :users
  resources :secrets, only: [:index, :create, :destroy]

  # For whatever reason, 'rources :secrets' doesn't give me the POST ... secrets/destroy route,
  # thus, I am explictly adding it.
  post '/secrets/:id' => 'secrets#destroy'

  # You can have the root of your site routed with "root"
  root 'sessions#new'


end
