
# Find out the number of articles with longest number of strictly decreasing sequence of views
# Example: If 21 articles have strictly decreasing pageviews everyday for 5 days (which is the global maximum), 
# then your script should find these articles from the output file and return 21.
# Run your commands/code to process the output and echo the answer

file = open("output","r")

longest_dec_days = 0
total_titles = 0

for line in file:
    line = line.strip()
    elements = line.split("\t")

    title_longest_dec = 0
    running_dec_days = 0
    view_pivot = int(elements[2].split(":")[1])

    for i in range(2,33):
        date_score = int(elements[i].split(":")[1])
        if date_score < view_pivot and running_dec_days < title_longest_dec:
            running_dec_days += 1
        else:
            if date_score >= view_pivot and running_dec_days >= title_longest_dec: 
                title_longest_dec = running_dec_days
                running_dec_days = 0

        view_pivot = date_score
    
    # print elements[1] + "\t" + str(title_longest_dec)

    if title_longest_dec == longest_dec_days:
        print elements[1] + ": " + str(title_longest_dec)
        total_titles += 1
    elif title_longest_dec > longest_dec_days:
        print elements[1] + ": " + str(title_longest_dec)
        longest_dec_days = title_longest_dec
        total_titles = 1

print total_titles
