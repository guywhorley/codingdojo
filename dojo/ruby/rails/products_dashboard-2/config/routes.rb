Rails.application.routes.draw do

  # PRODUCTS
  get '/products' => 'products#index'

  get 'products/new' => 'products#new'

  post 'products' => 'products#create'

  get 'products/:id' => 'products#show'

  get 'products/:id/edit' => 'products#edit'

  patch 'products/:id' => 'products#update'

  delete 'products/:id' => 'products#destroy'

  # COMMENTS
  get '/comments' => 'comments#index'


  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  # root 'welcome#index'

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase
end
