# took way longer to figure out how to set up launch.json for this than needed
with open('input.txt', 'r') as f:
    input_file = f.read()

# splits are weird, also had to trim a weird newline at the end of input manually
elves = [[int(cal) for cal in e.split('\n')] for e in input_file.split('\n\n')]

# might as well sort, pop needs index
elf_cals = sorted([sum(e) for e in elves])

# reverse through last three, could also just tell sorted to run in reverse
big_elves = elf_cals[-1:-4:-1]

print(f"Question 1: {big_elves[0]}")
print(f"Question 2: {sum(big_elves)}")