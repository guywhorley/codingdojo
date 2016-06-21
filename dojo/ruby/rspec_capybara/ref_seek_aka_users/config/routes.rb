Rails.application.routes.draw do

  resources :sessions, only: [:new, :create, :destroy]
  resources :users

  # You can have the root of your site routed with "root"
  root 'sessions#new' 


end
