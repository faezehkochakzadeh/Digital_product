from rest_framework import serializers

from .models import Category, File, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')


class FileSerializer(serializers.ModelSerializer):
    file_type= serializers.SerializerMethodField() #چون میخواهیم خودمان به صورت دستی تغییرش بدهیم
    class Meta:
        model = File
        fields = ('id','title','file_type', 'file')

    def get_file_type(self,obj): #بجای عدد اون متنی که میدهیم رو برمیگردونه
        return obj.get_file_type_display()


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ("id",'title', 'description', 'avatar', 'categories','url')
