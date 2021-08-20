import numpy as np

def Qlearning(environment, num_episodes=100, alpha=0.3, gamma=0.9, epsilon=1.0, decay_epsilon=0.1, max_epsilon=1.0,
              min_epsilon=0.01):
    # initializing the Q-table
    Q = np.zeros((environment.observation_space.n, environment.action_space.n))

    # additional lists to keep track of reward and epsilon values
    rewards = []
    epsilons = []

    print_count = 0
    # episodes
    for episode in range(num_episodes):

        # reset the environment to start a new episode
        state = environment.reset()

        # reward accumulated along episode
        accumulated_reward = 0

        # steps within current episode
        for step in range(300):

            # epsilon-greedy action selection
            # exploit with probability 1-epsilon
            if np.random.uniform(0, 1) > epsilon:
                action = np.argmax(Q[state, :])

            # explore with probability epsilon
            else:
                action = environment.action_space.sample()

            # perform the action and observe the new state and corresponding reward
            new_state, reward, done, info = environment.step(action)

            # update the Q-table
            Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])

            # update the accumulated reward
            accumulated_reward += reward

            # update the current state
            state = new_state

            # end the episode when it is done
            if done == True:
                break

        # decay exploration rate to ensure that the agent exploits more as it becomes experienced
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_epsilon * episode)

        # update the lists of rewards and epsilons
        rewards.append(accumulated_reward)
        epsilons.append(epsilon)
        environment.print_infos(episode, accumulated_reward)


    # render the environment
    environment.render()

    # return the list of accumulated reward along episodes
    return rewards