letter = "hey my name is {} and I am from {}"
country="india"
name="Harry"
print(letter.format(name,country))
print("--------------------------------------------------------")

letter = "hey my name is {1} and I am from {0}"
country="india"
name="Harry"
print(letter.format(country,name))
print(f"hey me name is {name} and I am from {country}")
print("--------------------------------------------------------")

txt="For only {price:.2f} dollars"
print(txt.format(price = 49.09999))
print("--------------------------------------------------------")

price=49.0999
txt1=f"For only {price:.2f} dollars"
print(txt1)
print("--------------------------------------------------------")

print(type(f"{2*30}"))
print(f"{2*30}")
print("--------------------------------------------------------")

print(f"We use f-string like this: Hey my name is {{name}} and I am from {{country}}")
print("--------------------------------------------------------")
