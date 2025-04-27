from ZAppUser.models import Product
from rest_framework import serializers

class ProductSerializers1(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True) #drnaha 7it bghina ngoulo ha ecriture hada 7it makayench f assel f model
    name = serializers.CharField(max_length=255)
    price_in_euros = serializers.SerializerMethodField()
    new_description = serializers.SerializerMethodField()
    # detail_link = serializers.SerializerMethodField() # Hadi Method link (code:090) 
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_view_detail',lookup_field='pk') #method akhera bach tjib link ms aykhess tzid un ligne f page api(context)
    
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id','name','price','description','email','price_in_euros','new_description','link']
        read_only_fields = ['created_at', 'updated_at']
        
    def get_price_in_euros(self, obj):
        return obj.get_price_in_euros()
    
    def get_new_description(self, obj):
        return obj.get_description()
    
    # def get_detail_link(self, obj): # Hadi Method link (code:090) 
    #     return obj.get_absolute_url()
        
    def validate_name(self, value): #Validate Name
        if value in ['tby','zby','putain','cock']:
            raise serializers.ValidationError('You are not allowed to use this name')
        return value
    
    def create(self, validated_data):
        email = validated_data.pop('email')
        print(email)
        return super().create(validated_data)

class ProductSerializers2(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    
    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance