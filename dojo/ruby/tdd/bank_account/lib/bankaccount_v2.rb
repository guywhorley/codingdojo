# name: bankaccount_v2.rb
# auth: Guy Whorley
# desc: this class represents a bank account. The various methods model
#   activities that an account holder can perform.
# history:
#   06-07-2016  gcw - created v2, refactored private methods to user ruby shortcut if syntax

class BankAccount

    @@numberOfAccounts = 0
    attr_reader :accountNumber, :checkingBalance, :savingsBalance

    # Public: instantiate new bank account
    #
    # checkingBalance - the beginning balance for the checking account.
    # savingsBalance - the beginning balance for the savings account.
    # rate - interest rate for savings account.
    def initialize(checkingBalance, savingsBalance, rate=1.9)
        @checkingBalance = preventNegativeAmount(checkingBalance)
        @savingsBalance = preventNegativeAmount(savingsBalance)
        @interestRate = preventNegativeAmount(rate)
        @accountNumber = generateAccountNumber()
        @@numberOfAccounts += 1
        self
    end

    # Public: deposit amount into checking account.
    # amount - nonzero funds.
    def depositIntoChecking(amount)
        # puts "Deposit $#{amount} into checking."
        @checkingBalance += preventNegativeAmount(amount)
        # puts "New checking balance: $#{@checkingBalance}\n\n"
        self
    end

    # Public: deposit amount into savings account.
    # amount - nonzero funds.
    def depositIntoSavings(amount)
        # puts "Deposit $#{amount} into savings."
        @savingsBalance += preventNegativeAmount(amount)
        # puts "New savings balance: $#{@savingsBalance}\n\n"
        self
    end

    # Public: withdraw amount from checking. If amount is greater than balance, withdraw $0.
    # amount - size of funds to take from checking.
    def withdrawFromChecking(amount)
        # puts "Withdrawing $#{amount} from checking."
        amount = preventNegativeAmount(amount)
        @checkingBalance -= preventAccountOverdraw(amount, "checking")
        # puts "New checking balance: $#{@checkingBalance}\n\n"
        self
    end

    # Public: withdraw amount from savings. If amount is greater than balance, withdraw $0.
    # amount - size of funds to take from savings.
    def withdrawFromSavings(amount)
        # puts "Withdrawing $#{amount} from savings."
        amount = preventNegativeAmount(amount)
        @savingsBalance -= preventAccountOverdraw(amount, "savings")
        # puts "New savings balance: $#{@savingsBalance}\n\n"
        self
    end

    # Public: display total number of accounts.
    def totalNumberOfAccounts
        return @@numberOfAccounts
    end

    # Public: display the account total: sum of checking and savings.
    def viewAccountTotal
        puts "Account: ##{accountNumber}, Total Funds: $#{@checkingBalance + @savingsBalance}"
        self
    end

    # Public: display account information for this account.
    def accountInformation
        info = "ACCOUNT INFORMATION\n"
        info += "Account:          ##{@accountNumber}\n"
        info += "Total-Funds:      $#{@checkingBalance + @savingsBalance}\n"
        info += "Checking Balance: $#{@checkingBalance}\n"
        info += "Savings Balance:  $#{@savingsBalance}\n"
        info += "Interest Rate:    #{@interestRate}%"
        # puts info
        return info
    end

    private

        # Private: check amount against account balance. If amount is
        # greater, then reduce amount to zero to prevent overdraw.
        #
        # amount - proposed amount to withdraw.
        # accountType - 'checking' or 'savings'
        def preventAccountOverdraw(amount, accountType)

            if (accountType=='checking')
                # puts "Insufficient fund!" if (amount > @checkingBalance)
                raise "Insufficent Funds!" if (amount > @checkingBalance)
                return amount
            elsif (accountType=='savings')
                # puts "Insufficent funds!" if (amount > @savingsBalance)
                raise "Insufficent Funds!" if (amount > @savingsBalance)
                return amount
            else
                puts "Account type unknown!"
                return 0
            end #end if
        end

        # Private: check that value is positive. If so, return value. If not, return 0.
        def preventNegativeAmount(value)
            return 0 if (value < 0)
            return value
        end

        # Private: Generate random account number.
        def generateAccountNumber
            prng = Random.new
            return prng.rand(99999999)
        end
end #class
