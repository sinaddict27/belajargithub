html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>Hello Guys dari Python!</h1>
    <p>File ini dibuat secara otomatis menggunakan script Python.</p>
</body>
</html>
"""

with open("index.html", "w") as file:
    file.write(html_code)

print("Berhasil membuat file index.html!")
