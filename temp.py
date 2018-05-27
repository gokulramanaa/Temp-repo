
# coding: utf-8

# In[6]:


import json
import pandas as pd
import codecs
import math
from pandas.io.json import json_normalize as jsy
#pip install gensim
#from gensim.models import Word2Vec
#from nltk.corpus import brown # , #movie_review
import numpy as np
#from textblob import TextBlob as tb
import tensorflow as tf
import random
import os
import time


# In[21]:


def read_glove_vec(glove_file):
    with open(glove_file,encoding='utf8') as f:
        words = set()
        word_to_vec_map = {}
        for line in f:
            line = line.strip().split()
            curr_word = line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)
        
        i = 1
        words_to_index = {}
        index_to_words = {}
        for w in sorted(words):
            words_to_index[w] = i
            index_to_words[i] = w
            i = i + 1
    return words_to_index, index_to_words, word_to_vec_map


# In[22]:


#word_to_index, index_to_word, word_to_vec_map = read_glove_vec('C:/Users/gokul/Documents/Deep_learning/New folder/C5W2A2 - Emojify - v2/data/glove.6B.50d.txt')
word_to_index = 400000
# word = "expired"
# index = 289846
# print("the index of", word, "in the vocabulary is", word_to_index[word])
# print("the", str(index) + "th word in the vocabulary is", index_to_word[index])


# In[2]:


X = np.load('/data/X.npy')
Y = np.load('/data/Y.npy')
X_embedings = np.load('/data/X_embedings.npy')
Y_embedings = np.load('/data/Y_embedings.npy')


# In[4]:


print(X.shape)
print(Y.shape)


# In[5]:


x_seq_length = len(X[1])
y_seq_length = len(Y[1])- 1
print(y_seq_length)


# In[58]:


def random_mini_batches(X, Y, X_embedings, Y_embedings, mini_batch_size = 128, seed = 0):
    
    X = X.T
    Y = Y.T
    #print(Y.shape)
    m = X.shape[1]                  # number of training examples
#     print(m)
    mini_batches = []
    np.random.seed(seed)
    
    # Step 1: Shuffle (X, Y)
    permutation = list(np.random.permutation(m))
    shuffled_X = X[:, permutation]
    shuffled_Y = Y[:, permutation] ##.reshape((Y.shape[0],m))
    shuffled_X_embedings = X_embedings[permutation,:]
    shuffled_Y_embedings = Y_embedings[permutation,:]

    # Step 2: Partition (shuffled_X, shuffled_Y). Minus the end case.
    num_complete_minibatches = math.floor(m/mini_batch_size) # number of mini batches of size mini_batch_size in your partitionning
    for k in range(0, num_complete_minibatches):
        mini_batch_X = shuffled_X[:, k * mini_batch_size : k * mini_batch_size + mini_batch_size]
        mini_batch_Y = shuffled_Y[:, k * mini_batch_size : k * mini_batch_size + mini_batch_size]
        mini_batch_X_emb = shuffled_X_embedings[ k * mini_batch_size : k * mini_batch_size + mini_batch_size,:]
        mini_batch_Y_emb = shuffled_Y_embedings[k * mini_batch_size : k * mini_batch_size + mini_batch_size,:]
        mini_batch = (mini_batch_X.T, mini_batch_Y.T, mini_batch_X_emb,mini_batch_Y_emb )
        mini_batches.append(mini_batch)
    
    # Handling the end case (last mini-batch < mini_batch_size)
    if m % mini_batch_size != 0:
        mini_batch_X = shuffled_X[:, num_complete_minibatches * mini_batch_size : m]
        mini_batch_Y = shuffled_Y[:, num_complete_minibatches * mini_batch_size : m]
        mini_batch_X_emb = shuffled_X_embedings[num_complete_minibatches * mini_batch_size : m,:]
        mini_batch_Y_emb = shuffled_Y_embedings[num_complete_minibatches * mini_batch_size : m, :]
        mini_batch = (mini_batch_X.T, mini_batch_Y.T, mini_batch_X_emb, mini_batch_Y_emb)
        mini_batches.append(mini_batch)
    
    return mini_batches


# In[59]:


tem = random_mini_batches(X,Y, X_embedings, Y_embedings)
print(len(tem))
tem1 = tem[1]
tem2,tem3,tem4,tem5 = tem1
print(tem2.shape)
print(tem3.shape)
print(tem4.shape)
print(tem5.shape)
# 5079//128

#len(word_to_index)


# In[64]:


epochs = 2
# batch_size = 128
minibatch_size = 128
nodes = 64
embed_size = 10

tf.reset_default_graph()
sess = tf.InteractiveSession()

inputs = tf.placeholder(tf.int32, (None, x_seq_length), 'inputs')
outputs = tf.placeholder(tf.int32, (None, None), 'output')
targets = tf.placeholder(tf.int32, (None, None), 'targets')

ques_input_embedding = tf.placeholder(tf.float32, (None, 35,50),'ques_input_embedding')
ques_output_embedding = tf.placeholder(tf.float32,(None, None, 50),'ques_output_embedding')

with tf.variable_scope("encoding") as encoding_scope:
    lstm_enc = tf.contrib.rnn.BasicLSTMCell(nodes)
    _, last_state = tf.nn.dynamic_rnn(lstm_enc, inputs=ques_input_embedding, dtype=tf.float32)

with tf.variable_scope("decoding") as decoding_scope:
    lstm_dec = tf.contrib.rnn.BasicLSTMCell(nodes)
    dec_outputs, _ = tf.nn.dynamic_rnn(lstm_dec, inputs=ques_output_embedding, initial_state=last_state)
    
logits = tf.contrib.layers.fully_connected(dec_outputs, num_outputs=word_to_index, activation_fn=None) 
with tf.name_scope("optimization"):
#     print(logits.get_shape().as_list())
#     print(targets.get_shape().as_list())
    loss = tf.contrib.seq2seq.sequence_loss(logits, targets, tf.ones([minibatch_size, 100]))
    optimizer = tf.train.RMSPropOptimizer(1e-3).minimize(loss)


# In[65]:


print(dec_outputs.get_shape().as_list())
print(last_state[0].get_shape().as_list())
print(ques_input_embedding.get_shape().as_list())
print(logits.get_shape().as_list())
print(targets.get_shape().as_list())


# In[ ]:



sess.run(tf.global_variables_initializer())
epochs = 10
for epoch_i in range(1):
    start_time = time.time()
#     m = 5079
#     num_minibatches = int(m / minibatch_size)
#     print(num_minibatches)
    minibatches = random_mini_batches(X, Y, X_embedings, Y_embedings)
#     print(X.shape)
#     print(Y.shape)
#     print(len(minibatches))
    
    for minibatch in minibatches:
        (minibatch_X, minibatch_Y, minibatch_X_emb, minibatch_Y_emb) = minibatch
#         print(minibatch_X_emb.shape)
#         print(minibatch_Y_emb.shape)
        print(minibatch_Y[:, 1:].shape)
        _, batch_loss, batch_logits = sess.run([optimizer, loss, logits],
            feed_dict = {inputs: minibatch_X,
             outputs: minibatch_Y[:, :-1],
             targets: minibatch_Y[:, 1:],
             ques_input_embedding: minibatch_X_emb,
             ques_output_embedding: minibatch_Y_emb[:,:-1]})

    print('Epoch {:3} Loss: {:>6.3f} Accuracy: {:>6.4f} Epoch duration: {:>6.3f}s'.format(epoch_i, batch_loss, 
                                                                      100, time.time() - start_time))

