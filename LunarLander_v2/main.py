import gym
from stable_baselines3 import PPO


env = gym.make('LunarLander-v2')
env.reset()

model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=30000)

for ep in range(10):
    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        env.render()

env.close()