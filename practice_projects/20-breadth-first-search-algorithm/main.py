def gen_parentheses(pairs):
    # Validate the input before generating combinations.
    if not isinstance(pairs, int):
        return "The number of pairs should be an integer"
    if pairs < 1:
        return "The number of pairs should be at least 1"

    # Each queue item stores the string so far and the opening/closing counts.
    queue = [("", 0, 0)]
    result = []

    # Explore possible combinations level by level using breadth-first search.
    while queue:
        current, opens_used, closes_used = queue.pop(0)

        # Save the string when it contains the required number of characters.
        if len(current) == 2 * pairs:
            result.append(current)
        else:
            # Add an opening parenthesis if we have not used all available pairs.
            if opens_used < pairs:
                queue.append((current + "(", opens_used + 1, closes_used))

            # Add a closing parenthesis only if it can be matched with an opening one.
            if closes_used < opens_used:
                queue.append((current + ")", opens_used, closes_used + 1))

    return result


print(gen_parentheses(2))
print(gen_parentheses(3))
