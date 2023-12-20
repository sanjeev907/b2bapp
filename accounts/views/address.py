from accounts.models.users import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView,CreateAPIView , GenericAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.serializers.address import ZoneSerializer,AddressSerializer,StateSerializer,CountrySerializer,CitySerializer,PincodeSerializer
from accounts.models.address import Zone, Country, State, City, Pincode, Address


class GetZoneAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class GetCountryAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class GetStateAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer

class GetCityAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer

class GetPincodeAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Pincode.objects.all()
    serializer_class = PincodeSerializer

class GetAddressAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class CreateAddressAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        address_tye = request.data.get('address_tye')
        street_address = request.data.get('street_address')
        landmark = request.data.get('landmark')
        locality = request.data.get('locality')
        city_id = request.data.get('city')  
        pincode_id = request.data.get('pincode')  
        country_id = request.data.get('country')  
        company_id = request.data.get('company')  

        try:
            if address_tye and street_address and locality and landmark and city_id and pincode_id and country_id and company_id:
                state = City.objects.get(id=city_id).state
                
                address = Address.objects.create(
                    address_tye=address_tye,
                    street_address=street_address,
                    landmark=landmark,
                    locality=locality,
                    city_id=city_id,
                    state=state,
                    pincode_id=pincode_id,
                    country_id=country_id,
                    company_id=company_id,
                    zone=state.zone  
                )

                
                instance = AddressSerializer(address)
                return Response(instance.data)
            else:
                return Response({"message": "Enter valid details for the address"})
        except City.DoesNotExist:
            return Response({"message": "Invalid city ID"})
        except Address.DoesNotExist:
            return Response({"message": "Error creating the address"})