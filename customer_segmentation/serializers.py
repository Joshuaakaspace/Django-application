from .models import Accounts1, Accounts2
from rest_framework import serializers

class DataSerializers(serializers.ModelSerializer):

    class Meta:
        model = Accounts1
        fields = ["a_number", "account_name", "account_status", "address", "country", "last_updated", "segment_source", "entity_url",
                  "unavailable", "org_type", "segmentation_details"]

    last_updated = serializers.StringRelatedField()
    org_type = serializers.SerializerMethodField()
    segmentation_details = serializers.SerializerMethodField()
    def get_org_type(self, obj):
        try:
            org = Accounts2.objects.filter(a_number=obj.a_number).first()
            org_type = org.org_type
            return org_type
        except:
            return ""
    def get_segmentation_details(self, obj):
        try:
            org_1 = obj.org_type_1 
            org_2 = obj.org_type_2
            org_3 = obj.org_type_3
            org_4 = obj.org_type_4
            org_5 = obj.org_type_5
            orgs = org_1 + ", " + org_2 + ", " + org_3 + ", " + org_4 + ", " + org_5 
            return orgs
        except:
            return ""
    def to_representation(self, instance):
        rep = super(DataSerializers, self).to_representation(instance)
        rep['last_updated'] = instance.last_updated.username if instance.last_updated else ""
        return rep