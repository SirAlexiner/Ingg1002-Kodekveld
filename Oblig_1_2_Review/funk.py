def hei(): # Lager en hei funksjon, vi ønsker ikke å gi den noe
  print('Hei Tilbake') # Den gir oss ikke noe tilbake den bare sier "Hei tilbake"

hei() # Her sier vi "Hei" i koden.
# kjører vi dette får vi ut "Hei Tilbake"

# Vi kan også gi noe til en funksjon vi ikke forventer noe tilbake fra:
def hei_mitt_navn_er(navn): # Lager en hei funksjon som tar imot eit navn,
  print(f'Hei {navn}') # Her skriver vi en formatter tekst, lar oss bruke variabler til å si Hei med navnet vi ga.

hei_mitt_navn_er('Torgrim') # Her sier vi "Hei, mitt navn er Torgrim" i koden
# kjører vi dette får vi ut "Hei Torgrim"

# Så har vi de vi ønsker noe tilbake fra:
def hva_heter_du(): # Lager en hva heter du funksjon
  mitt_navn = 'Inge' # Inne i funksjonen har vi navnet til koden lagret som "mitt_navn"
  return mitt_navn # Når noen spør gir koden navnet sitt til den som spør

koden_sitt_navn = hva_heter_du() # Når vi spør om noe som returnere noe må vi lagre det for å "huske"
print(f'Koden heter {koden_sitt_navn}') # Her sier VI at koden heter Mathilde 
# kjører vi dette får vi ut "Koden heter Mathilde"

#Siste:
# Vi kan gi en funksjon noe og forvente noe tilbake:
def mitt_navn_baklengs(navn_forlengs):
  navn_baklengs = navn_forlengs[::-1] # Dette bare skriver det vi tar imot baklengs (Ikke viktig)
  return navn_baklengs # Sender tilbake navnet baklengs

print(f"Torgrim baklengs er {mitt_navn_baklengs('Torgrim')}") # Når en funksjon returnere en verdi kan vi også printe det.

# kjører vi dette får vi ut "Torgrim baklengs er mirgroT"
# Men siden vi ikke lagret det i en variabel, må vi sjekke igjen neste gang vi trenger å vite hva det er baklengs