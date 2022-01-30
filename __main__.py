from cli.difficulty import atDifficulty
from cli.tutor import play

level = 0
while True:
    off = play(*atDifficulty(level))
