from rest_framework import serializers
from draw.models import DrawingModel



class DrawingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DrawingModel
        fields = '__all__'




class DrawingSocketSerializer(serializers.ModelSerializer):
    prw = serializers.SerializerMethodField()
    webp = serializers.SerializerMethodField()
    pdf = serializers.SerializerMethodField()

    class Meta:
        model = DrawingModel
        fields = ('uuid', 'name', 'status', 'created_at', 'link', 'pdf', 'webp', 'webp_size', 'prw',)

    def get_prw(self, obj):
        base_url = self.context.get('base_url', '')
        
        if obj:
            return f"{base_url}{obj.prw.url}" if base_url else obj.prw.url

    def get_webp(self, obj):
        base_url = self.context.get('base_url', '')

        if obj:
            return f"{base_url}{obj.webp.url}" if base_url else obj.webp.url

    def get_pdf(self, obj):
        base_url = self.context.get('base_url', '')
        
        print(obj)
        if obj:
            return f"{base_url}{obj.pdf.url}" if base_url else obj.pdf.url
