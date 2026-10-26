def hanoi_solver(n):
    # Create the three rods and put every disk on the first rod.
    first = [i for i in range(n, 0, -1)]
    second = []
    third = []

    # Save the starting arrangement before any disks move.
    moves = str(first) + " " + str(second) + " " + str(third) + "\n"

    def helper(source, destination, num_disks, auxiliary):
        # Allow this function to update the moves string from hanoi_solver.
        nonlocal moves

        # Stop when there are no disks left in this smaller task.
        if num_disks == 0:
            return

        # Move the smaller disks out of the way onto the auxiliary rod.
        helper(source, auxiliary, num_disks - 1, destination)

        # Move the top disk from the source rod to the destination rod.
        disk = source.pop()
        destination.append(disk)

        # Record the arrangement after this move.
        moves += str(first) + " " + str(second) + " " + str(third) + "\n"

        # Move the smaller disks onto the destination rod.
        helper(auxiliary, destination, num_disks - 1, source)

    # Start solving with all disks: first rod to third rod, using second as auxiliary.
    helper(first, third, n, second)

    # Remove only the final newline so the returned string matches the expected format. 
    return moves.rstrip("\n")


print(hanoi_solver(3))
