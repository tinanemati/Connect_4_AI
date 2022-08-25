# Project-2
  Part II: Coding the Agent
  Using minimax with alpha-beta pruning, code your algorithm to play the game. 
  
  To make things easier and faster for us to read and go over the code, we took advantage of Michael's implementaion of min and max in PA2 helper video.
  
  we have methods called: 'def MAX(self, env, prev_move, depth, alpha, beta)`and def MIN(self, env, prev_move, depth, alpha, beta)` that return the 
  updated value of '`MIN` and updated value of `MAX` for us, so we are able to store that in `max_v`and `min_v` variables. Afterwards, we will save and   
  make the next move using our driver function. 
  
  Using our minimax implementation with alpha-beta pruning, allowed us to play faster since we are able to prune some nodes and don't go through them, as 
  result we are winning most of the 20 games. 
  
  
  
  In order to imrpove the efficiency of our program: 
  1. we decided to change the weight of our evalution function, to be able to block the opponent, this helped us play much faster and better.
  2. we decided to play around with our depth, having depth of 3 and 5 was too high for our minimax to select the best move, so we decreased it to 2. 
  3. we decided to order our nodes in the most optimal order(center column gets evaluted first and then we move to edge columns [3,2,4,1,5,0,6] instead 
  of [0,1,2,3,4,5,6], however, after implementation we noticed that our agent hasn't imrpoved as much and as a matter of fact, we are losing more games, 
  so we decided to put it back to the prev implementation. 
  
  
  
  
  Part III: Evaluation Function
  Evaluate your agent against the benchmark agents.
  
  ● OurAgent vs StupidAI:
  
  | games         | OurAgent - p1 vs. StupidAI -p2| StupidAI - p1 vs. OurAgent - p2 |
  | ------------- | ------------- | --------      |
  | game 1| p1 wins         | p2 wins             |    
  | game 2| p1 wins      | p2 wins             |
  
  ● OurAgent vs RandomAI -- 5 times:
  | games         | OurAgent - p1 vs. RandomAI -p2| RandomAI - p1 vs. OurAgent - p2 |
  | ------------- | ------------- | --------      |
  | seed 0| p1 wins         | p2 wins             |    
  | seed 1| p1 wins         | p2 wins             |
  | seed 2| p1 wins         | p2 wins             |    
  | seed 3| p1 wins       | p2 wins             |
  | seed 4| p1 wins       | p2 wins             |
  
  ● OurAgent vs MonteCarloAI -- 10 times:
  | games         | OurAgent - p1 vs. MonteCarloAI -p2| MonteCarloAI - p1 vs. OurAgent - p2 |
  | ------------- | ------------- | --------            |
  | seed 0| p1 wins               | p2 wins             |    
  | seed 1| p1 wins          | p2 loses             |
  | seed 2| p1 wins               | p2 wins             |    
  | seed 3| p1 wins          | p2 wins             |
  | seed 4| p1 wins               | p2 wins             |
  | seed 5| p1 wins               | p2 wins             |    
  | seed 6| p1 wins              | p2 wins             |
  | seed 7| p1 wins               | p2 wins             |    
  | seed 8| p1 wins              | p2 wins             |
  | seed 9| p1 wins              | p2 wins             |
  
  
