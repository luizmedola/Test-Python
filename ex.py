a = "lUIZ"
print(len(a))

b = (len(a))
print(b)
# len realiza a contagem de caracteres que possui na variavel

c = "luiz"
print(c.capitalize())
# capitalize transforma a primeira letra da palavra em maiúscula

d = "luiz"
print(a.upper())
# upper transforma todo o texto em maiúsculo

e = "LUIZ"
print(e.casefold())
# case transforma todo o texto em minusculo

f = "LUIZ"
print(f.lower())
# case transforma todo o texto em minusculo

g = "LUIZ"
print(g.islower())
# lower identifica se todo o texto está em minusculo

h = "LUIZ"
print(h.isupper())
# issuper identifica se todo o texto está em maiúsculo

x = "12345"
print(x.isdigit())

z = "1234abc"
print(z.isdigit())
# isdigit verifica se uma string só possui números inteiros

o = "Luiz Medola"
print(o.replace("Medola","Mendonça"))
# replace serve para trocar todas as ocorrências de uma substring por outra em uma string

r = "Luiz-Otávio-Medola"
print(r.split("-"))
# split separa uma string usando sep como separador, retorna uma lista das substring, passado sem parâmetro substitui espaço por ","

j = "Luiz Otávio Medola"
print(j.find("Medola"))
# find retorna onde a substring começa na string

q = "Luiz Otávio Medola"
print("Medola" in q)
# in verifica se uma substring é parte de uma outra string

t = "Luiz Otávio Medola"
print(t.count("t"))
# count retorna a frequência de ocorrência do parâmetro passado

s = "São Paulo"
print(s[0])
print(s[2])
print(s[6])

p = "São Paulo"
print(p[-1])
print(p[-2])
print(p[-3])