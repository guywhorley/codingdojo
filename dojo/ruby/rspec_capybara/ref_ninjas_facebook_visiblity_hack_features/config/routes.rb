Rails.application.routes.draw do

  get  '/' => 'ninjas#new'
  post '/ninjas'     => 'ninjas#create'
  get  '/success'   => 'ninjas#success'
  root 'ninjas/#new'

end
