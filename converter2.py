# PyMuPDF

import os
import fitz  # PyMuPDF

# 指定包含PDF文件的資料夾
pdf_folder = 'testData'

# 遍歷資料夾中的所有PDF文件
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, filename)
        pdf_document = fitz.open(pdf_path)

        # 將每一頁轉換為PNG
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            pix = page.get_pixmap()
            output_path = os.path.join(pdf_folder, f'{filename[:-4]}_page_{page_num + 1}.png')
            pix.save(output_path)

        pdf_document.close()
