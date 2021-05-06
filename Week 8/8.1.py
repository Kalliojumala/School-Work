#list of paints, user checks if paint in stock :D
paints = ["sininen", "punainen", "vihreä", "keltainen", "turkoosi"]

print("Varastossamme on seuraavia sävyjä:")
for paint in paints:
    print(paint)

user_input = input("\nMitä väriä tarvitset?\n")

if user_input.lower() in paints:
    print("Varastosta löytyy.")
else:
    print("Valitettavasti meiltä ei löydy juuri tuota sävyä.")

print("Kiitos ohjelman käytöstä.")