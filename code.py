import PyPDF2
a=PyPDF2.PdfFileReader('C:/Users/HP/Desktop/Cases/PROPERTY-CRIMES/Swami_Vasudevanand_Saraswati_vs_Jagat_Guru_Shankarcharya_on_22_September_2017.PDF')
str=""
n=a.getNumPages()
for i in range(n):
    str+=a.getPage(i).extractText()

with open("prop9.txt","w",encoding="utf-8") as f:
    f.write(str)