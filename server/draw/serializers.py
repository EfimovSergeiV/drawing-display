from rest_framework import serializers
from draw.models import DrawingModel
from datetime import datetime

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class DrawingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DrawingModel
        fields = '__all__'




class DrawingSocketSerializer(serializers.ModelSerializer):
    prw = serializers.SerializerMethodField()
    webp = serializers.SerializerMethodField()
    pdf = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0  # Инициализация счётчика
        self.base_url = self.context.get('base_url', '')

    class Meta:
        model = DrawingModel
        fields = ('uuid', 'name', 'status', 'created_at', 'link', 'pdf', 'webp', 'webp_size', 'prw',)

    # def get_prw(self, obj):
    #     base_url = self.context.get('base_url', '')
    #     print(f'{current_time()} THIS IS OBJ: ', obj)
    #     if obj:
    #         return f"{base_url}{obj.prw.url}" if base_url else obj.prw.url

    # def get_webp(self, obj):
    #     base_url = self.context.get('base_url', '')
    #     print(f'{current_time()} THIS IS OBJ: ', obj)
    #     if obj:
    #         return f"{base_url}{obj.webp.url}" if base_url else obj.webp.url

    # def get_pdf(self, obj):
    #     self.counter += 1
        
    #     base_url = self.context.get('base_url', '')
        
    #     print(f'{current_time()} THIS IS OBJ {self.counter}: ', obj)

    #     if obj:
    #         return f"{base_url}{obj.pdf.url}" if base_url else obj.pdf.url
    
    def get_prw(self, obj):
        if obj and obj.prw and hasattr(obj.prw, 'url'):
            return f"{self.base_url}{obj.prw.url}" if self.base_url else obj.prw.url
        return None

    def get_webp(self, obj):
        if obj and obj.webp and hasattr(obj.webp, 'url'):
            return f"{self.base_url}{obj.webp.url}" if self.base_url else obj.webp.url
        return None

    def get_pdf(self, obj):
        self.counter += 1
        if obj and obj.pdf and hasattr(obj.pdf, 'url'):
            return f"{self.base_url}{obj.pdf.url}" if self.base_url else obj.pdf.url
        return None