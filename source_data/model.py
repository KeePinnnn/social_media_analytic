import numpy as np
import pandas as pd

import tensorflow as tf
import tensorflow_hub as hub

from sklearn.preprocessing import MultiLabelBinarizer

print("start")
data = pd.read_csv('./clean_dataset.csv')
df = pd.DataFrame(data)

content = df['text']
type = df['type']


train_size = int(len(content) * .8)

train_content = content[:train_size]
train_type = type[:train_size]

test_content = content[train_size:]
test_type = type[train_size:]

text_embedding = hub.text_embedding_column(
    "content", 
    module_spec="https://tfhub.dev/google/universal-sentence-encoder/2"
)

# text_embedding = hub.text_embedding_column(
#     "content", 
#     module_spec="https://tfhub.dev/google/elmo/2"
# )

# text_embedding = hub.text_embedding_column(
#     "content", 
#     module_spec="https://tfhub.dev/google/nnlm-en-dim50-with-normalization/1"
# )

# text_embedding = hub.text_embedding_column(
#     "content", 
#     module_spec="https://tfhub.dev/google/Wiki-words-500-with-normalization/1"
# )

print("encoder encoding")
encoder = MultiLabelBinarizer()
encoder.fit_transform(train_type)
train_encoded = encoder.transform(train_type)
test_encoded = encoder.transform(test_type)
num_classes = len(encoder.classes_)
print(num_classes)

binary_label_head = tf.contrib.estimator.binary_classification_head(
    num_classes,
    loss_reduction=tf.losses.Reduction.SUM_OVER_BATCH_SIZE
)

estimator = tf.contrib.estimator.DNNEstimator(
    head=binary_label_head,
    hidden_units=[64,10],
    feature_columns=[text_embedding]
)

features = {
  "content": np.array(train_content)
}
labels = np.array(train_encoded)

train_input_fn = tf.estimator.inputs.numpy_input_fn(
    features, 
    labels, 
    shuffle=True, 
    batch_size=32, 
    num_epochs=1000
)

print("start training")
estimator.train(input_fn=train_input_fn)

eval_input_fn = tf.estimator.inputs.numpy_input_fn({"content": np.array(test_content).astype(np.str)}, test_encoded.astype(np.int32), shuffle=False)

print("start testing")
estimator.evaluate(input_fn=eval_input_fn)