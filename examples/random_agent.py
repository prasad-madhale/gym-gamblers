from gym_gamblers.envs.gamblers_env import GamblersEnv

env = GamblersEnv()

state = env.reset()

for itr in range(10):
    env.render()
    action = env.sample_action()
    next_state, reward, done, action_taken = env.step(action)
    print("State: {}, Reward: {}, Done: {}, Action Taken: {}".format(state, reward, done, action_taken))
    state = next_state

    if done:
        print("Player has won!")
        break
