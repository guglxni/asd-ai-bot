import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class QuestionSelector(nn.Module):
    def __init__(self, state_size, hidden_size, action_size):
        super(QuestionSelector, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, action_size)
        )
        
    def forward(self, state):
        return self.network(state)

class RLAgent:
    def __init__(self, state_size, action_size, hidden_size=128):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.policy_net = QuestionSelector(state_size, hidden_size, action_size).to(self.device)
        self.target_net = QuestionSelector(state_size, hidden_size, action_size).to(self.device)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        
        self.optimizer = optim.Adam(self.policy_net.parameters())
        self.memory = []
        self.batch_size = 32
        self.gamma = 0.99
        self.epsilon = 0.1
        
    def select_question(self, state):
        if np.random.random() < self.epsilon:
            return np.random.randint(self.policy_net.network[-1].out_features)
            
        with torch.no_grad():
            state_tensor = torch.FloatTensor(state).to(self.device)
            q_values = self.policy_net(state_tensor)
            return q_values.argmax().item()
    
    def update_model(self, state, action, reward, next_state):
        # Store transition in memory
        self.memory.append((state, action, reward, next_state))
        
        if len(self.memory) < self.batch_size:
            return
            
        # Sample random batch from memory
        batch = random.sample(self.memory, self.batch_size)
        states, actions, rewards, next_states = zip(*batch)
        
        # Convert to tensors
        state_batch = torch.FloatTensor(states).to(self.device)
        action_batch = torch.LongTensor(actions).to(self.device)
        reward_batch = torch.FloatTensor(rewards).to(self.device)
        next_state_batch = torch.FloatTensor(next_states).to(self.device)
        
        # Compute Q values
        current_q_values = self.policy_net(state_batch).gather(1, action_batch.unsqueeze(1))
        next_q_values = self.target_net(next_state_batch).max(1)[0].detach()
        expected_q_values = reward_batch + self.gamma * next_q_values
        
        # Compute loss and update
        loss = nn.MSELoss()(current_q_values.squeeze(), expected_q_values)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step() 