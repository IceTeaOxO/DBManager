# pip install pdf2image Pillow


from pdf2image import convert_from_path

# 指定PDF文件的路徑
pdf_path = 'testData/sealt1.pdf'

# 將PDF轉換為圖像
images = convert_from_path(pdf_path)

# 儲存每一頁為PNG文件
for i, image in enumerate(images):
    image.save(f'page_{i + 1}.png', 'PNG')
