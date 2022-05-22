#  Inputs: Each input corresponds to a feature.
# Weights: Each input also has a weight which assigns a
#          certain amount of importance to the input.
#  Output: Finally, the perceptron uses the inputs and weights
#          to produce an output.


class Perceptron:
    def __init__(self, num_inputs=3, weights=[1, 1, 1]):
        self.num_inputs = num_inputs
        self.weights = weights

    def weighted_sum(self, inputs, weights):
        # weighted_sum = x1 * w1 + x2 * w2 + ... + xn * wn
        weighted_sum = 0
        for i in range(self.num_inputs):
            weighted_sum += inputs[i] * weights[i]
        return weighted_sum

    def activation(self, weighted_sum):
        # An activation function is a function that converts the input
        # given into a certain output based on a set of rules.
        # 1. Hyperbolic Tangent: used to output a number from -1 to 1.
        # 2. Logistic Function: used to output a number from 0 to 1.
        if weighted_sum >= 0:
            return 1
        if weighted_sum < 0:
            return 0

    def training(self, training_set, max_iter=1000):
        still_error = True
        while still_error:
            total_error = 0
            prediction_list = []
            actual_list = []
            for inputs in training_set:
                prediction = self.activation(self.weighted_sum(inputs, self.weights))
                actual = training_set[inputs]
                prediction_list.append(prediction)
                actual_list.append(actual)
                error = actual - prediction
                total_error += abs(error)
                for i in range(self.num_inputs):
                    self.weights[i] += error * inputs[i]
            # print("Nº in:", self.num_inputs, " Weights:", self.weights)
            # print("Prediction: ", prediction_list)
            # print("Real Labels:", actual_list)
            # print("Total error: ", total_error)
            # print("-----------------------------")
            max_iter -= 1
            if total_error == 0:
                still_error = False
            elif max_iter == 0:
                break
        return self.weights, total_error

    def prediction(self, inputs, weights):
        prediction = self.activation(self.weighted_sum(inputs, self.weights))
        return prediction


cool_perceptron = Perceptron()
small_training_set = {(0, 0, 1): 0, (1, 0, 1): 0, (0, 1, 1): 0, (1, 1, 1): 1}
trained_weights, trained_error = cool_perceptron.training(small_training_set)
prediction = cool_perceptron.prediction((1, 1, 1), trained_weights)
print("New Weights:", trained_weights)
print("Error:", trained_error)
print("Prediction:", prediction)
