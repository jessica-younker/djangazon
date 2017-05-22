from django.shortcuts import render

from website.models.product_model import Product
from django.contrib.auth.models import User

def product_detail(request, product_id):
	"""
	This function renders the request using:
		- TEMPLATE: product/detail.html
		- OBJECT: The Product that was clicked on is the data that this view returns

	Author: Will Sims
	"""

	template_name = 'product/detail.html'
	product = Product.objects.get(id__exact=product_id)

	# Get seller object
	seller = User.objects.get(id__exact=product.id)
	seller_name = " ".join([seller.first_name.title(), seller.last_name.title()])

	# This part can probably be refactored, I just wanted to get something that works merged in
	# (manually extracting the product data and creating a list of tuples is probably resource expensive)
	new_product = [("Seller", seller_name), ("Description", product.description), ("Price", product.price), ("Quantity", product.quantity)]

	
	return render(request, template_name, {'object_to_display': new_product, "page_title":product.title})