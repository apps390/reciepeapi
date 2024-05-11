from django.shortcuts import render
from rest_framework import viewsets, status
from recipe.models import recipe, review
from django.contrib.auth.models import User
from recipe.serializers import reciepeserializers, userserializers, reviewserializers
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class recipeviewsets(viewsets.ModelViewSet):
    queryset = recipe.objects.all()
    serializer_class = reciepeserializers


class userviewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializers
class createreview(viewsets.ModelViewSet):
    queryset = review.objects.all()
    serializer_class = reviewserializers
class retrievereview(APIView):
    def get_object(self,pk):
        try:
            return recipe.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
    def get(self,request,pk):
        k=self.get_object(pk)
        sr=review.objects.filter(recipe_name=k)
        ser=reviewserializers(sr,many=True)
        return Response(ser.data)


class Cuisinefilter(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        query=self.request.query_params.get('cuisine')
        R=recipe.objects.filter(cuisine=query)
        res=reciepeserializers(R,many=True)
        return Response(res.data)
class mealfilter(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        query=self.request.query_params.get('meal')
        R=recipe.objects.filter(meal_type=query)
        res=reciepeserializers(R,many=True)
        return Response(res.data)
class ingredientfilter(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        query=self.request.query_params.get('ing')
        R=recipe.objects.filter(recipe_ingredients=query)
        res=reciepeserializers(R,many=True)
        return Response(res.data)
class userlogout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'message':'logoutSuccessfully'})








