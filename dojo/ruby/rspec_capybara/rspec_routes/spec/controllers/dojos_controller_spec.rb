require 'rails_helper'

RSpec.describe DojosController, type: :controller do

    # The routing tests only test that rails actually routes correctly.
    # In other words, the controller methods are not checked. In fact, the
    # controller methods do not even need to be defined for the routing tests.

    describe "routing" do

        it "routes to root" do
            expect(:get => "/").to route_to(:controller => "dojos", :action => "index")
        end

        it "routes to 'hello" do
            expect(:get => "/hello").to route_to(:controller => "dojos", :action => "world")
        end

        it "routes to 'ninjas'" do
            expect(:get => "/ninjas").to route_to(:controller => "dojos", :action => "ninjas")
        end

        # EXAMPLES OF TESTING RESTFUL ROUTES
        # Note: the syntax for 'expect' is recognized without error.

        # xit "routes to #new" do
        #     expect(:get => "/dojos/new").to route_to(:controller => "dojos", :action => "new")
        # end
        # xit "routes to #show" do
        #   expect(:get => "/dojos/1").to route_to(:controller => "dojos", :action => "show", :id => "1")
        # end
        # xit "routes to #edit" do
        #   expect(:get => "/dojos/1/edit").to route_to(:controller => "dojos", :action => "edit", :id => "1")
        # end
        # xit "routes to #create" do
        #   expect(:post => "/dojos").to route_to(:controller => "dojos", :action => "create")
        # end
        # xit "routes to #update" do
        #   expect(:patch => "/dojos/1").to route_to(:controller => "dojos", :action => "update", :id => "1")
        # end
        # xit "routes to #destroy" do
        #   expect(:delete => "/dojos/1").to route_to(:controller => "dojos", :action => "destroy", :id => "1")
        # end
    end

end
