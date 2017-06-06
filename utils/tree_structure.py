from treelib import Tree
import common.constant as con


class TreeStructure(object):

    def __init__(self):
        self.report_choices = {1: con.BALANCE_STATEMENTS, 2: con.CASH_FLOW_STATEMENTS}
        self.tree = Tree()

    def get_string(self, s):
        return s.replace(" ", "_").replace("'", "").upper()

    def get_income_tree(self):
        self.tree.create_node(con.REVENUE, self.get_string(con.REVENUE), data={con.TAGGED: False})
        self.tree.create_node(con.COST_OF_REVENUE, self.get_string(con.COST_OF_REVENUE),
                              parent=self.get_string(con.REVENUE))
        self.tree.create_node(con.GROSS_PROFIT, self.get_string(con.GROSS_PROFIT), parent=self.get_string(con.REVENUE))
        self.tree.create_node(con.TOTAL_OPERATING_EXPENSES, self.get_string(con.TOTAL_OPERATING_EXPENSES),
                              parent=self.get_string(con.GROSS_PROFIT))
        self.tree.create_node(con.RESEARCH_AND_DEVELOPMENT, self.get_string(con.RESEARCH_AND_DEVELOPMENT),
                              parent=self.get_string(con.TOTAL_OPERATING_EXPENSES))
        self.tree.create_node(con.SALES_GENERAL_AND_ADMINISTRATIVE,
                              self.get_string(con.SALES_GENERAL_AND_ADMINISTRATIVE),
                              parent=self.get_string(con.TOTAL_OPERATING_EXPENSES))
        self.tree.create_node(con.OPERATING_INCOME, self.get_string(con.OPERATING_INCOME),
                              parent=self.get_string(con.GROSS_PROFIT))
        self.tree.create_node(con.INTEREST_EXPENSE, self.get_string(con.INTEREST_EXPENSE),
                              parent=self.get_string(con.OPERATING_INCOME))
        self.tree.create_node(con.INCOME_BEFORE_TAXES, self.get_string(con.INCOME_BEFORE_TAXES),
                              parent=self.get_string(con.OPERATING_INCOME))
        self.tree.create_node(con.PROVISION_FOR_INCOME_TAXES, self.get_string(con.PROVISION_FOR_INCOME_TAXES),
                              parent=self.get_string(con.INCOME_BEFORE_TAXES))
        self.tree.create_node(con.NET_INCOME, self.get_string(con.NET_INCOME),
                              parent=self.get_string(con.INCOME_BEFORE_TAXES))

    def get_balance_tree(self):
        self.tree.create_node(con.TOTAL_ASSETS, self.get_string(con.TOTAL_ASSETS), data={con.TAGGED: False})

        self.tree.create_node(con.TOTAL_CURRENT_ASSETS, self.get_string(con.TOTAL_CURRENT_ASSETS),
                              parent=self.get_string(con.TOTAL_ASSETS))
        self.tree.create_node(con.CASH_AND_CASH_EQUIVALENTS, self.get_string(con.CASH_AND_CASH_EQUIVALENTS),
                              parent=self.get_string(con.TOTAL_CURRENT_ASSETS))
        self.tree.create_node(con.RECEIVABLES, self.get_string(con.RECEIVABLES),
                              parent=self.get_string(con.TOTAL_CURRENT_ASSETS))
        self.tree.create_node(con.OTHER_CURRENT_ASSETS, self.get_string(con.OTHER_CURRENT_ASSETS),
                              parent=self.get_string(con.TOTAL_CURRENT_ASSETS))
        self.tree.create_node(con.NET_PROPERTY_PLANT_AND_EQUIPMENT,
                              self.get_string(con.NET_PROPERTY_PLANT_AND_EQUIPMENT),
                              parent=self.get_string(con.TOTAL_ASSETS))
        self.tree.create_node(con.GOODWILL, self.get_string(con.GOODWILL), parent=self.get_string(con.TOTAL_ASSETS))
        self.tree.create_node(con.TOTAL_NON_CURRENT_ASSETS, self.get_string(con.TOTAL_NON_CURRENT_ASSETS),
                              parent=self.get_string(con.TOTAL_ASSETS))

        self.tree.create_node(con.TOTAL_ASSETS, self.get_string(con.TOTAL_LIABILITIES_AND_STOCKHOLDERS_EQUITY),
                              parent=self.get_string(con.TOTAL_ASSETS))
        self.tree.create_node(con.TOTAL_LIABILITIES, self.get_string(con.TOTAL_LIABILITIES),
                              parent=self.get_string(con.TOTAL_LIABILITIES_AND_STOCKHOLDERS_EQUITY))
        self.tree.create_node(con.ACCOUNTS_PAYABLE, self.get_string(con.ACCOUNTS_PAYABLE),
                              parent=self.get_string(con.TOTAL_LIABILITIES))
        self.tree.create_node(con.ACCRUED_LIABILITIES, self.get_string(con.ACCRUED_LIABILITIES),
                              parent=self.get_string(con.TOTAL_LIABILITIES))
        self.tree.create_node(con.SHORT_TERM_DEBT, self.get_string(con.SHORT_TERM_DEBT),
                              parent=self.get_string(con.TOTAL_LIABILITIES))
        self.tree.create_node(con.TOTAL_CURRENT_LIABILITIES, self.get_string(con.TOTAL_CURRENT_LIABILITIES),
                              parent=self.get_string(con.TOTAL_LIABILITIES))
        self.tree.create_node(con.LONG_TERM_DEBT, self.get_string(con.LONG_TERM_DEBT),
                              parent=self.get_string(con.TOTAL_LIABILITIES))
        self.tree.create_node(con.OTHER_LONG_TERM_LIABILITIES, self.get_string(con.OTHER_LONG_TERM_LIABILITIES),
                              parent=self.get_string(con.TOTAL_LIABILITIES))

        self.tree.create_node(con.TOTAL_EQUITY, self.get_string(con.TOTAL_EQUITY),
                              parent=self.get_string(con.TOTAL_LIABILITIES_AND_STOCKHOLDERS_EQUITY))

    def get_cash_flow_tree(self):
        self.tree.create_node(con.TOTAL_CASH_FLOW, self.get_string(con.TOTAL_CASH_FLOW))
        self.tree.create_node(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES,
                              self.get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES),
                              parent=self.get_string(con.TOTAL_CASH_FLOW))
        self.tree.create_node(con.NET_INCOME, self.get_string(con.NET_INCOME),
                              parent=self.get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))
        self.tree.create_node(con.DEPRECIATION_AND_AMORTIZATION, self.get_string(con.DEPRECIATION_AND_AMORTIZATION),
                              parent=self.get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))
        self.tree.create_node(con.STOCK_BASED_COMPENSATION, self.get_string(con.STOCK_BASED_COMPENSATION),
                              parent=self.get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))
        self.tree.create_node(con.DEFERRED_INCOME_TAXES, self.get_string(con.DEFERRED_INCOME_TAXES),
                              parent=self.get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))
        self.tree.create_node(con.ACCOUNTS_RECEIVABLE, self.get_string(con.ACCOUNTS_RECEIVABLE),
                              parent=self.get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))
        self.tree.create_node(con.INVENTORY, self.get_string(con.INVENTORY),
                              parent=self.get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))

        self.tree.create_node(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES,
                              self.get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES),
                              parent=self.get_string(con.TOTAL_CASH_FLOW))
        self.tree.create_node(con.INVESTMENTS_IN_PROPERTY_PLANT_AND_EQUIPMENT,
                              self.get_string(con.INVESTMENTS_IN_PROPERTY_PLANT_AND_EQUIPMENT),
                              parent=self.get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES))
        self.tree.create_node(con.PURCHASES_OF_INVESTMENTS, self.get_string(con.PURCHASES_OF_INVESTMENTS),
                              parent=self.get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES))
        self.tree.create_node(con.SALES_MATURITIES_OF_INVESTMENTS, self.get_string(con.SALES_MATURITIES_OF_INVESTMENTS),
                              parent=self.get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES))

        self.tree.create_node(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES,
                              self.get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES),
                              parent=self.get_string(con.TOTAL_CASH_FLOW))
        self.tree.create_node(con.DIVIDEND_PAID, self.get_string(con.DIVIDEND_PAID),
                              parent=self.get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES))
        self.tree.create_node(con.COMMON_STOCK_ISSUED, self.get_string(con.COMMON_STOCK_ISSUED),
                              parent=self.get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES))
        self.tree.create_node(con.COMMON_STOCK_REPURCHASED, self.get_string(con.COMMON_STOCK_REPURCHASED),
                              parent=self.get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES))
