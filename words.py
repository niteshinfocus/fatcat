import random
import requests

my_array = vocabulary_words = ['Abhor', 'Abundant', 'Acclaimed', 'Acrid', 'Acumen', 'Adamant', 'Adept', 'Adhere', 'Adroit', 'Allure', 'Ambiguous', 'Apprehensive', 'Arrogant', 'Aspire', 'Authentic', 'Aversion', 'Benevolent', 'Brevity', 'Candid', 'Capricious', 'Cogent', 'Coherent', 'Condescending', 'Conducive', 'Conscientious', 'Contemptuous', 'Conviction', 'Credible', 'Cryptic', 'Cynical', 'Debacle', 'Deference', 'Deliberate', 'Demeanor', 'Denounce', 'Derogatory', 'Desolate', 'Detrimental', 'Diligent', 'Discreet', 'Disdain', 'Disparage', 'Disposition', 'Dubious', 'Eclectic', 'Egregious', 'Elusive', 'Empathy', 'Endorse', 'Enigma', 'Entail', 'Erratic', 'Euphemism', 'Exacerbate', 'Exemplary', 'Exorbitant', 'Extraneous', 'Facetious', 'Fervent', 'Fluctuate', 'Formidable', 'Frivolous', 'Furtive', 'Garrulous', 'Gratuitous', 'Gregarious', 'Guile', 'Haphazard', 'Harbinger', 'Haughty', 'Heedless', 'Hierarchy', 'Histrionic', 'Homogeneous', 'Hypothetical', 'Idiosyncrasy', 'Ignominy', 'Illicit', 'Imminent', 'Impartial', 'Impetuous', 'Implication', 'Inadvertent', 'Inane', 'Incessant', 'Incongruous', 'Incontrovertible', 'Indifferent', 'Indignation', 'Indispensable', 'Indulgent', 'Inevitable', 'Infallible', 'Inherent', 'Innocuous', 'Insidious', 'Insipid', 'Insolent', 'Intrepid', 'Intrinsic', 'Apathetic', 'Articulate', 'Aspiration', 'Assimilate', 'Audacity', 'Authenticity', 'Aversion', 'Belittle', 'Benevolent', 'Blatant', 'Bolster', 'Bombastic', 'Brevity', 'Callous', 'Candor', 'Capricious', 'Catalyst', 'Censure', 'Charisma', 'Chronic', 'Circumspect', 'Coalesce', 'Cogent', 'Complacency', 'Condone', 'Conducive', 'Connoisseur', 'Conscientious', 'Consensus', 'Contemptuous', 'Contrite', 'Conundrum', 'Copious', 'Corroborate', 'Credibility', 'Cryptic', 'Cursory', 'Dearth', 'Debacle', 'Deference', 'Deliberate', 'Delusion', 'Demure', 'Denounce', 'Deride', 'Desolate', 'Despondent', 'Detrimental', 'Deviate', 'Diligent']
 

# Use random.sample() to select two random words
selected_words = random.sample(my_array, 2)
word = selected_words[0]
word1 = selected_words[1]
# print(word1)
# print(word)

#generating meaning of random words
url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
meaning = requests.get(url).json()
definition = meaning[0]['meanings'][0]['definitions'][0]['definition']

url2 = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word1
meaning1 = requests.get(url2).json()
definition1 = meaning1[0]['meanings'][0]['definitions'][0]['definition']

# print(word +": "+ definition)
# print(word1 +": "+ definition1)