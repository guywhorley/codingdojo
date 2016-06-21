require 'rails_helper'

RSpec.describe "Ninjas Routing", type: :routing do

    it "#new" do
        expect(:get => "/").to route_to(:controller => "ninjas", :action => "new")
    end

    it "#create routes to /success" do
        expect(:post => '/ninjas').to route_to(:controller => "ninjas", :action => "create")
    end

end
