import gym, robo_gym
from robo_gym.wrappers.exception_handling import ExceptionHandling


env = gym.make('MazeMir100Sim-v0', ip='127.0.0.1', gui=True)

env = ExceptionHandling(env)
num_episodes = 100



for episode in range(num_episodes):
    done = False
    print("Reset: {num}".format(num=episode))
    env.reset()
    while not done:
 # random step in the environment
        state, reward, done, info = env.step(env.action_space.sample())
