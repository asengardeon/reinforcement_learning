from copy import deepcopy

import numpy as np
import gym
from gym import spaces

class MyEnv(gym.Env):
  metadata = {'render.modes': ['console']}

  # Define constants for clearer code
  LEFT = 0
  RIGHT = 1
  UP = 2
  DOWN = 3





  def __init__(self):
      super(MyEnv, self).__init__()

      # Size of the 1D-grid
      self.columns = 7
      self.rows = 6
      self.start = [0, 0]
      # Initialize the agent at the right of the grid
      self.agent_pos = (5,0) #linha, coluna
      self.objeto = (2, 3) #linha, coluna
      self.paredes = [(1, 3), (4,0), (4, 1), (4, 3), (4, 4), (4, 5), (4, 6), (5, 6)]
      self.base = [(0, 2), (0, 3), (0, 4)]
      self.matriz_renderizacao = [["" for x in range(7)] for y in range(6)]

      # Define action and observation space
      # They must be gym.spaces objects
      # Example when using discrete actions, we have two: left and right
      n_actions = 4
      self.action_space = spaces.Discrete(n_actions)

      self.current_state = None
      # The observation will be the coordinate of the agent
      # this can be described both by Discrete and Box space
      self.observation_space = spaces.Discrete(self.rows*self.columns)

  def observation(self, state):
      return state[0] * self.columns + state[1]

  def pode_andar(self, x, y):
      if x < 0 or y < 0 or x >= self.columns or y >= self.rows:
          return False
      if (y, x) == self.objeto:
          return False
      if (y, x) in self.paredes:
          return False
      return True

  def step(self, action):
      new_state = deepcopy(self.current_state)

      # ay, ax = self.agent_pos
      # if action == self.LEFT and self.pode_andar(ax-1, ay):
      #     self.agent_pos = (ax-1, ay)
      # elif action == self.RIGHT and self.pode_andar(ax+1, ay):
      #     self.agent_pos = (ax+1, ay)
      # elif action == self.UP and self.pode_andar(ax, ay-1):
      #     self.agent_pos = (ax, ay-1)
      # elif action == self.DOWN  and self.pode_andar(ax, ay+1):
      #     self.agent_pos = (ax, ay+1)
      #
      # done = self.agent_pos in self.base
      # reward = 1 if done else 0
      #
      # info = {}
      #
      # return np.array([self.agent_pos]).astype(np.float32), reward, done, info
      new_state = deepcopy(self.current_state)

      if action == 0:  # right
          new_state[1] = min(new_state[1] + 1, self.columns - 1)
      elif action == 1:  # down
          new_state[0] = max(new_state[0] - 1, 0)
      elif action == 2:  # left
          new_state[1] = max(new_state[1] - 1, 0)
      elif action == 3:  # up
          new_state[0] = min(new_state[0] + 1, self.rows - 1)
      else:
          raise Exception("Invalid action.")
      self.current_state = new_state

      reward = -1.0
      is_terminal = False
      if self.current_state[0] == 0 and self.current_state[1] > 0:
          if self.current_state[1] < self.columns - 1:
              reward = -100.0
              self.current_state = deepcopy(self.start)
          else:
              is_terminal = True

      return self.observation(self.current_state), reward, is_terminal, {}


  def reset(self):
    self.agent_pos = (5,0)
    self.objeto = (2, 3)
    self.current_state = self.start
    return self.observation(self.current_state)


  def render(self, mode='console'):
    if mode != 'console':
       raise NotImplementedError()
       # agent is represented as a cross, rest as a dot
    ay, ax = self.agent_pos
    oy, ox = self.objeto

    for y, x in self.paredes:
        self.matriz_renderizacao[y][x] = "X"
    for y, x in self.base:
        self.matriz_renderizacao[y][x] = "B"

    for y in range(self.rows):
        for x in range(self.columns):
            if not self.matriz_renderizacao[y][x] in ["X", "B"]:
                if ax == x and ay == y:
                    self.matriz_renderizacao[y][x] = "A"
                elif ox == x and oy == y:
                    self.matriz_renderizacao[y][x] = "O"
                else:
                    self.matriz_renderizacao[y][x] = " "

    for y in range(self.rows):
        print("-" * self.columns * 2)
        linha = "|"
        for x in range(self.columns):
            linha += f"{self.matriz_renderizacao[y][x]}|"
        print(linha)



  def close(self):
    pass