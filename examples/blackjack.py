# -*- coding: utf-8 -*-
"""
Author: John Mansfield
"""

import os
import warnings

import gym
import pygame
from algorithms.rl import RL
from algorithms.planner import Planner
from examples.test_env import TestEnv
import pickle


class Blackjack:
    def __init__(self):
        self._env = gym.make('Blackjack-v1', render_mode=None)
        # Explanation of convert_state_obs lambda:
        # def function(state, done):
        # 	if done:
		#         return -1
        #     else:
        #         if state[2]:
        #             int(f"{state[0]+6}{(state[1]-2)%10}")
        #         else:
        #             int(f"{state[0]-4}{(state[1]-2)%10}")
        self._convert_state_obs = lambda state, done: (
            -1 if done else int(f"{state[0] + 6}{(state[1] - 2) % 10}") if state[2] else int(
                f"{state[0] - 4}{(state[1] - 2) % 10}"))
        # Transitions and rewards matrix from: https://github.com/rhalbersma/gym-blackjack-v1
        current_dir = os.path.dirname(__file__)
        file_name = 'blackjack-envP'
        f = os.path.join(current_dir, file_name)
        try:
            self._P = pickle.load(open(f, "rb"))
        except IOError:
            print("Pickle load failed.  Check path", f)
        self._n_actions = self.env.action_space.n
        self._n_states = len(self._P)

    @property
    def n_actions(self):
        return self._n_actions

    @n_actions.setter
    def n_actions(self, n_actions):
        self._n_actions = n_actions

    @property
    def n_states(self):
        return self._n_states

    @n_states.setter
    def n_states(self, n_states):
        self._n_states = n_states

    @property
    def P(self):
        return self._P

    @P.setter
    def P(self, P):
        self._P = P

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, env):
        self._env = env

    @property
    def convert_state_obs(self):
        return self._convert_state_obs

    @convert_state_obs.setter
    def convert_state_obs(self, convert_state_obs):
        self._convert_state_obs = convert_state_obs


if __name__ == "__main__":
    blackjack = Blackjack()

    # VI/PI
    # V, V_track, pi = Planner(blackjack.P).value_iteration()

##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=1) 
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=2)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=3)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=4)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=5)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=6)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=7)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=8)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=9)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=10)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=13)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=100)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=200)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1 , n_iters=500)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=750)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=1000)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=1100)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=1200)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=1300)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=1500)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=2000)
##    V, V_track, pi = Planner(blackjack.P).value_iteration(gamma=1, n_iters=3000)


    
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=1) 
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=2)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=3)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=4)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=5)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=6)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=7)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=8)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=9)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=10)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=50)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=100)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=200)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=500)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=750)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=1000)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=1100)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=1200)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=1300)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=1500)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=2000)
    # V, V_track, pi = Planner(blackjack.P).policy_iteration(gamma=1, n_iters=3000)

    # Q-learning
    Q, V, pi, Q_track, pi_track = RL(blackjack.env).q_learning(blackjack.n_states, blackjack.n_actions, blackjack.convert_state_obs, n_episodes=5000)
    Q, V, pi, Q_track, pi_track = RL(blackjack.env).q_learning(blackjack.n_states, blackjack.n_actions, blackjack.convert_state_obs, n_episodes=10000)
    Q, V, pi, Q_track, pi_track = RL(blackjack.env).q_learning(blackjack.n_states, blackjack.n_actions, blackjack.convert_state_obs, n_episodes=50000)
    Q, V, pi, Q_track, pi_track = RL(blackjack.env).q_learning(blackjack.n_states, blackjack.n_actions, blackjack.convert_state_obs, n_episodes=100000)
    Q, V, pi, Q_track, pi_track = RL(blackjack.env).q_learning(blackjack.n_states, blackjack.n_actions, blackjack.convert_state_obs, n_episodes=500000)
    Q, V, pi, Q_track, pi_track = RL(blackjack.env).q_learning(blackjack.n_states, blackjack.n_actions, blackjack.convert_state_obs, n_episodes=750000)
    Q, V, pi, Q_track, pi_track = RL(blackjack.env).q_learning(blackjack.n_states, blackjack.n_actions, blackjack.convert_state_obs, n_episodes=1000000)
      

    test_scores = TestEnv.test_env(env=blackjack.env, render=True, pi=pi, user_input=False,
                                   convert_state_obs=blackjack.convert_state_obs)
