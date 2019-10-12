import numpy as np
import pandas as pd

import tensorflow as tf
import tensorflow_hub as hub

print("start")
data = pd.read_csv('./clean_dataset.csv')
df = pd.DataFrame(data)
df = df.sample(frac=1).reset_index(drop=True)

content = df['text']
type = df['type']
title = df['title']
author = df['authors']
url = df['url']


train_size = int(len(content) * .8)

train_content = content[:train_size].astype('str')
train_author = author[:train_size].astype('str')
train_title = title[:train_size].astype('str')
train_url = url[:train_size].astype('str')
train_type = type[:train_size]
train_testing = np.random.rand(len(train_type), 1)

test_content = content[train_size:].astype('str')
test_author = author[train_size:].astype('str')
test_title = title[train_size:].astype('str')
test_url = url[train_size:].astype('str')
test_type = type[train_size:]
test_testing = np.random.rand(len(test_type), 1)

# text_embedding = hub.text_embedding_column(
#     "content", 
#     module_spec="https://tfhub.dev/google/universal-sentence-encoder/2",
#     trainable=False
# )

# text_embedding = hub.text_embedding_column(
#     "content", 
#     module_spec="https://tfhub.dev/google/elmo/2",
#     trainable=False
# )

text_embedding = hub.text_embedding_column(
    "content", 
    module_spec="https://tfhub.dev/google/nnlm-en-dim128-with-normalization/1",
    trainable=False
)

title_embedding = hub.text_embedding_column(
    "title", 
    module_spec="https://tfhub.dev/google/nnlm-en-dim128-with-normalization/1",
    trainable=False
)

author_embedding = hub.text_embedding_column(
    "author", 
    module_spec="https://tfhub.dev/google/nnlm-en-dim128-with-normalization/1",
    trainable=False
)

url_embedding = hub.text_embedding_column(
    "url", 
    module_spec="https://tfhub.dev/google/nnlm-en-dim128-with-normalization/1",
    trainable=False
)

test = tf.feature_column.numeric_column("test")

# text_embedding = hub.text_embedding_column(
#     "content", 
#     module_spec="https://tfhub.dev/google/Wiki-words-500-with-normalization/1"
# )

# train_input_fn = tf.estimator.inputs.pandas_input_fn(
#     train_content, train_type, num_epochs=10, shuffle=True, batch_size=32)

# predict_test_input_fn = tf.estimator.inputs.pandas_input_fn(
#     test_content, test_type, shuffle=False)

binary_label_head = tf.contrib.estimator.binary_classification_head(
    loss_reduction=tf.losses.Reduction.SUM_OVER_BATCH_SIZE
)

estimator = tf.estimator.DNNEstimator(
    head=binary_label_head,
    hidden_units=[64,32],
    feature_columns=[text_embedding, title_embedding, author_embedding, url_embedding, test],
    batch_norm=True
    # model_dir="./estimator"
)

features = {
    "content": np.array(train_content),
    "title": np.array(train_title), 
    "author": np.array(train_author),
    "url": np.array(train_url),
    "test": train_testing
}
labels = np.array(train_type).astype(np.int32)

# train_input_fn = tf.data.Dataset.from_tensor_slices((features, labels)).shuffle(42).batch(32).repeat(10)

train_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn(
    features, 
    labels, 
    shuffle=True, 
    batch_size=128, 
    num_epochs=10
)

print("start training")
print(estimator.train(input_fn=train_input_fn))

eval_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn({
                "content": np.array(test_content).astype(np.str),
                "title": np.array(test_title).astype(np.str),
                "author": np.array(test_author).astype(np.str),
                "url": np.array(test_url).astype(np.str),
                "test": test_testing
                }, 
                np.array(test_type).astype(np.int32), 
                shuffle=True 
                )

print("start testing")
print(estimator.evaluate(input_fn=eval_input_fn))

raw_content_test = [
    "Why won't the Corupt Fake News blame Low IQ Rick Perry for my crimes?! Its NOT MY FAULT that I bribed Ukraine to interfere with the 2020 US election! Dumb as a rock Rick Perry made me do it! Rick Perry says stuff and keeps outsmarting me! Treason!",
    "Another armed man decides it’s time for his entire family to die before killing himself - this time in Massachusetts. A majority of mass shootings in America are instigated by domestic violence.",
    "Tariffs are forcing China to pay attention to US concerns, US Secretary of Commerce Wilbur Ross said on Thursday (Oct 10). Mr Ross said the United States would have preferred not to implement tariffs against Chinese goods more than a year ago, which ignited a trade war that slowed global commerce and threatened decades-old systems, but added that it has forced Beijing into action.\nThe trade war has weighed on global growth and roiled financial markets.\n\"We do not love tariffs, in fact we would prefer not to use them, but after years of discussions and no action, tariffs are finally forcing China to pay attention to our concerns,\"\nMr Ross told a business function held by the American Chamber of Commerce in Australia.\n\"We could have had a deal two-and-a-half years ago without going through the whole tit-for-tat on tariffs that we have.\" \nMr Ross is on an official visit to Australia. \nTop US and Chinese trade and economic officials will meet in Washington on Thursday and Friday to try to end a 15-month-old trade war."
    ]

raw_title_test = [
    "",
    "",
    "US tariffs on China are working, says Secretary of Commerce Wilbur Ross"
]

raw_author_test = [
    "Donald J. Trump",
    "Shannon Watts",
    ""
]

raw_url_test = [
    "",
    "www.bostonglobe.com",
    "www.straitstimes.com"
]

predict_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn({
                "content": np.array(raw_content_test).astype(np.str),
                "title": np.array(raw_title_test).astype(np.str),
                "author": np.array(raw_author_test).astype(np.str),
                "url": np.array(raw_url_test).astype(np.str)
                }, 
                shuffle=False
                )
results = estimator.predict(predict_input_fn)
for each in results:
    print(each)