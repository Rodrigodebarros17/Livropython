import os
import os.path

dir = input("Informe o diretório:")

with open(f"{dir}\dir.html", "w", encoding="utf-8") as página:
    página.write(f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
</head>
<body>
<h1>{dir}</h1>
<ul>
 """)
    for c in os.listdir(dir):
        print(c)
        if os.path.isfile(c):
            print(c)
            if s[len(s)-3:len(s)] == "jpg" or s[len(s)-3:len(s)] == "png":
                página.write(f"<li><a href=\"url\">{dir}\{c}</a></li>")
            else:
                página.write(f"<li>{dir}\{c}</li>")
    página.write("</ul>\n")
    página.write("</body></html>")
