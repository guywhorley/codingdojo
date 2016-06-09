require 'spec_helper'
require 'bankaccount_v2'

describe BankAccount do

    ################
    #  LET/DOUBLES
    ################
    subject { BankAccount.new(1000.00, 5000.00, 2.5) }

    ###################
    # MY TESTS HERE...
    ###################

    describe 'attributes' do  # test getters, setters
        it 'has default values' do
            expect(subject.checkingBalance).to eq(1000.00)
            expect(subject.savingsBalance).to eq(5000.00)
            expect(subject.totalNumberOfAccounts).to eq(1)
            expect(subject.accountInformation).to match(/Interest Rate:/)
        end
        it 'allows reading on :accountNumber' do
            accountNumber = subject.accountNumber.to_s
            expect(accountNumber).to match(/\d{8}/)
        end
        it 'allows reading on :checkingBalance' do
            expect(subject.checkingBalance).to eq(1000.00)
        end
        it 'allows reading on :savingsBalance' do
            expect(subject.savingsBalance).to eq(5000.00)
        end

    end

    describe '# deposit Into Checking' do
        it 'allows depositing valid funds into checking' do
            subject.depositIntoChecking(150.50)
            expect(subject.checkingBalance).to eq(1150.50)
        end
        it "doesn't allow depositing negative funds into checking" do
            subject.depositIntoChecking(-150.00)
            expect(subject.checkingBalance).to eq(1000.00)
        end
    end

    describe '# deposit Into Savings' do
        it 'allows depositing valid funds into savings' do
            subject.depositIntoSavings(150.50)
            expect(subject.savingsBalance).to eq(5150.50)
        end
        it "doesn't allow depositing negative funds into savings" do
            subject.depositIntoSavings(-150.00)
            expect(subject.savingsBalance).to eq(5000.00)
        end
    end

    describe '# withdraw From Checking' do
        it "allows taking of sufficient funds." do
            subject.withdrawFromChecking(500.00)
            expect(subject.checkingBalance).to eq(500.00)
        end
        it "prevents overdraws" do
            expect { subject.withdrawFromChecking(2000.00) }.to raise_error("Insufficent Funds!")
        end
        it "prevents negative withdrawl" do
            subject.withdrawFromChecking(-4000.00)
            expect(subject.checkingBalance).not_to eq(5000.00)
            expect(subject.checkingBalance).to eq(1000.00)
        end
    end

    describe '# withdraw From Savings' do
        it "allows taking of sufficient funds." do
            subject.withdrawFromSavings(500.00)
            expect(subject.savingsBalance).to eq(4500.00)
        end
        it "prevents overdraws" do
        expect { subject.withdrawFromSavings(10000.00) }.to raise_error("Insufficent Funds!")
        end
        it "prevents negative withdrawl" do
            subject.withdrawFromSavings(-5000.00)
            expect(subject.savingsBalance).not_to eq(10000.00)
            expect(subject.savingsBalance).to eq(5000.00)
        end
    end

    describe '# view Account Total' do
        it 'allows viewing account information' do
            expect {subject.viewAccountTotal}.to output(/Account:/).to_stdout
            expect {subject.viewAccountTotal}.to output(/Total Funds:/).to_stdout
        end
    end

    describe '# account Information' do
        it "allows viewing of acount information" do
            info = subject.accountInformation
            expect(info).to match(/Account:/)
            expect(info).to match(/Total-Funds:/)
            expect(info).to match(/Checking Balance:/)
            expect(info).to match(/Savings Balance:/)
            expect(info).to match(/Interest Rate:/)
        end

        



    end
end
