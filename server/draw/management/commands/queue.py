from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import datetime


from pdf2image import convert_from_path
from PIL import Image
from smb.SMBHandler import SMBHandler
from smb.SMBConnection import SMBConnection
import tempfile
# sudo apt install poppler-utils

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Command(BaseCommand):
    args = ''
    help = ''
    
    def handle(self, *args, **options):
        pass





from draw.models import FileModel
qs_files = FileModel.objects.all()



from pdf2image import convert_from_path
from PIL import Image
def pdf_to_webp(pdf_path, output_folder):
    # Конвертируем PDF в список изображений (по одному изображению на страницу)
    pages = convert_from_path(pdf_path)

    for i, page in enumerate(pages):
        # Генерируем путь для сохранения каждого изображения
        output_path = f"{output_folder}/slide_{i + 1}.webp"
        
        # Сохраняем изображение в формате WEBP
        page.save(output_path, "WEBP")
        print(f"Сохранено: {output_path}")

    # Создаём превью из первого изображения и сохраняем его в формате WEBP в диеркторию prw
    prw_path = f"{output_folder}/slide_1.webp"
    img = Image.open(prw_path)
    img.thumbnail((420, 420))
    img.save(f"{'files/prw'}/prw.webp", "WEBP")
    print(f"Создано превью: {output_folder}/prw.webp")



USERNAME='user'
PASSWORD='123456'
SERVER='deop.local'
SHARE='public'


conn = SMBConnection(USERNAME, PASSWORD, "pysmb", SERVER, use_ntlm_v2=True)
conn.connect(SERVER, 445)
file_path = "data-1/BCP/public/04. Архив чертежей/Корпус Т1400 целиком/ПДФ/Т1400.000.014 Фланец.pdf"


with open('files/pdf/Т1400.000.014 Фланец.pdf', "wb") as f:
    conn.retrieveFile(SHARE, file_path, f)

pdf_to_webp('files/pdf/Т1400.000.014 Фланец.pdf', 'files/webp')


conn.close()