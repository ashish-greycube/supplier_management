frappe.ready(function() {
	// bind events here
	setTimeout(() => {
		var supplier=frappe.get_cookie('supplier');
		frappe.web_form.set_value('supplier',supplier);
		// $('input[data-fieldname="supplier"]').val('Walmart')
		frappe.web_form.set_field_property('supplier', 'read_only', 1);
	}, 1000);

})