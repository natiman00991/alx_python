def common_elements(set_1, set_2):
    # Initialize an empty set to store the common elements
    common_set = set()

    # Loop through each element in set_1
    for element in set_1:
        # Check if the element is also in set_2
        if element in set_2:
            # Add the common element to the common_set
            common_set.add(element)

    return common_set


# Test the function with the given sets
# set_1 = { "Python", "C", "Javascript" }
# set_2 = { "Bash", "C", "Ruby", "Perl" }
# c_set = common_elements(set_1, set_2)
# print(sorted(list(c_set)))
