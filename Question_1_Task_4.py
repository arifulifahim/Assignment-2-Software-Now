import spacy



# Read the text file
with open('extracted_text.txt', 'r') as file:
    text = file.read()

# Load scispaCy models
nlp_sci_sm = spacy.load('en_core_sci_sm')
nlp_bc5cdr = spacy.load('en_ner_bc5cdr_md')

# Run NER on the combined text
doc_sci_sm = nlp_sci_sm(text)
doc_bc5cdr = nlp_bc5cdr(text)

# Extract diseases and drugs entities from both models
entities_sci_sm = [(ent.text, ent.label_) for ent in doc_sci_sm.ents if ent.label_ in ['DISEASE', 'DRUG']]
entities_bc5cdr = [(ent.text, ent.label_) for ent in doc_bc5cdr.ents if ent.label_ in ['DISEASE', 'DRUG']]

# Compare the results
sci_sm_entities = set(entities_sci_sm)
bc5cdr_entities = set(entities_bc5cdr)
common_entities = sci_sm_entities & bc5cdr_entities
unique_sci_sm = sci_sm_entities - bc5cdr_entities
unique_bc5cdr = bc5cdr_entities - sci_sm_entities

print(f"Total entities in scispaCy (en_core_sci_sm): {len(sci_sm_entities)}")
print(f"Total entities in scispaCy (bc5cdr): {len(bc5cdr_entities)}")
print(f"Common entities: {len(common_entities)}")
print(f"Unique to en_core_sci_sm: {len(unique_sci_sm)}")
print(f"Unique to bc5cdr: {len(unique_bc5cdr)}")

