require 'rails_helper'

describe Mathdojo, :type => :model do

    # subject
    subject do
        m = Mathdojo.new
    end

    # tests
    it "multiplies flat integers" do
        expect(subject.add(5).multiply_by_sum_of(1,2,3,4,5).result).to eq(75)
    end

    it "multiplies array integers" do
        expect(subject.add(5).multiply_by_sum_of([1,2,3,4,5]).result).to eq(75)
    end

    it "multiplies mixed flat-and-array integers" do
        expect(subject.add(5).multiply_by_sum_of(5,[1,2,3,4,5]).result).to eq(100)
    end


    it "multiplies flat floats" do
        expect(subject.add(5).multiply_by_sum_of(1.0,2.0,3.0,4.0,5.0).result).to eq(75.0)
    end

    it "multiplies array floats" do
        expect(subject.add(5.0).multiply_by_sum_of([1.0,2.0,3.0,4.0,5.0]).result).to eq(75.0)
    end

    it "multiplies mixed flat-and-array floats" do
        expect(subject.add(5.0).multiply_by_sum_of(5.0,[1.0,2.0,3.0,4.0,5.0]).result).to eq(100.0)
    end

    it "multiplies mixed flat-and-array mixed int-and-float" do
            expect(subject.add(5).multiply_by_sum_of(5,[1.0,2,3.0,4,5.0]).result).to eq(100.0)
    end

    it "resets" do
        expect(subject.add(5).multiply_by_sum_of(3.0, 4, 5).subtract(2,5).reset.add(2).result).to eq(3)
    end



    it "adds integer flat values" do
        expect(subject.add(1,2,3).result).to eq(6)
    end

    it "adds integer array values" do
        expect(subject.add([1,2,3]).result).to eq(6)
    end

    it "adds integer mixed flat-and-array values" do
        expect(subject.add(1,2,[3,4,5]).result).to eq(15)
    end

    it "adds float flat values" do
        expect(subject.add(1.0,2.0,3.0).result).to eq(6.0)
    end

    it "adds float array values" do
        expect(subject.add([1.0, 2.0, 3.0]).result).to eq(6.0)
    end

    it "adds float flat-and-array values" do
        expect(subject.add(1.0, 2.0,[3.0,4.0,5.0]).result).to eq(15.0)
    end

    it "subtracts integer flat values" do
        expect(subject.subtract(1,2,3).result).to eq(-6)
    end

    it "subtracts integer array values" do
        expect(subject.subtract([1,2,3]).result).to eq(-6)
    end

    it "subtracts integer mixed flat-and-array values" do
        expect(subject.subtract(1,2,[3,4,5]).result).to eq(-15)
    end

    it "subtracts float flat values" do
        expect(subject.subtract(1.0,2.0,3.0).result).to eq(-6.0)
    end

    it "subtracts float array values" do
        expect(subject.subtract([1.0, 2.0, 3.0]).result).to eq(-6.0)
    end

    it "subtracts float mixed flat-and-array values" do
        expect(subject.subtract(1.0, 2.0,[3.0,4.0,5.0]).result).to eq(-15.0)
    end

end
