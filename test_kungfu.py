import gym
env = gym.make('KungFuMaster-v0')
for i_episode in range(100):
    observation = env.reset()
    for t in range(2000):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
