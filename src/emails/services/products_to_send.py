from product.models import Product, WriteReview
from users.models import User
from datetime import datetime, timedelta


email_list = []

user_list = User.objects.filter(last_login__lte = (datetime.today() - timedelta(days=30) ))

for user in user_list:
    email_list.append(user.email)


product_list = Product.objects.filter(created_at__gte = (datetime.today() - timedelta(days=30) ))

product_and_rating = []
for product in product_list:
    rating_count = WriteReview.objects.filter(product=product).count()
    product_and_rating.append((product, rating_count))


sorted_product_and_rating = sorted(
    product_and_rating,
    key=lambda t: t[1]
)[::-1]

products_to_send = []

for i in range(2):
    products_to_send.append(sorted_product_and_rating[i][0])