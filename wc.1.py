import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
text="Music has always been one of the most important parts of my life. I especially love singing and writing lyrics because they allow me to express my thoughts, emotions, and creativity in a unique way. Whenever I sing, I feel confident, peaceful, and connected to my feelings. Singing helps me communicate emotions that are sometimes difficult to express through ordinary words. I enjoy exploring different styles of music and learning how melodies and rhythms can create powerful experiences for listeners. Along with singing, lyric writing is another passion of mine. I love turning my ideas, dreams, experiences, and observations into meaningful words that can inspire or comfort others. Writing lyrics gives me the freedom to tell stories, share emotions, and create messages that people can relate to. It also improves my imagination and helps me develop my language and communication skills. Music has the ability to bring people together regardless of their background, culture, or language, and that is one of the reasons I admire it so much. Listening to great songs motivates me to improve my own singing and songwriting abilities. In the future, I hope to continue developing my talent, create original songs, and share my music with a wider audience. For me, music is not just a hobby; it is a source of happiness, inspiration, and self-expression that plays a significant role in my life."
import nltk
nltk.download('punkt')
nltk.download('stopwords')
words = word_tokenize(text.lower())  
print(words)
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
print(filtered_words)
word_freq = Counter(filtered_words)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  
plt.show()
