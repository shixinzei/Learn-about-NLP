
# coding: utf-8

# # 英文文本处理与[spaCy](https://spacy.io/)
# 
# [spaCy](https://spacy.io/)是Python和Cython中的高级自然语言处理库，它建立在最新的研究基础之上，从一开始就设计用于实际产品。spaCy 带有预先训练的统计模型和单词向量，目前支持 20 多种语言的标记。它具有世界上速度最快的句法分析器，用于标签的卷积神经网络模型，解析和命名实体识别以及与深度学习整合。
# 
# ![](../img/L2_spaCy.jpg)

# ### 0.英文Tokenization(标记化/分词)
# 
# >文本是不能成段送入模型中进行分析的，我们通常会把文本切成有独立含义的字、词或者短语，这个过程叫做tokenization，这通常是大家解决自然语言处理问题的第一步。在spaCY中同样可以很方便地完成Tokenization。

# In[1]:


# python -m spacy download en_core_web_sm


# In[2]:


import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp('Hello World! My name is wydxry')
for token in doc:
    print('"' + token.text + '"')


# 每个token对象有着非常丰富的属性，如下的方式可以取出其中的部分属性。

# In[3]:


doc = nlp("Next week I'll   be in Chengdu.")
for token in doc:
    print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}".format(
        token.text,
        token.idx,
        token.lemma_,
        token.is_punct,
        token.is_space,
        token.shape_,
        token.pos_,
        token.tag_
    ))


# 断句功能在spaCy中也有体现，如下：

# In[4]:


# 断句 sents
doc = nlp("Hello World! My name is 午夜的行人， 今天好热啊. 啊啊啊啊")
for sent in doc.sents:
    print(sent)


# ### 1.词性标注
# 
# >词性（part-of-speech）是词汇基本的语法属性，通常也称为词性。
# 
# >词性标注（part-of-speech tagging）,又称为词类标注或者简称标注，是指为分词结果中的每个单词标注一个正确的词性的程序，也即确定每个词是名词、动词、形容词或者其他词性的过程。
# 
# >词性标注是很多NLP任务的预处理步骤，如句法分析，经过词性标注后的文本会带来很大的便利性，但也不是不可或缺的步骤。
# >词性标注的最简单做法是选取最高频词性，主流的做法可以分为基于规则和基于统计的方法，包括：
# * 基于最大熵的词性标注
# * 基于统计最大概率输出词性
# * 基于HMM的词性标注

# In[5]:


# 词性标注
doc = nlp("Next week I'll be in Sichuan.")
print([(token.text, token.tag_) for token in doc])


# 具体的词性标注编码和含义见如下对应表：
# 
# | POS Tag | Description | Example |
# | --- | --- | --- |
# | CC | coordinating conjunction | and |
# | CD | cardinal number | 1, third |
# | DT | determiner | the |
# | EX | existential there | there, is |
# | FW | foreign word | d’hoevre |
# | IN | preposition or subordinating conjunction | in, of, like |
# | JJ | adjective | big |
# | JJR | adjective, comparative | bigger |
# | JJS | adjective, superlative | biggest |
# | LS | list marker | 1) |
# | MD | modal | could, will |
# | NN | noun, singular or mass | door |
# | NNS | noun plural | doors |
# | NNP | proper noun, singular | John |
# | NNPS | proper noun, plural | Vikings |
# | PDT | predeterminer | both the boys |
# | POS | possessive ending | friend‘s |
# | PRP | personal pronoun | I, he, it |
# | PRP$ | possessive pronoun | my, his |
# | RB | adverb | however, usually, naturally, here, good |
# | RBR | adverb, comparative | better |
# | RBS | adverb, superlative | best |
# | RP | particle | give up |
# | TO | to | to go, to him |
# | UH | interjection | uhhuhhuhh |
# | VB | verb, base form | take |
# | VBD | verb, past tense | took |
# | VBG | verb, gerund or present participle | taking |
# | VBN | verb, past participle | taken |
# | VBP | verb, sing. present, non-3d | take |
# | VBZ | verb, 3rd person sing. present | takes |
# | WDT | wh-determiner | which |
# | WP | wh-pronoun | who, what |
# | WP\$ | possessive wh-pronoun | whose |
# | WRB | wh-abverb | where, when |

# ### 2.命名实体识别
# 
# 命名实体识别（Named Entity Recognition，简称NER），又称作“专名识别”，是指识别文本中具有特定意义的实体，主要包括人名、地名、机构名、专有名词等。
# 
# 通常包括两部分：1) 实体边界识别；2) 确定实体类别（人名、地名、机构名或其他）。

# In[6]:


doc = nlp("Next week I'll be in Chengdu.")
for ent in doc.ents:
    print(ent.text, ent.label_)


# In[7]:


from nltk.chunk import conlltags2tree

doc = nlp("Next week I'll be in Chengdu.")
iob_tagged = [
    (
        token.text, 
        token.tag_, 
        "{0}-{1}".format(token.ent_iob_, token.ent_type_) if token.ent_iob_ != 'O' else token.ent_iob_
    ) for token in doc
]
 
print(iob_tagged)
# 按照nltk.Tree的格式显示
print(conlltags2tree(iob_tagged))


# spaCy中包含的命名实体非常丰富，如下例所示：

# In[8]:


doc = nlp("I just bought 2 shares at 9 a.m. because the stock went up 30% in just 2 days according to the WSJ")
for ent in doc.ents:
    print(ent.text, ent.label_)


# 还可以用非常漂亮的可视化做显示：

# In[9]:


from spacy import displacy
 
doc = nlp('I just bought 2 shares at 9 a.m. because the stock went up 30% in just 2 days according to the WSJ')
displacy.render(doc, style='ent', jupyter=True)


# ### 3.chunking/组块分析
# 
# spaCy可以自动检测名词短语，并输出根(root)词，比如下面的"Journal","piece","currencies"

# In[10]:


doc = nlp("Wall Street Journal just published an interesting piece on crypto currencies")
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.label_, chunk.root.text)


# ### 4.句法依存解析
# 
# spaCy有着非常强大的句法依存解析功能，可以试试对句子进行解析。

# In[11]:


doc = nlp('Wall Street Journal just published an interesting piece on crypto currencies')
 
for token in doc:
    print("{0}/{1} <--{2}-- {3}/{4}".format(
        token.text, token.tag_, token.dep_, token.head.text, token.head.tag_))


# In[12]:


from spacy import displacy
 
doc = nlp('Wall Street Journal just published an interesting piece on crypto currencies')
displacy.render(doc, style='dep', jupyter=True, options={'distance': 90})


# ### 5.词向量使用
# 
# NLP中有一个非常强大的文本表示学习方法叫做word2vec，通过词的上下文学习到词语的稠密向量化表示，同时在这个表示形态下，语义相关的词在向量空间中会比较接近。也有类似`v(爷爷)-v(奶奶) ≈ v(男人)-v(女人)`的关系。
# 
# 如果大家要使用英文的词向量，需要先下载预先训练好的结果。
# 
# 命令：!python3 -m spacy download en_core_web_lg

# In[13]:


# !python -m spacy download en_core_web_lg


# In[14]:


nlp = spacy.load('en_core_web_lg')
print(nlp.vocab['banana'].vector)


# In[15]:


from scipy import spatial

# 余弦相似度计算
cosine_similarity = lambda x, y: 1 - spatial.distance.cosine(x, y)

# 男人、女人、国王、女王 的词向量
man = nlp.vocab['man'].vector
woman = nlp.vocab['woman'].vector
queen = nlp.vocab['queen'].vector
king = nlp.vocab['king'].vector
 
# 我们对向量做一个简单的计算，"man" - "woman" + "queen"
maybe_king = man - woman + queen
computed_similarities = []

# 扫描整个词库的词向量做比对，召回最接近的词向量
for word in nlp.vocab:
    if not word.has_vector:
        continue
 
    similarity = cosine_similarity(maybe_king, word.vector)
    computed_similarities.append((word, similarity))

# 排序与最接近结果展示
computed_similarities = sorted(computed_similarities, key=lambda item: -item[1])
print([w[0].text for w in computed_similarities[:10]])


# ### 6.词汇与文本相似度
# ##### \[稀牛学院 x 网易云课程\]《AI工程师(自然语言处理方向)》课程资料 by [@寒小阳]
# 在词向量的基础上，spaCy提供了从词到文档的相似度计算的方法，下面的例子是它的使用方法。

# In[16]:


# 词汇语义相似度(关联性)
banana = nlp.vocab['banana']
dog = nlp.vocab['dog']
fruit = nlp.vocab['fruit']
animal = nlp.vocab['animal']
 
print(dog.similarity(animal), dog.similarity(fruit)) # 0.6618534 0.23552845
print(banana.similarity(fruit), banana.similarity(animal)) # 0.67148364 0.2427285


# In[17]:


# 文本语义相似度(关联性)
target = nlp("Cats are beautiful animals.")
 
doc1 = nlp("Dogs are awesome.")
doc2 = nlp("Some gorgeous creatures are felines.")
doc3 = nlp("Dolphins are swimming mammals.")
 
print(target.similarity(doc1))  # 0.8901765218466683
print(target.similarity(doc2))  # 0.9115828449161616
print(target.similarity(doc3))  # 0.7822956752876101

