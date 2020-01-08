frappe.ready(function () {
	$('input[type=search]').on('keydown', (e) => {
		if (e.keyCode === 13) {
		  // Enter
		  const value = e.target.value;
		  if (value) {
			console.log(window.location.protocol+'//'+ window.location.host+'/all-products?search=' + e.target.value)
			window.location.href=window.location.protocol+'//'+ window.location.host+'/all-products?search=' + e.target.value;
		  } else {
			// window.location.search = '';
		  }
		}
	  });
	});    