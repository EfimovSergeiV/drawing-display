from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import datetime


from pdf2image import convert_from_path
from PIL import Image
from smb.SMBHandler import SMBHandler
from smb.SMBConnection import SMBConnection
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




USERNAME='user'
PASSWORD='123456'
SERVER='deop.local'
SHARE='public'


conn = SMBConnection(USERNAME, PASSWORD, "pysmb", SERVER, use_ntlm_v2=True)
conn.connect(SERVER, 445)
    
# PATH = "/data-1/BCP/public/04. Архив чертежей"
DIRS = ["data-1", "BCP", "public", "04. Архив чертежей"]

def get_list_files(DIRS, level=1):

    file_list = conn.listPath(SHARE, str(Path(*DIRS)))
    for file in file_list:
        if file.filename in [".", ".."]:
            continue
        if file.isDirectory:
            # print(f"{str(Path(*DIRS))}/{file.filename}")
            get_list_files(DIRS + [file.filename], level + 1)
        else:
            if f"{str(Path(*DIRS))}/{file.filename}".endswith(".pdf"):
                print(f"{str(Path(*DIRS))}/{file.filename}")

                name = file.filename
                link = f"{str(Path(*DIRS))}/{file.filename}"

                qs_files.update_or_create(name=name, link=link)



get_list_files(DIRS)
