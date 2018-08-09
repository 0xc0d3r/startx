### Hyper Parameters
  * No. of hidden layers
      - Complexity
      - Chance of over-fitting increases
      - Chance of finding good local minima
  * No. of neurons in each hidden layer
      - it's better to increase no. of hidden layers rather than no. of neurons
  * Various activation functions
      - sigmoid
          * Vanishing & Exploding gradient problem
      - tanh
          * A slight modification of `sigmoid`
          * Vanishing & Exploding gradient problem
      - relu
          * 6 times faster than `tanh` and `sigmoid`
  * Learning rate
      if increase:
         - chance of missing local minimas
         - oscillations might happen
         - error rate also might increase
      if decreases:
         - will take too much time & need more computational power
  * No. of iterations
      if increases:
         - will take more time
         - accuracy will improve if leanring rate is less
         - error rate may increase
  * Loss functions
  * Various optimization algos
       - Adam algo is efficient
  * Batch size
      if large value:
         - need more computational power because we have to find slope for parameters
      if small value:
         - noise
  * Regularlization:
        - Dropout
        - Batch normalization
  * Variable initiliazations
  
       
