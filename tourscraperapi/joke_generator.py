import random


class JokeGenerator:
  jokes = [
    (
      "How many metalheads does it take to change a light bulb?\n\n"
      "None. They embrace the darkness."
    ),
    (
      "What did one metalhead say to another after the concert?\n\n"
      "\"You smelly, you need to take Abbath.\""
    ),
    (
      "What's Rob Halford's favorite chore?\n\n"
      "Raking the lawn, raking the lawn..."
    ),
    (
      "What's a metal vocalist favorite type of cheese?\n\n"
      "Brie."
    ),
    (
      "What does a metalhead do when their coffee is too bitter?\n\n"
      "They put Messhugah in it."
    ),
    (
      "That band's so heavy, I can't even read their logo."
    )
  ]

  def __init__(self) -> None:
    pass

  def get_random_joke(self):
    return random.choice(self.jokes)
