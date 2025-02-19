file_nevek = ['forras_afrika.txt', 'forras_azsia.txt', 'forras_europa.txt']

orszagok = []

for file_nev in file_nevek:
    with open(file_nev, 'r', encoding='utf-8') as file:       
        fejlec = file.readline()       
        for sor in file:
            adatok = sor.strip().split(";")  
            orszag = {
                'orszag': adatok[0],
                'fovaros': adatok[1],
                'terulet': int(adatok[2]),
                'nepesseg': int(adatok[3]),
                'nepsuruseg': float(adatok[4].replace(',', '.')) 
            }
            orszagok.append(orszag)

legnagyobb_nepessegu_orszag = max(orszagok, key=lambda x: x['nepesseg'])
print(f"A legnagyobb népességgel rendelkező ország: {legnagyobb_nepessegu_orszag['orszag']} ({legnagyobb_nepessegu_orszag['nepesseg']})")

legnagyobb_teruletu_orszag = max(orszagok, key=lambda x: x['terulet'])
print(f"A legnagyobb területű ország: {legnagyobb_teruletu_orszag['orszag']} ({legnagyobb_teruletu_orszag['terulet']} km²)")

max_nepsurusegu_orszag = max(orszagok, key=lambda x: x['nepsuruseg'])
print(f"A legnagyobb népsűrűségű ország: {max_nepsurusegu_orszag['orszag']} ({max_nepsurusegu_orszag['nepsuruseg']} fő/km²)")

atlagos_nepsuruseg = sum(orszag['nepsuruseg'] for orszag in orszagok) / len(orszagok)
print(f"Az országok átlagos népsűrűsége: {atlagos_nepsuruseg:.2f} fő/km²")

ossz_terulet = sum(orszag['terulet'] for orszag in orszagok)
print(f"Az összes ország együttes területe: {ossz_terulet} km²")

import statistics
nepessegek = [orszag['nepesseg'] for orszag in orszagok]
medián_nepesseg = statistics.median(nepessegek)
print(f"Az országok népességének mediánja: {medián_nepesseg}")

magas_nepsurusegu_orszagok = [orszag['orszag'] for orszag in orszagok if orszag['nepsuruseg'] > 150]
print("Országok, ahol a népsűrűség nagyobb, mint 150 fő/km²:")
print(magas_nepsurusegu_orszagok)

rendezve_terulet_szerint = sorted(orszagok, key=lambda x: x['terulet'])
print("Országok területük szerint növekvő sorrendben:")
for orszag in rendezve_terulet_szerint:
    print(f"{orszag['orszag']} - {orszag['terulet']} km²")

alacsony_nepsurusegu = [orszag['orszag'] for orszag in orszagok if orszag['nepsuruseg'] < 100]
kozepes_nepsurusegu = [orszag['orszag'] for orszag in orszagok if 100 <= orszag['nepsuruseg'] <= 300]
magas_nepsurusegu = [orszag['orszag'] for orszag in orszagok if orszag['nepsuruseg'] > 300]

print("Alacsony népsűrűségű országok (kisebb 100 fő/km²):")
print(alacsony_nepsurusegu)

print("Közepes népsűrűségű országok (100-300 fő/km²):")
print(kozepes_nepsurusegu)

print("Magas népsűrűségű országok (nagyobb 300 fő/km²):")
print(magas_nepsurusegu)