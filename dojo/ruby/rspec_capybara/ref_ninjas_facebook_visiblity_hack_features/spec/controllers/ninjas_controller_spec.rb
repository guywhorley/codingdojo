require 'rails_helper'

RSpec.describe NinjasController, type: :controller do

    subject { post :create, :ninja => { :ninja_name => 'danielsan', :ninja_description => "wax on" }}

    context "GET /ninjas/new" do
        it "#new returns status code 200" do
            get :new
            expect(response.status).to eq(200)
        end
    end

    context "POST /ninjas ---> valid data" do
        it "returns a status code 200" do
            post :create
            expect(response.status).to eq(200)
        end
    end
end
