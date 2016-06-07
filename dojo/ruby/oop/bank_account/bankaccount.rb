# name: bankaccount.rb
# auth: Guy Whorley
# desc: this class represents a bank account. The various methods model
#   activities that an account holder can perform.

class BankAccount

    @@numberOfAccounts = 0
    attr_reader :accountNumber, :checkingBalance, :savingsBalance, :numberOfAccounts

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
        puts "Deposit $#{amount} into checking."
        @checkingBalance += preventNegativeAmount(amount)
        puts "New checking balance: $#{@checkingBalance}\n\n"
        self
    end

    # Public: deposit amount into savings account.
    # amount - nonzero funds.
    def depositIntoSavings(amount)
        puts "Deposit $#{amount} into savings."
        @savingsBalance += preventNegativeAmount(amount)
        puts "New savings balance: $#{@savingsBalance}\n\n"
        self
    end

    # Public: withdraw amount from checking. If amount is greater than balance, withdraw $0.
    # amount - size of funds to take from checking.
    def withdrawFromChecking(amount)
        puts "Withdrawing $#{amount} from checking."
        @checkingBalance -= preventAccountOverdraw(amount, "checking")
        puts "New checking balance: $#{@checkingBalance}\n\n"
        self
    end

    # Public: withdraw amount from savings. If amount is greater than balance, withdraw $0.
    # amount - size of funds to take from savings.
    def withdrawFromSavings(amount)
        puts "Withdrawing $#{amount} from savings."
        @savingsBalance -= preventAccountOverdraw(amount, "savings")
        puts "New savings balance: $#{@savingsBalance}\n\n"
        self
    end

    # Public: display the account total: sum of checking and savings.
    def viewAccountTotal
        puts "****************************************"
        puts "Account: ##{accountNumber}, Total Funds: $#{@checkingBalance + @savingsBalance}"
        puts "****************************************\n\n"
        self
    end

    # Public: display account information for this account.
    def accountInformation
        puts "ACCOUNT INFORMATION"
        puts "Account:          ##{@accountNumber}"
        puts "Total-Funds:      $#{@checkingBalance + @savingsBalance}"
        puts "Checking Balance: $#{@checkingBalance}"
        puts "Savings Balance:  $#{@savingsBalance}"
        puts "Interest Rate:    #{@interestRate}%\n\n"
        self
    end

    private

        # Private: check amount against account balance. If amount is
        # greater, then reduce amount to zero to prevent overdraw.
        #
        # amount - proposed amount to withdraw.
        # accountType - 'checking' or 'savings'
        def preventAccountOverdraw(amount, accountType)
            if (accountType=='checking')
                if (amount > @checkingBalance)
                    puts "Insufficient funds!"
                    return 0
                else
                    return amount
                end #end checking
            elsif (accountType=='savings')
                if (amount > @savingsBalance)
                    puts "Insufficient funds!"
                    return 0
                else
                    return amount
                end #end savings
            else
                puts "Account type unknown!"
                return 0
            end #end if
        end

        # Private: check that value is positive. If so, return value. If not, return 0.
        def preventNegativeAmount(value)
            if (value < 0)
                return 0
            else
                return value
            end #if
        end
        # Private: Generate random account number.

        def generateAccountNumber
            prng = Random.new
            return prng.rand(99999999)
        end
end #class


# TEST
a1 = BankAccount.new(1000, 2000, 5.5)
a1.viewAccountTotal
a1.accountInformation
puts "Checking balance: $" + a1.checkingBalance.to_s
a1.depositIntoChecking(200).withdrawFromChecking(100)
puts "Savings Balance: $" + a1.savingsBalance.to_s
a1.depositIntoSavings(300)
a1.withdrawFromSavings(150).withdrawFromChecking(5000).withdrawFromSavings(10000)
a1.viewAccountTotal
