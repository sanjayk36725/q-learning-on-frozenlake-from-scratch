# 🧊 Q-Learning on FrozenLake from Scratch

> A complete implementation of tabular Q-learning with epsilon-greedy exploration. Build an intelligent agent that learns to navigate a frozen lake environment from the ground up.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square&logo=python)
![Deep Learning](https://img.shields.io/badge/Type-Reinforcement%20Learning-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

</div>

---

## 📚 Overview

This project implements **tabular Q-learning** from scratch—no frameworks, just core algorithms. You'll learn how RL agents make decisions, explore their environment, and incrementally improve through temporal difference (TD) learning.

### What You'll Build

An agent that starts clueless about the frozen lake and gradually learns:
- ❄️ Where to step safely
- 🎯 How to reach the goal  
- ⚖️ The trade-off between exploration and exploitation

The agent gets **smarter with every episode**, using Q-values to encode its knowledge and epsilon-decay to shift from curiosity to confidence.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- `gym` (or `gymnasium` for newer versions)
- `numpy`

### Installation

```bash
# Clone and navigate
git clone <your-repo-url>
cd frozenlake-qlearning

# Install dependencies
pip install gymnasium numpy
```

### Run

```bash
python scaffold.py
```

This trains your Q-learning agent and evaluates its learned policy on fresh episodes.

---

## 🧠 Core Components

The project breaks down Q-learning into 16 carefully ordered steps:

### 1️⃣ **Foundation** (Steps 1–5)
Initialize the agent's knowledge and decision-making mechanics:

| Step | Function | Purpose |
|------|----------|---------|
| **1** | `init_q_table` | Create empty Q-values for all state-action pairs |
| **2** | `max_q_value` | Find the best next action's Q-value |
| **3** | `greedy_action` | Pick the best-known action (exploitation) |
| **4** | `sample_random_action` | Pick a random action (exploration) |
| **5** | `should_explore` | Decide whether to explore (epsilon-based) |

### 2️⃣ **Exploration Strategy** (Steps 6–7)
Balance curiosity with confidence:

| Step | Function | Purpose |
|------|----------|---------|
| **6** | `epsilon_greedy_action` | Choose explore or exploit each step |
| **7** | `decay_epsilon` | Gradually shift from exploring to exploiting |

### 3️⃣ **Learning Algorithm** (Steps 8–10)
The heart of Q-learning—updating knowledge from experience:

| Step | Function | Purpose |
|------|----------|---------|
| **8** | `td_target` | Calculate what the Q-value should be |
| **9** | `td_error` | Measure how wrong your current estimate is |
| **10** | `q_learning_update` | Adjust Q-value toward the target |

### 4️⃣ **Training Loop** (Steps 11–13)
Run episodes and accumulate learning:

| Step | Function | Purpose |
|------|----------|---------|
| **11** | `interaction_step` | Take one action, observe reward and next state |
| **12** | `run_training_episode` | Execute one full training episode |
| **13** | `train_q_learning` | Run many episodes, updating Q-values throughout |

### 5️⃣ **Evaluation** (Steps 14–16)
Test the learned policy:

| Step | Function | Purpose |
|------|----------|---------|
| **14** | `extract_greedy_policy` | Convert Q-table into best-action-only policy |
| **15** | `run_greedy_episode` | Execute one episode using only best actions |
| **16** | `evaluate_success_rate` | Measure how often the agent succeeds |

---

## 📊 How Q-Learning Works

### The Update Rule

```
Q(s,a) ← Q(s,a) + α [ r + γ·max Q(s',a') - Q(s,a) ]
```

**Where:**
- **s** = current state (position on ice)
- **a** = action taken (direction)
- **r** = reward received (1 if goal, 0 otherwise, -1 if hole)
- **s'** = next state  
- **α** = learning rate (how fast to learn)
- **γ** = discount factor (value of future rewards)

### Epsilon-Greedy Strategy

- **Probability ε:** Pick a random action → *Explore*
- **Probability 1-ε:** Pick the best known action → *Exploit*
- **Over time:** ε decays, shifting the agent from explorer to expert

---

## 🎮 Project Structure

```
frozenlake-qlearning/
├── scaffold.py              # Main training script
├── README.md                # This file
├── requirements.txt         # Dependencies
└── results/                 # (Optional) Training metrics & plots
    ├── training_log.csv
    └── policy_visualization.png
```

---

## 💡 Key Concepts

### Temporal Difference (TD) Learning
The agent learns by comparing its prediction (old Q-value) to a new observation (reward + future estimate). The gap is the **TD error**—how surprised the agent was.

### State-Action Values (Q-Values)
A table where `Q[state][action]` = "expected reward if I take this action from this state and act optimally after."

### Exploration vs. Exploitation
- **Exploration:** Try new things, discover their value
- **Exploitation:** Use what you've learned to maximize reward
- **Epsilon-decay:** Gradually phase out exploration as you gain confidence

---

## 🔧 Customization

Tune these hyperparameters in `scaffold.py`:

```python
# Learning rate: how much to adjust Q-values per update
LEARNING_RATE = 0.1

# Discount factor: how much to value future rewards
DISCOUNT_FACTOR = 0.99

# Initial exploration probability
EPSILON_START = 1.0

# How quickly epsilon decays
EPSILON_DECAY_RATE = 0.995

# Total training episodes
NUM_EPISODES = 1000

# Max steps per episode (prevents infinite loops)
MAX_STEPS = 100
```

---

## 📈 Expected Results

After training:
- ✅ **Success Rate:** 70-90% on fresh episodes
- ✅ **Learning Curve:** Steep initial improvement, then plateau
- ✅ **Policy:** Clear path from start to goal learned

Typical progression:
- Episodes 0–100: Chaotic, lots of failing
- Episodes 100–500: Steady improvement
- Episodes 500+: Consistent success (plateau)

---

## 🎓 Learning Path

**New to RL?** Follow the steps in order:
1. Understand Q-tables (Step 1)
2. Learn greedy selection (Steps 2–3)
3. Add randomness (Steps 4–5)
4. Implement epsilon-greedy (Steps 6–7)
5. Understand TD learning (Steps 8–10)
6. Build training loops (Steps 11–13)
7. Evaluate your agent (Steps 14–16)

Each step builds on the previous—this is how RL algorithms are actually constructed!

---

## 🔗 Resources

- [Sutton & Barto's "Reinforcement Learning: An Introduction"](http://incompleteideas.net/book/the-book-2nd.html) – The RL Bible
- [OpenAI Gym Documentation](https://gymnasium.farama.org/) – Environment specs
- [David Silver's RL Course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) – Free lectures

---

## 🙌 Credits

Built on [Deep-ML](https://github.com/The-ML-Curve/Deep-ML) – a collection of ML algorithms from scratch.

---

## 📝 License

MIT License – Feel free to use, modify, and share!

---

<div align="center">

**Made with ❤️ for RL learners**

[⭐ Star this repo](#) if it helped you learn! | [🐛 Report issues](#) | [💬 Discussions](#)

</div>
