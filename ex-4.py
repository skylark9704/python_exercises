# Ex-5
# Extract filenames that has txt as extension
filenames = ['file1.txt', 'file2.txt', 'file3.pdf', 'file4.pdf']


def get_file(ext):
    return [file for file in filenames if file.find("."+ext) != -1] 

print(get_file("pdf"))

    
