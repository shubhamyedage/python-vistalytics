# from treelib import Tree, Node
# import main.common.constant as con
#
# tree = Tree()
#
#
# def get_string(s):
#     return s.replace(" ", "_").replace("'", "")
#
#
# def compare(a, b):
#     return (a * b) > 0
#
#
# def get_tree():
#     tree.create_node(con.TOTAL_CASH_FLOW, get_string(con.TOTAL_CASH_FLOW), data={'val': 1, con.TAGGED: False})
#     tree.create_node(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES,
#                      get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES), parent=get_string(con.TOTAL_CASH_FLOW),
#                      data={'val': 1})
#     tree.create_node(con.NET_INCOME, get_string(con.NET_INCOME),
#                      parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES), data={'val': -1})
#     tree.create_node(con.DEPRECIATION_AND_AMORTIZATION, get_string(con.DEPRECIATION_AND_AMORTIZATION),
#                      parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES), data={'val': 1})
#     tree.create_node(con.STOCK_BASED_COMPENSATION, get_string(con.STOCK_BASED_COMPENSATION),
#                      parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES), data={'val': 1})
#     tree.create_node(con.DEFERRED_INCOME_TAXES, get_string(con.DEFERRED_INCOME_TAXES),
#                      parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES), data={'val': 1})
#     tree.create_node(con.ACCOUNTS_RECEIVABLE, get_string(con.ACCOUNTS_RECEIVABLE),
#                      parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES), data={'val': 1})
#     tree.create_node(con.INVENTORY, get_string(con.INVENTORY),
#                      parent=get_string(con.NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES), data={'val': 1})
#
#     tree.create_node(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES, get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES),
#                      parent=get_string(con.TOTAL_CASH_FLOW), data={'val': -1})
#     tree.create_node(con.INVESTMENTS_IN_PROPERTY_PLANT_AND_EQUIPMENT,
#                      get_string(con.INVESTMENTS_IN_PROPERTY_PLANT_AND_EQUIPMENT),
#                      parent=get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES), data={'val': -1})
#     tree.create_node(con.PURCHASES_OF_INVESTMENTS, get_string(con.PURCHASES_OF_INVESTMENTS),
#                      parent=get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES), data={'val': -1})
#     tree.create_node(con.SALES_MATURITIES_OF_INVESTMENTS, get_string(con.SALES_MATURITIES_OF_INVESTMENTS),
#                      parent=get_string(con.NET_CASH_USED_FOR_INVESTING_ACTIVITIES), data={'val': 1})
#
#     tree.create_node(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES,
#                      get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES), parent=get_string(con.TOTAL_CASH_FLOW),
#                      data={'val': 1})
#     tree.create_node(con.DIVIDEND_PAID, get_string(con.DIVIDEND_PAID),
#                      parent=get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES), data={'val': 1})
#     tree.create_node(con.COMMON_STOCK_ISSUED, get_string(con.COMMON_STOCK_ISSUED),
#                      parent=get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES), data={'val': 1})
#     tree.create_node(con.COMMON_STOCK_REPURCHASED, get_string(con.COMMON_STOCK_REPURCHASED),
#                      parent=get_string(con.NET_CASH_PROVIDED_BY_FINANCING_ACTIVITIES), data={'val': 1})
#
#     return
#
#
# # def get_tree():
# #     tree.create_node(con.REVENUE, get_string(con.REVENUE), data={'val': 1, con.TAGGED: False})
# #     tree.create_node(con.COST_OF_REVENUE, get_string(con.COST_OF_REVENUE), parent=get_string(con.REVENUE),
# #                      data={'val': 1})
# #     tree.create_node(con.GROSS_PROFIT, get_string(con.GROSS_PROFIT), parent=get_string(con.REVENUE), data={'val': -1})
# #     tree.create_node(con.TOTAL_OPERATING_EXPENSES, get_string(con.TOTAL_OPERATING_EXPENSES),
# #                      parent=get_string(con.GROSS_PROFIT), data={'val': -1})
# #     tree.create_node(con.RESEARCH_AND_DEVELOPMENT, get_string(con.RESEARCH_AND_DEVELOPMENT),
# #                      parent=get_string(con.TOTAL_OPERATING_EXPENSES), data={'val': -1})
# #     tree.create_node(con.SALES_GENERAL_AND_ADMINISTRATIVE, get_string(con.SALES_GENERAL_AND_ADMINISTRATIVE),
# #                      parent=get_string(con.TOTAL_OPERATING_EXPENSES), data={'val': 1})
# #     tree.create_node(con.OPERATING_INCOME, get_string(con.OPERATING_INCOME), parent=get_string(con.GROSS_PROFIT),
# #                      data={'val': 1})
# #     tree.create_node(con.INTEREST_EXPENSE, get_string(con.INTEREST_EXPENSE), parent=get_string(con.OPERATING_INCOME),
# #                      data={'val': 1})
# #     tree.create_node(con.INCOME_BEFORE_TAXES, get_string(con.INCOME_BEFORE_TAXES),
# #                      parent=get_string(con.OPERATING_INCOME), data={'val': 1})
# #     tree.create_node(con.PROVISION_FOR_INCOME_TAXES, get_string(con.PROVISION_FOR_INCOME_TAXES),
# #                      parent=get_string(con.INCOME_BEFORE_TAXES), data={'val': 1})
# #     tree.create_node(con.NET_INCOME, get_string(con.NET_INCOME), parent=get_string(con.INCOME_BEFORE_TAXES),
# #                      data={'val': -1})
# #     return
#
#
# def func():
#     node_id_list = []
#     for node in tree.all_nodes():
#         if node.is_root():
#             print('Root Node: ' + node.identifier)
#         else:
#             parent_node = tree.parent(node.identifier)
#             if not compare(node.data['val'], parent_node.data['val']) and not parent_node.data[con.TAGGED]:
#                 node.data[con.TAGGED] = True
#                 # print('###### Tagged Nodes: ' + node.identifier + ' data: ' + str(node.data))
#                 node_id_list.append(node.identifier)
#             else:
#                 node.data[con.TAGGED] = False
#                 # print('Un-tagged Nodes: ' + node.identifier + ' data: ' + str(node.data))
#     return node_id_list
#
# #
# # def print_text(node):
# #     root_node = tree.get_node(tree.root)
# #     growth_indicator = "UP" if root_node.data['val'] > 0 else "DOWN"
# #     parent_node = tree.parent(node.identifier)
# #     print("##############################################")
# #     print("While root index " + root_node.identifier + " and parent index " + parent_node.identifier +
# #           "has gone " + growth_indicator + " by " + root_node.data['val'] + " and " + parent_node.data['val'] +
# #           " respectively, index " + node.identifier + " is trending in OPPOSITE direction by " + node.data['val'])
# #     print("##############################################")
# #
# #     return
#
#
# def get_node_list_to_print(sub_tree):
#     node_id_list = []
#     sub_tree_root_node = sub_tree.get_node(sub_tree.root)
#     for node in sub_tree.all_nodes():
#         tree.get_node(node.identifier).data[con.TAGGED] = False
#         if not node.is_root() and compare(node.data['val'], sub_tree_root_node.data['val']):
#             node_id_list.append(node.identifier)
#
#     return node_id_list
#
#
# def deep_compare_and_print(node_id_list):
#     for node_id in node_id_list:
#         if tree.get_node(node_id).data[con.TAGGED]:
#             sub_tree = tree.subtree(node_id)
#             if sub_tree.depth() > 0:
#                 print_id_list = get_node_list_to_print(sub_tree)
#                 print(print_id_list)
#             else:
#                 print(node_id)
#
#     return
#
# get_tree()
# print(tree)
# node_id_list = func()
#
# deep_compare_and_print(node_id_list)
# print('##########################################################################################################\n\n')