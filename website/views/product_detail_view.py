from django.shortcuts import render

from website.models.product_model import Product
from website.models.order_model import Order
from website.models.payment_type_model import PaymentType
from website.models.product_order_model import ProductOrder
from django.contrib.auth.models import User


def product_detail(request, product_id=None):
	"""
	This function renders the request using:
		- TEMPLATE: product/detail.html
		- OBJECT: The Product that was clicked on is the data that this view 
			returns

	Author: Will Sims
	"""
	
	if request.method == 'GET':

		template_name = 'product/detail.html'
		product = Product.objects.get(pk=product_id)

		# Get seller object
		seller = User.objects.get(pk=product.seller_id)
		seller_name = " ".join([seller.first_name.title(), seller.last_name.\
			title()])

		# This part can probably be refactored, I just wanted to get something 
		# that works merged in (manually extracting the product data and 
		# creating a list of tuples is probably resource expensive)
		new_product = [("Seller", seller_name), ("Description", \
			product.description), ("Price", product.price), ("Quantity", \
			product.quantity), ("Date Listed", product.date_added)]

		
		return render(request, template_name, {'object_to_display': \
			new_product, "page_title":product.title, "type": "product", \
			"product_id": product.pk})

	elif request.method == 'POST':
		order = Order.objects.filter(user_id=request.user.id, payment_type_id=None)
		po = ProductOrder(
			order_id = order.latest('id').id,
			product_id = product_id
		)
		po.save()
		template_name = 'product/success.html'
		
		return render(request, template_name, {})
