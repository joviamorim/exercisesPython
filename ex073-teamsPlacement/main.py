placement = ("Santos", "Atlético MG", "Corinthians", "Cuiabá", "Internacional", "Bragantino", "Palmeiras", "Flamengo", "Coritiba",
 "São Paulo", "Botafogo", "Fluminense", "América MG", "Ceará SC", "Avaí", "Athletico PR", "Atlético GO", "Goiás", "Juventude", "Fortaleza")

for i in range(0,5):
    print(f"{i+1} place: {placement[i]}")

print("-"*10)

for i in range(16,20):
    print(f"{i+1} place: {placement[i]}")

print("-"*10)

sort = sorted(placement)
print("Teams in alphabetical order:")
for i in sort:
    print(i)

print("-"*10)

position = placement.index("São Paulo")+1
print(f"São Paulo is on position {position}")
