from .models import Accounts1, Accounts2
from rest_framework import serializers

class DataSerializers(serializers.ModelSerializer):

    class Meta:
        model = Accounts1
        fields = ["a_number", "account_name", "account_status", "address", "country", "last_updated", "segment_source", "entity_url",
                  "unavailable", "org_type"]

    last_updated = serializers.StringRelatedField()
    org_type = serializers.SerializerMethodField()
    
    def get_org_type(self, obj):
        try:
            org = Accounts2.objects.filter(a_number=obj.a_number).first()
            org_type = org.org_type
            return org_type
        except:
            return ""
    
    def to_representation(self, instance):
        rep = super(DataSerializers, self).to_representation(instance)
        rep['last_updated'] = instance.last_updated.username if instance.last_updated else ""
        return rep