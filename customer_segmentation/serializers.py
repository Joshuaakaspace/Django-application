from .models import Accounts1, Accounts2
from rest_framework import serializers

class DataSerializers(serializers.ModelSerializer):

    class Meta:
        model = Accounts1
        fields = ["a_number", "account_name", "account_status", "address", "country", "last_updated", "segment_source", "entity_url",
                  "unavailable", "segmentation_details", "sfdc_segmentation", "modified"]

    last_updated = serializers.StringRelatedField()
    segmentation_details = serializers.SerializerMethodField()
    def get_segmentation_details(self, obj):
        try:
            org_1 = obj.org_type_1 if obj.org_type_1 else ""
            org_2 = obj.org_type_2 if obj.org_type_2 else ""
            org_3 = obj.org_type_3 if obj.org_type_3 else ""
            org_4 = obj.org_type_4 if obj.org_type_4 else ""
            org_5 = obj.org_type_5 if obj.org_type_5 else ""
            orgs = org_1 + ", " + org_2 + ", " + org_3 + ", " + org_4 + ", " + org_5 
            return orgs
        except:
            return ""
    def to_representation(self, instance):
        rep = super(DataSerializers, self).to_representation(instance)
        rep['last_updated'] = instance.last_updated.username if instance.last_updated else ""
        return rep