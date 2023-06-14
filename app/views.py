from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet

from app.models import *

from app.seraliazers import *

from rest_framework.response import Response

class ProductCurdVS(ViewSet):
    def list(self,request):
        PQS=Product.objects.all()
        PSD=Product_seralizer(PQS,many=True)
        return Response(PSD.data)
    
    
    def create(self,request):
        PSD=Product_seralizer(data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({'Sucess':"create a new data"})
        else:
            return Response({'Failed':'Cannot create new data'})
        
        
    def retrieve(self,request,pk):
        PQS=Product.objects.get(pk=pk)
        PSD=Product_seralizer(PQS)
        return Response(PSD.data)
    
    def update(self,request,pk):
        PQS=Product.objects.get(pk=pk)
        PSU=Product_seralizer(PQS,data=request.data)
        if PSU.is_valid():
            PSU.save()
            return Response({'sucess':'Update sucessfully'})
        else:
            return Response({'Failed':'not updated'})
        
    def partial_update(self,request,pk):
        PQS=Product.objects.get(pk=pk)
        PPU=Product_seralizer(PQS,data=request.data,partial=True)
        if PPU.is_valid():
            PPU.save()
            return Response({'sucess':'Partially updated:'})
        else:
            return Response({'failed':'Not UPDATED'})
        
    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'sucess':'data is deleted sucessfully'})
        
        
        