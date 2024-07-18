from ruwordnet import RuWordNet

wn = RuWordNet()

for i in wn['Стрелок'][0].sources:
    print(i.synset)
