from rest_framework import serializers
from demo.models import student, user


class studentSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only = True)
    # name = serializers.CharField()
    # age = serializers.IntegerField()
    # position = serializers.CharField()
    class Meta:
        model = student
        fields = "__all__"
    
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"


