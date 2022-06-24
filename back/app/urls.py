from django.urls import path
from . views import GoodView
from . views import GoodcategoryView
from . views import GoodcountyView
from . views import GoodthemeView
from . views import ReviewView
from . views import UserView
from . views import ReviewGETView
from . views import CreateUserView
from . views import UserPostView
from . views import NewColibriView
from . views import CartPOSTView
from . views import CartGETView
from . views import SellPOSTView
from . views import LogoutView
from . views import CartDELETEView
from . views import SellView
from . views import SellStatusView
urlpatterns = [
    path('good/', GoodView.as_view(), name='good_view'),
    path('news/', NewColibriView.as_view(), name='news'),
    path('good/category', GoodcategoryView.as_view(), name='category_view'),
    path('good/country', GoodcountyView.as_view(), name='country_view'),
    path('good/theme', GoodthemeView.as_view(), name='theme_view'),
    path('feedback/review', ReviewView.as_view(), name='review_view'),
    path('feedback/reviewGET', ReviewGETView.as_view(), name='review_view'),
    path('user/', UserView.as_view(), name='user_view'),
    path('user/create', CreateUserView.as_view(), name='create_user'),
    path('user/login', UserPostView.as_view(), name='post_user'),
    path('cart/get', CartGETView.as_view(), name='get_cart'),
    path('cart/post', CartPOSTView.as_view(), name='post_cart'),
    path('user/logout', LogoutView.as_view(), name='logout_user'),
    path('cart/delete', CartDELETEView.as_view(), name='cart_delete'),
    path('sell/', SellView.as_view(), name='sell'),
    path('sell/status', SellStatusView.as_view(), name='sell_status'),
    path('sell/post', SellPOSTView.as_view(), name='post_sell'),
]