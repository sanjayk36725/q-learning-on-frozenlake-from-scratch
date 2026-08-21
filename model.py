"""
Q-Learning on FrozenLake from Scratch

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - init_q_table
import numpy as np

def init_q_table(num_states, num_actions):
    return np.zeros((num_states, num_actions), dtype=np.float64)

# Step 2 - max_q_value
import numpy as np

def max_q_value(q_table, state):
    return np.max(q_table[state])

# Step 3 - greedy_action
import numpy as np

def greedy_action(q_table, state):
    return int(np.argmax(q_table[state]))

# Step 4 - sample_random_action
def sample_random_action(action_space):
    return int(action_space.sample())

# Step 5 - should_explore
import numpy as np

def should_explore(epsilon, rng):
    return bool(rng.random() < epsilon)

# Step 6 - epsilon_greedy_action
def epsilon_greedy_action(q_table, state, epsilon, action_space, rng):
    if should_explore(epsilon, rng):
        return sample_random_action(action_space)
    return greedy_action(q_table, state)

# Step 7 - decay_epsilon
def decay_epsilon(epsilon, decay_rate, min_epsilon):
    return max(epsilon * decay_rate, min_epsilon)

# Step 8 - td_target
def td_target(reward, gamma, q_table, next_state, done):
    if done:
        return float(reward)
    return float(reward + gamma * max_q_value(q_table, next_state))

# Step 9 - td_error
def td_error(target, q_table, state, action):
    return float(target - q_table[state, action])

# Step 10 - q_learning_update
def q_learning_update(q_table, state, action, reward,
                      next_state, done, alpha, gamma):
    target = td_target(
        reward, gamma, q_table, next_state, done
    )

    error = td_error(
        target, q_table, state, action
    )

    q_table[state, action] += alpha * error

    return float(q_table[state, action])

# Step 11 - interaction_step
def interaction_step(env, q_table, state, epsilon, alpha, gamma, rng):
    action = epsilon_greedy_action(
        q_table, state, epsilon, env.action_space, rng
    )

    next_state, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated

    q_learning_update(
        q_table,
        state,
        action,
        reward,
        next_state,
        done,
        alpha,
        gamma
    )

    return int(next_state), float(reward), bool(done)

# Step 12 - run_training_episode
def run_training_episode(env, q_table, epsilon, alpha, gamma, rng, max_steps):
    state, _ = env.reset()
    total_reward = 0.0

    for _ in range(max_steps):
        state, reward, done = interaction_step(
            env,
            q_table,
            state,
            epsilon,
            alpha,
            gamma,
            rng
        )

        total_reward += reward

        if done:
            break

    return float(total_reward)

# Step 13 - train_q_learning
def train_q_learning(env, num_episodes, seed=None,
                      alpha=0.8, gamma=0.95,
                      epsilon_start=1.0, epsilon_end=0.01,
                      epsilon_decay=0.995, max_steps=100):
    rng = np.random.default_rng(seed)
    env.action_space.seed(seed)
    env.reset(seed=seed)

    n_states = env.observation_space.n
    n_actions = env.action_space.n
    q_table = init_q_table(n_states, n_actions)

    epsilon = epsilon_start
    episode_returns = []

    for _ in range(num_episodes):
        ep_return = run_training_episode(
            env, q_table, epsilon, alpha, gamma, rng, max_steps
        )
        episode_returns.append(ep_return)
        epsilon = decay_epsilon(epsilon, epsilon_decay, epsilon_end)

    return q_table, episode_returns

# Step 14 - extract_greedy_policy (not yet solved)
# TODO: implement

# Step 15 - run_greedy_episode (not yet solved)
# TODO: implement

# Step 16 - evaluate_success_rate (not yet solved)
# TODO: implement

