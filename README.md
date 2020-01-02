# Don't Let My Plants Die! :o
![LOGO](happy_flower.jpeg)

### Objectives
- The user receives a .txt file with a calendar of the watering
schedule
- The schedule covers the next 12 weeks starting on the next Monday.
- No plants are watered on Saturdays or Sundays.
- Each plant is watered on its desired schedule or as close as possible, taking into account weekends.

### Part A
Write a function, `parse_json` to obtain a list of dictionaries of plants and 
how often they need to be watered (Hint:You may want to reformat the `water_after` values in the dictionary for easier use later)

### Part B
Write a function `schedule_per_plant` using the [datetime](https://
docs.python.org/3/library/datetime.html)library that adds a key
value pair, with the key being `schedule`, to each plant's
dictionary of the days that plant has to be watered, without being
concerned with weekends quite yet. (Hint:using pprint might make
the schedule easier to read)

### Part C
Write a function `final_schedule` to create a dictionary of all
the days in the 12 week period as the keys and a list of all the
plants that need to be watered on that day as the values.

### Part D
Write a function `weekend_filter` to implement in your
`schedule_per_plant` function. It should subtract a day if the
plant were to land on a Saturday, and add a day if it were to land
on a Sunday.

### Part E
Write a function `create_table` that outputs the schedule into a
table format using any Python table library.

### Part F
In the main function, write your now beautified schedule to a .txt
file. Make sure the .txt file gets pushed to the repo as well.

### PR (Pull Request) Workflow for this Assignment
1. *Fork* this repository into your own personal github account
2. Then *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
4. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes.  This is the code review iteration cycle.

