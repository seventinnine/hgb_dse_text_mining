# CNN

```python
from tensorflow.keras.models import *
from tensorflow.keras.layers import *

model = Sequential()
# max_length = max length of your tokenized texts, embedding_dimensions = word2vec dimensions (usually 300)
model.add(Conv1D(nr_of_filters, kernel_size, padding = padding, activation = "relu", input_shape = (max_length, embedding_dimensions)))
model.add(GlobalMaxPooling1D())
model.add(Dense(nr_hidden_units))
model.add(Dropout(0.2))
model.add(Activation("relu"))
model.add(Dense(1))
model.add(Activation("sigmoid"))

# callbacks
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
callbacks = []
callbacks.append(EarlyStopping(monitor = "val_loss", patience = 15, verbose = 0, mode = "auto"))
callbacks.append(ModelCheckpoint(model_name + "_check_.h5", save_best_only = True, monitor = "val_loss", mode = "min"))

# binary classification
model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ["accuracy"])
model.fit(X_train, y_train, batch_size = batch_size, epochs = epochs , validation_data = (X_val, y_val), callbacks = callbacks, verbose = 1)
```

****

# RNN

```python
from tensorflow.keras.models import *
from tensorflow.keras.layers import *

model = Sequential()
# max_length = max length of your tokenized texts, embedding_dimensions = word2vec dimensions (usually 300)
model.add(Input(shape = (max_length, embedding_dimensions))
model.add(SpatialDropout1D(rate = 0.1))
model.add(Bidirectional(GRU(256), merge_mode = "ave"))
model.add(Dropout(0.1))
model.add(Dense(256, activation = "relu"))
model.add(Dense(1))
model.add(Activation("sigmoid"))

# callbacks
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
callbacks = []
callbacks.append(EarlyStopping(monitor = "val_loss", patience = 15, verbose = 0, mode = "auto"))
callbacks.append(ModelCheckpoint(model_name + "_check_.h5", save_best_only = True, monitor = "val_loss", mode = "min"))

# binary classification
model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ["accuracy"])
model.fit(X_train, y_train, batch_size = batch_size, epochs = epochs , validation_data = (X_val, y_val), callbacks = callbacks, verbose = 1)
```

****
