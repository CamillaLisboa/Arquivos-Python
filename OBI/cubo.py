n = int(input())
    
if n > 2:
    nenhum = (n - 2) ** 3
else:
    nenhum = 0

if n > 1:
    uma_face = 6 * (n - 2) ** 2
else:
    uma_face = 0

if n > 1:
    duas_faces = 12 * (n - 2)
else:
    duas_faces = 0

tres_faces = 8 if n > 1 else 0
  
print(nenhum)
print(uma_face)
print(duas_faces)
print(tres_faces)

