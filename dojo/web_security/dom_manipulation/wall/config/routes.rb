Rails.application.routes.draw do

  get "wall/register" => "wall#register"

  get "wall/login" => "wall#login"

  post "wall/login" => "wall#dologin"

  post "wall/users/create" => "wall#create"

  get "wall/logout" => "wall#logout"

  get "wall" => "wall#index"

  post "wall" => "wall#create"

  post "/message" => "wall#create_message"

  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  root 'wall#index'

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

end
