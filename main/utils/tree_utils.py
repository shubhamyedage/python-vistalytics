from treelib import Tree, Node
import main.common.constant as con

report_choices = {1: con.BALANCE_STATEMENTS, 2: con.CASH_FLOW_STATEMENTS}
tree = Tree()


def get_string(s):
    return s.replace(" ", "_").replace("'", "").lower()


def get_income_statement_tree_structure():
    tree.create_node(con.REVENUE, get_string(con.REVENUE), data={con.TAGGED: False})
    tree.create_node(con.COST_OF_REVENUE, get_string(con.COST_OF_REVENUE), parent=get_string(con.REVENUE))
    tree.create_node(con.GROSS_PROFIT, get_string(con.GROSS_PROFIT), parent=get_string(con.REVENUE))
    tree.create_node(con.TOTAL_OPERATING_EXPENSES, get_string(con.TOTAL_OPERATING_EXPENSES),
                     parent=get_string(con.GROSS_PROFIT))
    tree.create_node(con.RESEARCH_AND_DEVELOPMENT, get_string(con.RESEARCH_AND_DEVELOPMENT),
                     parent=get_string(con.TOTAL_OPERATING_EXPENSES))
    tree.create_node(con.SALES_GENERAL_AND_ADMINISTRATIVE, get_string(con.SALES_GENERAL_AND_ADMINISTRATIVE),
                     parent=get_string(con.TOTAL_OPERATING_EXPENSES))
    tree.create_node(con.OPERATING_INCOME, get_string(con.OPERATING_INCOME), parent=get_string(con.GROSS_PROFIT))
    tree.create_node(con.INTEREST_EXPENSE, get_string(con.INTEREST_EXPENSE), parent=get_string(con.OPERATING_INCOME))
    tree.create_node(con.INCOME_BEFORE_TAXES, get_string(con.INCOME_BEFORE_TAXES),
                     parent=get_string(con.OPERATING_INCOME))
    tree.create_node(con.PROVISION_FOR_INCOME_TAXES, get_string(con.PROVISION_FOR_INCOME_TAXES),
                     parent=get_string(con.INCOME_BEFORE_TAXES))
    tree.create_node(con.NET_INCOME, get_string(con.NET_INCOME), parent=get_string(con.INCOME_BEFORE_TAXES))
    return tree


def get_balance_statement_tree_structure():
    tree.create_node(con.TOTAL_ASSETS, get_string(con.TOTAL_ASSETS), data={con.TAGGED: False})

    tree.create_node(con.TOTAL_CURRENT_ASSETS, get_string(con.TOTAL_CURRENT_ASSETS), parent=get_string(con.TOTAL_ASSETS))
    tree.create_node(con.CASH_AND_CASH_EQUIVALENTS, get_string(con.CASH_AND_CASH_EQUIVALENTS),
                     parent=get_string(con.TOTAL_CURRENT_ASSETS))
    tree.create_node(con.RECEIVABLES, get_string(con.RECEIVABLES), parent=get_string(con.TOTAL_CURRENT_ASSETS))
    tree.create_node(con.OTHER_CURRENT_ASSETS, get_string(con.OTHER_CURRENT_ASSETS),
                     parent=get_string(con.TOTAL_CURRENT_ASSETS))
    tree.create_node(con.NET_PROPERTY_PLANT_AND_EQUIPMENT, get_string(con.NET_PROPERTY_PLANT_AND_EQUIPMENT),
                     parent=get_string(con.TOTAL_ASSETS))
    tree.create_node(con.GOODWILL, get_string(con.GOODWILL), parent=get_string(con.TOTAL_ASSETS))
    tree.create_node(con.TOTAL_NON_CURRENT_ASSETS, get_string(con.TOTAL_NON_CURRENT_ASSETS), parent=get_string(con.TOTAL_ASSETS))

    tree.create_node(con.TOTAL_ASSETS, get_string(con.TOTAL_LIABILITIES_AND_STOCKHOLDERS_EQUITY), parent=get_string(con.TOTAL_ASSETS))
    tree.create_node(con.TOTAL_LIABILITIES, get_string(con.TOTAL_LIABILITIES),
                     parent=get_string(con.TOTAL_LIABILITIES_AND_STOCKHOLDERS_EQUITY))
    tree.create_node(con.ACCOUNTS_PAYABLE, get_string(con.ACCOUNTS_PAYABLE), parent=get_string(con.TOTAL_LIABILITIES))
    tree.create_node(con.ACCRUED_LIABILITIES, get_string(con.ACCRUED_LIABILITIES),
                     parent=get_string(con.TOTAL_LIABILITIES))
    tree.create_node(con.SHORT_TERM_DEBT, get_string(con.SHORT_TERM_DEBT), parent=get_string(con.TOTAL_LIABILITIES))
    tree.create_node(con.TOTAL_CURRENT_LIABILITIES, get_string(con.TOTAL_CURRENT_LIABILITIES),
                     parent=get_string(con.TOTAL_LIABILITIES))
    tree.create_node(con.LONG_TERM_DEBT, get_string(con.LONG_TERM_DEBT), parent=get_string(con.TOTAL_LIABILITIES))
    tree.create_node(con.OTHER_LONG_TERM_LIABILITIES, get_string(con.OTHER_LONG_TERM_LIABILITIES),
                     parent=get_string(con.TOTAL_LIABILITIES))

    tree.create_node(con.TOTAL_EQUITY, get_string(con.TOTAL_EQUITY),
                     parent=get_string(con.TOTAL_LIABILITIES_AND_STOCKHOLDERS_EQUITY))

    return tree


def get_cash_flow_statement():
    tree.create_node(con.TOTAL_CASH_FLOW, get_string(con.TOTAL_CASH_FLOW))
    tree.create_node(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES,
                     get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES), parent=get_string(con.TOTAL_CASH_FLOW))
    tree.create_node(con.NET_INCOME, get_string(con.NET_INCOME),
                     parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))
    tree.create_node(con.DEPRECIATION_AND_AMORTIZATION, get_string(con.DEPRECIATION_AND_AMORTIZATION),
                     parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))
    tree.create_node(con.STOCK_BASED_COMPENSATION, get_string(con.STOCK_BASED_COMPENSATION),
                     parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))
    tree.create_node(con.DEFERRED_INCOME_TAXES, get_string(con.DEFERRED_INCOME_TAXES),
                     parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))
    tree.create_node(con.ACCOUNTS_RECEIVABLE, get_string(con.ACCOUNTS_RECEIVABLE),
                     parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))
    tree.create_node(con.INVENTORY, get_string(con.INVENTORY), parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES))

    tree.create_node(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES, get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES),
                     parent=get_string(con.TOTAL_CASH_FLOW))
    tree.create_node(con.INVESTMENTS_IN_PROPERTY_PLANT_AND_EQUIPMENT,
                     get_string(con.INVESTMENTS_IN_PROPERTY_PLANT_AND_EQUIPMENT),
                     parent=get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES))
    tree.create_node(con.PURCHASES_OF_INVESTMENTS, get_string(con.PURCHASES_OF_INVESTMENTS),
                     parent=get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES))
    tree.create_node(con.SALES_MATURITIES_OF_INVESTMENTS, get_string(con.SALES_MATURITIES_OF_INVESTMENTS),
                     parent=get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES))

    tree.create_node(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES,
                     get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES), parent=get_string(con.TOTAL_CASH_FLOW))
    tree.create_node(con.DIVIDEND_PAID, get_string(con.DIVIDEND_PAID),
                     parent=get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES))
    tree.create_node(con.COMMON_STOCK_ISSUED, get_string(con.COMMON_STOCK_ISSUED),
                     parent=get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES))
    tree.create_node(con.COMMON_STOCK_REPURCHASED, get_string(con.COMMON_STOCK_REPURCHASED),
                     parent=get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES))

    return tree
