import math
import tkinter.filedialog
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
      self.start = [5, 0]
      self.objeto_state = [2, 3]
      # Initialize the agent at the right of the grid
      self.agent_pos = (5,0) #linha, coluna
      self.objeto = (2, 3) #linha, coluna
      self.paredes = [(1, 3), (4,0), (4, 1), (4, 3), (4, 4), (4, 5), (4, 6), (5, 6)]
      self.base = [(0, 2), (0, 3), (0, 4)]
      self.matriz_renderizacao = [["" for x in range(7)] for y in range(6)]
      self.capturou_objeto = False

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


  def colidiu(self, x, y):
      if x < 0 or y < 0 or x >= self.columns or y >= self.rows:
          return True
      if (y, x) == self.objeto:
          return True
      if (y, x) in self.paredes:
          return True

      return False


  def pode_andar(self, x, y):
      colidiu = not self.colidiu(x, y)
      return colidiu


  def captura_objeto(self):
      y = self.current_state[0]
      x = self.current_state[1]
      if y == 2 and x in [2,4]:
          self.capturou_objeto = True


  def get_delta(self, state_array, action):
      new_x = state_array[1]
      new_y = state_array[0]

      if action == self.RIGHT:  # right
          new_x = new_x + 1
      elif action == self.DOWN:  # down
          new_y = new_y + 1
      elif action == self.LEFT:  # left
          new_x = new_x - 1
      elif action == self.UP:  # up
          new_y = new_y - 1
      else:
          raise Exception("Invalid action.")

      return new_x, new_y

  def step(self, action):
      new_state = deepcopy(self.current_state)
      new_x, new_y = self.get_delta(new_state, action)

      andou = self.pode_andar(new_x, new_y)
      new_state = [new_y, new_x] if andou else new_state

      self.current_state = new_state
      self.captura_objeto()

      reward = -1.0
      is_terminal = False


      if andou:
          if (self.current_state[0], self.current_state[1]) in self.base:
              if self.capturou_objeto: #se chegou na base sem o objeto
                  is_terminal = True
              else:
                  reward = -100.0
                  self.current_state = deepcopy(self.start)

      return self.observation(self.current_state), reward, is_terminal, {}


  def reset(self):
    self.agent_pos = (5,0)
    self.objeto = (2, 3)
    self.current_state = self.start
    self.objeto_state = [2, 3]
    self.capturou_objeto = False
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