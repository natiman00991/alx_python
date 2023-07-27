def best_score(a_dictionary):
    # Check if the input dictionary is None or empty
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    # Initialize variables to keep track of the best score and corresponding key
    best_key = None
    best_score = float("-inf")  # A very small negative value as initial best score

    # Loop through the dictionary items to find the key with the highest score
    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            best_key = key

    return best_key


# Test the function with the given examples
# a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))

# best_key = best_score(None)
# print("Best score: {}".format(best_key))
