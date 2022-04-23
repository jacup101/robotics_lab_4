import gym, robo_gym
from robo_gym.wrappers.exception_handling import ExceptionHandling
env = gym.make('EndEffectorPositioningURSim-v0', ur_model='ur5', ip='127.0.0.1',gui=True)

env = ExceptionHandling(env)
num_episodes = 10
for episode in range(num_episodes):
    done = False
    env.reset()
    while not done:
        # random step in the environment
        state, reward, done, info = env.step(env.action_space.sample())
