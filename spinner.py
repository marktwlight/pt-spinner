from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.downloader import download
import nltk
import main

# 下载葡萄牙语的语言包
# download('own')

original_text_pt = 'O governo federal estuda um programa permanente de renovação de frota de caminhões e ônibus, afirmou nesta quinta-feira (8) o vice-presidente da República e ministro do Desenvolvimento, Indústria, Comércio e Serviços, Geraldo Alckmin.Ele participou de evento transmitido pela internet da Associação Nacional dos Fabricantes de Veículos Automotores (Anfavea).Segundo Alckmin, o objetivo desse programa em estudo seria reduzir custo do frete, no caso dos caminhões, e, também, estimular a segurança ao ter uma frota "mais nova".O vice-presidente lembrou que um programa de renovação de frota, teve validade durante 2023. O objetivo foi retirar de circulação veículos pesados com mais de 20 anos de circulação.Com benefícios limitados, o programa disponibilizou R$ 1 bilhão em créditos tributários em 2023 para as montadoras. Foram R$ 700 milhões para caminhões e R$ 300 milhões para ônibus. Não foi divulgado um balanço final sobre o uso dos recursos.Para os compradores, pessoas físicas ou jurídicas, o desconto variou de R$ 33,6 mil a R$ 99,4 mil por veículo – o abatimento foi maior em modelos mais caros.O programa incluiu caminhões leves, semileves, médios, semipesados e pesados, além de ônibus urbanos e rodoviários."Deu um incentivo importante. Baseado em critério social, carros até R$ 120 mil, de eficiência energética, ambiental, e na densidade industrial. Queremos que fabrique aqui no Brasil, tirando de circulação caminhões e ônibus com mais de 20 anos de circulação", acrescentou Alckmin.'
def get_primary_synonym(word):
    synonyms = []
    for synset in wn.synsets(word,lang='por'):
    
        for lemma in synset.lemmas('por'):
            
            synonyms.append(lemma.name())
            
            break  # 获取第一个同义词即可
    return synonyms

def preprocess_text(text):
    sentences = sent_tokenize(text, language='portuguese')  # 分句
    processed_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence, language='portuguese')  # 分词
        new_words = []
        for word in words:
            synonyms = get_primary_synonym(word)
            if synonyms:
                new_words.append(synonyms[0])  # 只保留第一个同义词
            else:
                new_words.append(word)
        processed_sentence = ' '.join(new_words)
        processed_sentences.append(processed_sentence)
    processed_text = ' '.join(processed_sentences)
    return processed_text

# 对文本进行词汇替换和句子重组
def transform_text(text):
    transformed_text = preprocess_text(text)
    return transformed_text

# 合并生成文本
new_text_pt = transform_text(original_text_pt)

rate = main.getSimilarity(original_text_pt, new_text_pt)
print('new_text_pt:', new_text_pt)
print('rate:', rate)
