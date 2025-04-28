import sys
import os
import markdown

inputpath = sys.argv[2]
outputpath = sys.argv[3]

if sys.argv[0] != "file-converter.py":
    print("1番目の引数は file-converter.py としてください")
    sys.exit()

if sys.argv[1] != "markdown":
    print("2番目の引数として指定するコマンドは markdown としてください")
    sys.exit()

if inputpath[-3:] != ".md":
    print("3番目の引数として指定するファイルの拡張子は .md としてください")
    sys.exit()

if not os.path.exists(inputpath):
    print("3番目の引数として指定されたファイルが存在しません")
    sys.exit()

if outputpath[-5:] != ".html":
    print("4番目の引数として指定するファイルの拡張子は .html としてください")
    sys.exit()

with open(inputpath) as f:
    contents = f.read()
html = markdown.markdown(contents)

with open(outputpath, "w") as f:
    f.write(html)
