# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from MyEnv import MyEnv
from q_learning import Qlearning
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    my_env = MyEnv()
    my_env.render()

def test_env():
    env = MyEnv()

    obs = env.reset()
    env.render()

    print(env.observation_space)
    print(env.action_space)
    print(env.action_space.sample())

    GO_LEFT = 0
    # Hardcoded best agent: always go left!
    n_steps = 7
    for step in range(n_steps):
        print("Step {}".format(step + 1))
        obs, reward, done, info = env.step(GO_LEFT)
        print('obs=', obs, 'reward=', reward, 'done=', done)
        env.render()
        if done:
            print("Goal reached!", "reward=", reward)
            break


def execute():
    num_episodes = 100
    alpha = 0.3
    gamma = 0.9
    epsilon = 1.0
    decay_epsilon = 0.3

    env = MyEnv()
    # run Q-learning
    rewards = Qlearning(env, num_episodes, alpha, gamma, epsilon, decay_epsilon)

    # print results
    print("Average reward (all episodes): " + str(sum(rewards) / num_episodes))
    print("Average reward (last 10 episodes): " + str(sum(rewards[-10:]) / 10))
    env.pritn_infos()

    plt.plot(range(num_episodes), rewards)
    plt.xlabel('Episodes')
    plt.ylabel('Accumulated reward along episodes')
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #test_env()
    execute()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
