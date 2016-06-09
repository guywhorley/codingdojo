require 'spec_helper'
require 'appletree'

describe AppleTree do

    #   L E T   /  S U B J E C T
    subject { AppleTree.new }
    # let(:custom) { TestObject.new("myTest", 99) }

    #  T E S T S

    describe '+Setters-Getters' do
        it '- allows reading of tree :height'  do
            expect(subject.height).to eq(0)
        end
        it '- allows reading of tree :age' do
            expect(subject.age).to eq(0)
        end
        it '- allows reading of tree :appleCount' do
            expect(subject.appleCount).to eq(0)
        end
    end

    describe '#YearGoneBy' do  # test instance methods
        it '- ages the tree by one year' do
            subject.yearGoneBy
            expect(subject.age).to eq(1)
        end
        it '- causes the tree to grow by 10 feet each year for 10 years' do
            subject.yearGoneBy
            expect(subject.height).to eq(10)

            for i in 2..10
                subject.yearGoneBy
            end
            expect(subject.height).to eq(100)
        end
        it '- tree does not grow after 10 years' do
            for i in 1..10
                subject.yearGoneBy
            end
            expect(subject.height).to eq(100)

            subject.yearGoneBy
            expect(subject.height).to eq(100)
        end
        it '- will only grow apples between years 3 and 10 inclusive' do
            for i in 1..4
                subject.yearGoneBy
            end
            expect(subject.appleCount).to eq(400)

            for i in 5..10
                subject.yearGoneBy
            end
            expect(subject.appleCount).to eq(1000)
        end
        it '- will not grow apples before year four' do
            for i in 1..3
                subject.yearGoneBy
            end
            expect(subject.appleCount).to eq(0)

            subject.yearGoneBy # validate apples do grow in year 4
            expect(subject.appleCount).to eq(400)
        end

        it '- no apples will grown on tree after ten years.' do
            for i in 1..10
                subject.yearGoneBy
            end
            expect(subject.appleCount).to eq(1000)

            subject.yearGoneBy
            expect(subject.appleCount).to eq(0)
        end
    end
    describe '#PickApples' do
        it '- takes all the apples off of the tree' do
            for i in 1..4
                subject.yearGoneBy
            end
            expect(subject.appleCount).to eq(400)
            subject.pickApples
            expect(subject.appleCount).to eq(0)
        end
    end
end
