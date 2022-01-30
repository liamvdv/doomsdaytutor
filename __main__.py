from cli.difficulty import atDifficulty
from cli.doomsday import play

level = 0
while True:
    off = play(*atDifficulty(level))
