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
        self.df = self.df.sample(frac=1).reset_index(drop=True)
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

class dnn_model():
    def __init__(self, file_path:str):
        self.data = pd.read_csv(file_path)
        self.df = pd.DataFrame(self.data)
        self.df = self.df.sample(frac=1).reset_index(drop=True)
        self.kfold = KFold(n_splits=5)

    def feature_input(self):
        self.content = self.df['text'].values
        self.type = self.df['type'].values
        self.user_cred = self.df['user_credibility'].values
        self.user_verf = self.df['verified'].values

    def embedding_feature(self):
        self.text_embedding = hub.text_embedding_column(
            "content", 
            module_spec="https://tfhub.dev/google/nnlm-en-dim128-with-normalization/1",
            # module_spec="https://tfhub.dev/google/Wiki-words-250-with-normalization/1",
            trainable=False
        )

        self.user_cred_feature = tf.feature_column.numeric_column("user_credibility")
        self.user_verf_feature = tf.feature_column.numeric_column("user_verified")

    def model_setup(self):
        # self.binary_label_head = tf.contrib.estimator.binary_classification_head(
        #     loss_reduction=tf.losses.Reduction.SUM_OVER_BATCH_SIZE
        # )

        # self.estimator = tf.estimator.DNNEstimator(
        #     head=self.binary_label_head,
        #     hidden_units=[128,64],
        #     feature_columns=[self.text_embedding, self.user_cred_feature, self.user_verf_feature],
        #     batch_norm=True,
        #     model_dir="./estimator_dnn"
        # )

        self.estimator = tf.estimator.DNNClassifier(
            n_classes=2,
            hidden_units=[128,64],
            feature_columns=[self.text_embedding, self.user_cred_feature, self.user_verf_feature],
            batch_norm=True,
            model_dir="./estimator_single"
        )

        # self.estimator = tf.estimator.DNNLinearCombinedClassifier(
        #     dnn_feature_columns=[self.text_embedding, self.user_verf_feature, self.user_cred_feature],
        #     dnn_hidden_units=[128,64],
        #     batch_norm=True,
        #     model_dir='./estimator_linear_classifier'
        # )

        # self.estimator = tf.estimator.LinearClassifier(
        #     feature_columns=[self.text_embedding, self.user_cred_feature, self.user_verf_feature],
        #     optimizer='Adagrad',
        #     model_dir='./estimator_linear'
        # )

    def restore_saved_model(self):
        print("start restoring model")
        self.estimator = tf.estimator.DNNClassifier(
            hidden_units=[128,64],
            feature_columns=[self.text_embedding, self.user_cred_feature, self.user_verf_feature],
            warm_start_from="./estimator_dnn"
        )

    def train_model(self):
        for train_index, test_index in self.kfold.split(self.type):

            self.train_content = self.content[train_index].astype(np.str)
            self.train_verf = self.user_verf[train_index].astype(np.float)
            self.train_cred = self.user_cred[train_index].astype(np.float)
            self.train_type = self.type[train_index].astype(np.int32)

            self.test_content = self.content[test_index].astype(np.str)
            self.test_verf = self.user_verf[test_index].astype(np.float)
            self.test_cred = self.user_cred[test_index].astype(np.float)
            self.test_type = self.type[test_index].astype(np.int32)

            features = {
                "content": self.train_content,
                "user_credibility": self.train_cred,
                "user_verified": self.train_verf
            }
            labels = self.train_type

            train_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn(
                features, 
                labels, 
                shuffle=False, 
                batch_size=64, 
                num_epochs=10
            )

            print("start training")
            self.estimator.train(input_fn=train_input_fn)

    def test_model(self):
        eval_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn({
                        "content": self.test_content,
                        "user_credibility": self.test_cred,
                        "user_verified": self.test_verf
                        },  
                        self.test_type,
                        shuffle=False 
                        )

        print("start predicting")
        print(self.estimator.evaluate(input_fn=eval_input_fn))

    def predict_model(self, content:list, verified:list, credibility:list):
        eval_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn({
                        "content": np.array(content),
                        "user_credibility": np.array(credibility),
                        "user_verified": np.array(verified)
                        },  
                        shuffle=False 
                        )

        print("start predicting")
        return self.estimator.predict(input_fn=eval_input_fn)