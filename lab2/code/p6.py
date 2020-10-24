import json
import random
with open("/content/country-by-capital-city.json","r") as f:
    cc = f.read()

ccd = json.loads(cc)
ccd2 = {d['country']:d['city'] for d in ccd}
ccd_len = len(ccd2)

cor = 0
for _ in range(50):
    n = random.randint(0, ccd_len-1)
    ctrs = list(ccd2.keys())
    ctr = ctrs[n]
    print(ctr)
    ans = input("What is the capital of {}? ".format(ctr))
    cap = ccd2[ctr]
    if ans.lower()==cap.lower():
        print("You answer is correct.")
        cor = cor + 1
    else:
        print("The correct answer should be {}.".format(ccd2[ctr]))