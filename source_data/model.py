import numpy as np
import pandas as pd

import tensorflow as tf
import tensorflow_hub as hub

from sklearn.model_selection import KFold

class embedding_model():
    def __init__(self, file_path:str):
        self.data = pd.read_csv(file_path)
        self.df = pd.DataFrame(self.data)
        self.df['username'] = self.df['username'].fillna('')
        # self.df = self.df.sample(frac=1).reset_index(drop=True)
        self.kfold = KFold(n_splits=5)

    def feature_input(self):
        self.content = self.df['text'].values
        self.type = self.df['type'].values

    def embedding_feature(self):
        self.text_embedding = hub.text_embedding_column(
            "content", 
            module_spec="https://tfhub.dev/google/nnlm-en-dim128-with-normalization/1",
            trainable=False
        )

    def model_setup(self):
        self.binary_label_head = tf.contrib.estimator.binary_classification_head(
            loss_reduction=tf.losses.Reduction.SUM_OVER_BATCH_SIZE
        )

        self.estimator = tf.estimator.DNNEstimator(
            head=self.binary_label_head,
            hidden_units=[128,64],
            feature_columns=[self.text_embedding],
            batch_norm=True,
            model_dir="./estimator_training"
        )

    def train_model(self):
        for train_index, test_index in self.kfold.split(self.type):

            train_content = self.content[train_index].astype(np.str)
            train_type = self.type[train_index].astype(np.int32)

            test_content = self.content[test_index].astype(np.str)
            test_type = self.type[test_index].astype(np.int32)

            features = {
                "content": train_content,
            }
            labels = train_type

            train_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn(
                features, 
                labels, 
                shuffle=False, 
                batch_size=64, 
                num_epochs=10
            )

            print("start training")
            self.estimator.train(input_fn=train_input_fn)

    def test_model(self, train_content:object, test_content:object):
        eval_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn({
                        "content": train_content,
                        },  
                        test_content,
                        shuffle=False 
                        )

        print("start predicting")
        return self.estimator.evaluate(input_fn=eval_input_fn)

    def predict_model(self, content:object):
        eval_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn({
                        "content": content,
                        },  
                        shuffle=False 
                        )

        print("start predicting")
        return self.estimator.predict(input_fn=eval_input_fn)

# raw_content_test = [
#     "Why won't the Corupt Fake News blame Low IQ Rick Perry for my crimes?! Its NOT MY FAULT that I bribed Ukraine to interfere with the 2020 US election! Dumb as a rock Rick Perry made me do it! Rick Perry says stuff and keeps outsmarting me! Treason!",
#     "Another armed man decides it’s time for his entire family to die before killing himself - this time in Massachusetts. A majority of mass shootings in America are instigated by domestic violence.",
#     "Tariffs are forcing China to pay attention to US concerns, US Secretary of Commerce Wilbur Ross said on Thursday (Oct 10). Mr Ross said the United States would have preferred not to implement tariffs against Chinese goods more than a year ago, which ignited a trade war that slowed global commerce and threatened decades-old systems, but added that it has forced Beijing into action.\nThe trade war has weighed on global growth and roiled financial markets.\n\"We do not love tariffs, in fact we would prefer not to use them, but after years of discussions and no action, tariffs are finally forcing China to pay attention to our concerns,\"\nMr Ross told a business function held by the American Chamber of Commerce in Australia.\n\"We could have had a deal two-and-a-half years ago without going through the whole tit-for-tat on tariffs that we have.\" \nMr Ross is on an official visit to Australia. \nTop US and Chinese trade and economic officials will meet in Washington on Thursday and Friday to try to end a 15-month-old trade war."
#     ]

# raw_title_test = [
#     "",
#     "",
#     "US tariffs on China are working, says Secretary of Commerce Wilbur Ross"
# ]

# raw_author_test = [
#     "Donald J. Trump",
#     "Shannon Watts",
#     ""
# ]

# raw_url_test = [
#     "",
#     "www.bostonglobe.com",
#     "www.straitstimes.com"
# ]

# predict_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn({
#                 "content": np.array(raw_content_test).astype(np.str),
#                 "title": np.array(raw_title_test).astype(np.str),
#                 "author": np.array(raw_author_test).astype(np.str),
#                 "url": np.array(raw_url_test).astype(np.str)
#                 }, 
#                 shuffle=False
#                 )
# results = estimator.predict(predict_input_fn)
# for each in results:
#     print(each)