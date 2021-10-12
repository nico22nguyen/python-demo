import numpy
import sklearn.tree
from keras.models import Sequential, load_model
from keras.layers import Dense
import file_parser
print('imports successful')

#parse raw data into list format
train = file_parser.parse_csv("new_data.csv")
#test = file_parser.parse_csv("test.csv")
training_data = train[0]
training_labels = train[1]
#test_data = test[0]
#test_labels = test[1]
print('parse successful')

"""
#need 3 layers
model = Sequential()
model.add(Dense(64, activation = 'relu', input_dim = 784)) #input layer 64 neurons 784 inputs
model.add(Dense(64, activation = 'relu')) #hidden layer 64 neurons
model.add(Dense(10, activation = 'softmax')) #output layer 10 outputs
print('model setup successful')

#compile the model
#set stuff like loss function ?
model.compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['accuracy']
)
print('model compile successful')
"""
model = load_model("number_guesser")##import old model to train
#train model
model.fit(
    training_data,
    training_labels,
    epochs = 20, # num of iterations over the entire dataset to train on 
    batch_size = 32 # num of samples per gradient update
)
print('model training successful')
"""
#evaluate model
model.evaluate(
    test_data,
    test_labels
)
print('model eval successful')
"""
model.save("number_guesser")##save with msirp model