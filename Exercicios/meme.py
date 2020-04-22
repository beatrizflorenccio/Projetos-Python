#EXEMPLO DO MÓDULO emoji

#import emoji

name = input("QUEM FALA? ").strip().upper()
if name == "VEIGA":
    a = emoji.emojize("EAE COMÉDIA! :sunglasses:",use_aliases=True)
    print(a)
