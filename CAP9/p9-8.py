# Programa 9.8 - Geração de uma págia web a partir de um dicionário
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
        for e in v:
            página.write(f"<h2>{c}</h2>\n")
    página.write("</body></html>")