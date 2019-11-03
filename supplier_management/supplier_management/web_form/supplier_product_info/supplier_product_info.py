from __future__ import unicode_literals
import frappe
from erpnext.controllers.website_list_for_contact import get_customers_suppliers
from frappe import _

def get_context(context):
	# do your magic here
	pass


def set_supplier():
	print('================================================')
	if hasattr(frappe.local, "cookie_manager"):
		customers, suppliers = get_customers_suppliers('Supplier Product Info', frappe.session.user)
		print(frappe.session.user,'-------------------------------------------------------------------------------')
		frappe.local.cookie_manager.set_cookie("supplier", suppliers[0])