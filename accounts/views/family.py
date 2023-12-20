from accounts.models.users import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView,CreateAPIView
from accounts.models.family import Spouse, Parents, Kids
from accounts.serializers.family import SpouseSerializer, ParentsSerializer, KidsSerializer
from rest_framework.permissions import IsAuthenticated

class GetSpouseAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Spouse.objects.all()
    serializer_class = SpouseSerializer

class CreateSpouseAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        dob = request.data.get('dob')
        doa = request.data.get('doa')

        try:
            if name and dob and doa:
                user = request.user
                spouse = Spouse.objects.create(name=name, doa=doa, user=user, dob = dob)
                instance = SpouseSerializer(spouse)
                return Response(instance.data)
            
            else:
                return Response({'error':"Mention all details of the Spouse"})
        
        except Spouse.DoesNotExist:
             return Response({'error':"Spouse is not available"})
        
class UpdateSpouseAPIView(CreateAPIView):
    def post(self, request, id, *args, **kwargs):
        name = request.data.get('name')
        dob = request.data.get('dob')
        doa = request.data.get('doa')

        try:
            user = request.user
            if name and dob and doa: 
                spouse = Spouse.objects.get(id=id,user=user)

                spouse.name = name
                spouse.dob = dob
                spouse.doa = doa
                spouse.save()
                
                instance = SpouseSerializer(spouse)
                
                return Response(instance.data)
            
            else:
                return Response({'message':'Enter the Valid details of the Spouse'})
        
        except Spouse.DoesNotExist:
             return Response({'error':"Spouse is not available"})
        

class GetKidsAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Kids.objects.all()
    serializer_class = KidsSerializer

class CreateKidsAPIView(CreateAPIView):
    def post(self,request, *args, **kwargs):
        name = request.data.get('name')
        dob = request.data.get('dob')
        gender = request.data.get('gender')

        try:
            user = request.user
            if name and dob and gender:
                kids = Kids.objects.create(name=name, gender=gender,dob = dob, user = user)
                instance = KidsSerializer(kids)
                return Response(instance.data)
            
            else:
                return Response({'error':"Mention all details of the Kids"})
        
        except Kids.DoesNotExist:
             return Response({'error':"Kids is not available"})

class UpdateKidsAPIView(CreateAPIView):
    def post(self,request, id, *args, **kwargs):
        name = request.data.get('name')
        dob = request.data.get('dob')
        gender = request.data.get('gender')

        try:
            user = request.user
            if name and dob and gender:
                kids = Kids.objects.get(id=id, user=user)

                kids.name = name
                kids.dob = dob
                kids.gender = gender
                kids.save()

                instance = KidsSerializer(kids)
                
                return Response(instance.data)
            
            else:
                return Response({'message':'Enter the Valid details of the kids'})
        
        except Kids.DoesNotExist:
             return Response({'error':"kids is not available"})
        
class GetParentsAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer

class CreateParentsAPIView(CreateAPIView):
    def post(self,request,*args,**kwargs):
        name = request.data.get('name')
        parent = request.data.get('parent')
        dob = request.data.get('dob')

        try:
            user = request.user
            if name and parent and dob:
                parent = Parents.objects.create(name=name, parent=parent,dob=dob,user=user)

                instance = ParentsSerializer(parent)
                return Response(instance.data)
            
            else:
                return Response({'error':"Mention all details of the parent"})
        
        except Parents.DoesNotExist:
             return Response({'error':"Parents is not available"})
        

class UpdateParentsAPIView(CreateAPIView):
    def post(self,request, id, *args, **kwargs):
        name = request.data.get('name')
        parent = request.data.get('parent')
        dob = request.data.get('dob')

        try:
            user = request.user
            if name and parent and dob:
                parents = Parents.objects.get(id=id, user=user)

                parents.name = name
                parents.parent = parent
                parents.dob = dob
                parents.save()

                instance = ParentsSerializer(parents)
                
                return Response(instance.data)
            
            else:
                return Response({'message':'Enter the Valid details of the parents'})
        
        except Parents.DoesNotExist:
             return Response({'error':"parents is not available"})

        