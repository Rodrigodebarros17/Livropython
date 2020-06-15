# Programa 9.8 - Geração de uma página web a partir de um dicionário
filmes = {
    "Drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"], 
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de matar"],
    "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora!"]
}
with open("filmes.html", "w", encoding="utf-8") as página:
    página.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
</head>
<body>
 """)
    for c, v in filmes.items():
        página.write(f"<h1>{c}</h1>\n")
        página.write("<ul>\n")
        for e in v:
            página.write(f"<li>{e}</li>\n")
        página.write("</ul>\n")
    página.write("</body></html>")