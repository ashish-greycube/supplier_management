# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "supplier_management"
app_title = "Supplier Management"
app_publisher = "GreyCube Technologies"
app_description = "Tool to help onboarding of Suppliers"
app_icon = "octicon octicon-gist-secret"
app_color = "#03fcb1"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = ["/assets/supplier_management/css/catalysts88_081223d2.css"] 
# app_include_js = "/assets/supplier_management/js/supplier_management.js"

# include js, css files in header of web template
web_include_css =  ["/assets/css/catalysts88_081223d2.css"] 
# web_include_js = "/assets/supplier_management/js/supplier_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "supplier_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------
on_session_creation = ["supplier_management.supplier_management.web_form.supplier_product_info.supplier_product_info.set_supplier"]
# before_install = "supplier_management.install.before_install"
# after_install = "supplier_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "supplier_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"supplier_management.tasks.all"
# 	],
# 	"daily": [
# 		"supplier_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"supplier_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"supplier_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"supplier_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "supplier_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "supplier_management.event.get_events"
# }

