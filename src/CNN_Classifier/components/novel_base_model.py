# workflow configuration manager
import os
import urllib.request as request
from zipfile import ZipFile
from pathlib import Path
from CNN_Classifier.entity.config_entity import NovelBaseModelConfig
import tensorflow as tf


class NovelBaseModel:
    def __init__(self, config: NovelBaseModelConfig):
        self.config = config

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.param_image_size,
            weights=self.config.param_weights,
            include_top=self.config.param_include_top
        )
        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy']
        )

        full_model.summary()
        return full_model

    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.param_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.param_learning_rate
        )

        self.save_model(path=self.config.update_base_model_path, model=self.full_model)
