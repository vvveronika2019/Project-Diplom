from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

import json
from .models import Cart
from .models import Good
from .models import Goodcategory
from .models import Goodcounty
from .models import Goodparameter
from .models import Goodtheme
from .models import Review
from .models import Sell
from .models import Sellstatus
from .models import User
from .models import Sysdiagrams
from .models import Newscolibri
from . serializers import CartSerializer
from . serializers import GoodSerializer
from . serializers import GoodcategorySerializer
from . serializers import GoodcountySerializer
from . serializers import GoodparameterSerializer
from . serializers import GoodthemeSerializer
from . serializers import ReviewSerializer
from . serializers import SellSerializer
from . serializers import SellstatusSerializer
from . serializers import UserSerializer
from . serializers import SysdiagramsSerializer
from . serializers import NewsColibriSerializer

last_login = []


class GoodView(generics.RetrieveAPIView):
    queryset = Good.objects.all()
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GoodSerializer(queryset, many=True)
        return Response(serializer.data)

class NewColibriView(generics.RetrieveAPIView):
    queryset = Newscolibri.objects.all()
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = NewsColibriSerializer(queryset, many=True)
        return Response(serializer.data)


class GoodcategoryView(generics.RetrieveAPIView):
    queryset = Goodcategory.objects.all()
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GoodcategorySerializer(queryset, many=True)
        return Response(serializer.data)

class GoodcountyView(generics.RetrieveAPIView):
    queryset = Goodcounty.objects.all()
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GoodcountySerializer(queryset, many=True)
        return Response(serializer.data)

class GoodthemeView(generics.RetrieveAPIView):
    queryset = Goodtheme.objects.all()
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GoodthemeSerializer(queryset, many=True)
        return Response(serializer.data)
        
class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    def get(self, request, *args, **kwargs):
        
        try:
            print (last_login[-1])
            return Response(last_login[-1])

        except IndexError:
            return Response(json.dumps({'login': 'False'}))


class ReviewGETView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

class ReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def post(self, request, *args, **kwargs):
        print("create review")
        return self.create(request, *args, **kwargs) 

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        print("create user")
        return self.create(request, *args, **kwargs)  

class UserPostView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        
        login = request.data['useremail']
        password = request.data['userpassword']
        

        queryset = self.get_queryset()
       
        data = UserSerializer(queryset, many=True).data

        last_login.clear ()
        for i in range (len (data)):
            if login == data[i]['useremail'] and data[i]['userpassword'] == password:
                last_login.append (data[i])
                return (Response(data[i]))
            else:
                continue
            
        return Response(json.dumps({'login': 'False'}))

class CartGETView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    def get(self, request, *args, **kwargs):
        current_user_products = []
        queryset = self.get_queryset()
        serializer = CartSerializer(queryset, many=True)
        
        try:
            for i, string in enumerate (Cart.objects.values()):
                if string['cartuserlastname'] == last_login[-1]['userlastname'] and string['cartuserfirstname'] == last_login[-1]['username'] and  string['cartusepatronyc'] == last_login[-1]['userpatronimys'] and string['cartuseremail'] == last_login[-1]['useremail']:
                    current_user_products.append (string)
             
        except IndexError:
            return Response(json.dumps ({
            "current_user_products": "none"
        }))
        
        return Response(json.dumps ({
            "current_user_products": current_user_products
        }, ensure_ascii=False))
       

class CartPOSTView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def post(self, request, *args, **kwargs):
        try:
            request.data.update({
                'cartuserlastname': last_login[-1]['userlastname'],
                'cartuserfirstname': last_login[-1]['username'],
                'cartusepatronyc': last_login[-1]['userpatronimys'],
                'cartuseradress': last_login[-1]['userbaseadress'],
                'cartuseremail': last_login[-1]['useremail'],
                'cartuserphone':last_login[-1]['userphone']
                })

            return self.create(request, *args, **kwargs) 

        except:
            return Response(json.dumps({'cart_add': 'false'}))


class LogoutView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        last_login.clear()
        return Response(json.dumps({'logout': 'success'}))

class CartDELETEView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def post(self, request, *args, **kwargs):
        print ('>', request.data)
        id = request.data['0']['cartid']
        print ("ID", id)
    
        try:
            Cart.objects.filter(cartid=id).delete()
            return (Response(json.dumps({"status":"True"})))
        except:
            return (Response(json.dumps({"status":"False"})))

class SellView(generics.RetrieveAPIView):
    queryset = Sell.objects.all()
    def get(self, request, *args, **kwargs):
        current_user_sell = []
        queryset = self.get_queryset()
        serializer = SellSerializer(queryset, many=True)
        try:
            for i, string in enumerate (Sell.objects.values()):
                if string['selluserlastname'] == last_login[-1]['userlastname'] and string['selluserfirstname'] == last_login[-1]['username'] and  string['sellusepatronyc'] == last_login[-1]['userpatronimys'] and string['selluseremail'] == last_login[-1]['useremail']:
                    current_user_sell.append (string)
             
        except IndexError:
            return Response(json.dumps ({
            "current_user_sell": ""
        }))
        
        return Response(json.dumps ({
            "current_user_sell": current_user_sell
        }, ensure_ascii=False))

class SellStatusView(generics.RetrieveAPIView):
    queryset = Sellstatus.objects.all()
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SellstatusSerializer(queryset, many=True)
        return Response(serializer.data)


class SellPOSTView(generics.CreateAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    def post(self, request, *args, **kwargs):
        print(request.data, '<<<<<<<<<<<')
        # try:
        request.data.update({
                'selluserlastname': last_login[-1]['userlastname'],
                'selluserfirstname': last_login[-1]['username'],
                'sellusepatronyc': last_login[-1]['userpatronimys'],
                'selluseradress': last_login[-1]['userbaseadress'],
                'selluseremail': last_login[-1]['useremail'],
                'selluserphone':last_login[-1]['userphone'],
                'sellstatus': 1,
                })
        print(request.data, '11111111111')

        return self.create(request, *args, **kwargs) 

        # except:
            # return Response(json.dumps({'sell_add': 'false'}))