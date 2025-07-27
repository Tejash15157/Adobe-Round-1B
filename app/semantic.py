from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

def rank_sections(sections, query):
    query_embedding = model.encode(query, convert_to_tensor=True)
    for sec in sections:
        sec_embedding = model.encode(sec["text"], convert_to_tensor=True)
        sec["score"] = float(util.pytorch_cos_sim(query_embedding, sec_embedding)[0][0])
    return sorted(sections, key=lambda x: x["score"], reverse=True)
