
import gc  # garbage collector module, used for tracking the objects/users that are created
import random

# schedule is made for 6 weeks
# balanced with 6 per shift



''' a function that turns numbers into printed days of the week, useful for quickly printing out the tracked data'''




def to_day(number):
    if number == 0:
        return 'Sunday '
    if number == 1:
        return 'Monday '
    if number == 2:
        return 'Tuesday'
    if number == 3:
        return 'Wednesday'
    if number == 4:
        return 'Thursday'
    if number == 5:
        return 'Friday '
    if number == 6:
        return 'Saturday'


users = []  # empty list for users


#######################

# class creates a new TYPE of object
# new INSTANCES of this type can be created...
class Person:
    """class for each nurse"""

    # ^^^ this is a docstring? returned through .__doc__

    # special method __init__ creates instances with customized initial state
    # class instantiation automatically invokes this for each creation
    def __init__(self, first_name, last_name = None):
        # init method may have arguments. taken in by class instantiation
        self.first_name = first_name  # passing in the arguments so they can be called with the method

        self.last_name = last_name

        #self.full_name = (first_name + ' ' + last_name)

        self.no_pref = True  # using to track whether a preference has been added

        self.points = []  # using to track the overall agreement of the user choices to what's assigned

        self.auto_filled = False

        self.last_assigned_preference = None

        # make a list of the days you want to work this week, 1's = top priority, etc.
        self.preference_list = []  # empty list that can be queried later

        self.assigned_days = []

    def add_preference(self, pref):  # pass in your preference through the argument

        self.preference_list.append(pref)  # add that preference to the list

        self.no_pref = False  # update the boolean for preference tracking


#maddie = Person('Maddie',)  # creating the person, aka instantiation
#maddie.add_preference([5, 7, 1, 2, 3, 6, 4])  # changing to a preference of days of the week, 1 through 7. like rankings
#maddie.add_preference([5, 1, 6, 7, 2, 3, 4])

an = Person('An',)
an.add_preference([1, 4, 6, 2, 3, 5, 7])
#an.add_preference([6, 3, 5, 7, 1, 2, 4])

angeline = Person('Angeline')
angeline.add_preference([1, 6, 5, 2, 3, 7, 4])
#angeline.add_preference([4, 2, 7, 3, 5, 6, 1])

brenda = Person('Brenda')
brenda.add_preference([7, 1, 2, 3, 5, 6, 4])
#brenda.add_preference([2, 1, 6, 4, 7, 5, 3])

crystal = Person('Crystal')
crystal.add_preference([4, 6, 5, 7, 1, 2, 3])
#crystal.add_preference([4, 5, 6, 3, 2, 7, 1])

daryl = Person('Daryl')
daryl.add_preference([1, 2, 7, 6, 3, 5, 4])
#daryl.add_preference([1, 2, 3, 4, 5, 6, 7])

grace = Person('Grace')
grace.add_preference([1, 4, 2, 5, 6, 7, 3])     # this PTO stuff is new
#grace.add_preference([4, 2, 7, 5, 6, 3, 1])

laura = Person('Laura')
laura.add_preference([5, 6, 7, 1, 2, 4, 3])
#laura.add_preference([6, 3, 4, 7, 5, 2, 1])

soniya = Person('Soniya')
soniya.add_preference([1, 5, 4, 7, 3, 2, 6])
#soniya.add_preference([4, 7, 5, 2, 3, 6, 1])

danny = Person('Danny')
danny.add_preference([4, 6, 1, 5, 3, 7, 2])
#danny.add_preference([6, 3, 7, 2, 1, 5, 4])

marifi = Person('Marifi')
marifi.add_preference([6, 7, 1, 5, 4, 2, 3])
#marifi.add_preference([5, 7, 3, 4, 2, 1, 6])

sheila = Person('Sheila')
sheila.add_preference([5, 1, 3, 4, 6, 2, 7])
#sheila.add_preference([6, 3, 5, 2, 1, 7, 4])

godfrey = Person('Godfrey')
godfrey.add_preference([6, 3, 1, 2, 5, 4, 7])
#godfrey.add_preference([3, 2, 1, 7, 6, 5, 4])

ashley = Person('Ashley')
ashley.add_preference([6, 7, 4, 2, 3, 5, 1])
#ashley.add_preference([7, 1, 2, 3, 4, 5, 6])

mary = Person('Mary')
mary.add_preference([1, 7, 5, 2, 3, 4, 6])
#ashley.add_preference([7, 1, 2, 3, 4, 5, 6])

# ********** algorithm starts below. will eventually run in a continually checking loop that returns it's outputs...


for people_made in gc.get_objects():  # garbage collector function to retrieve created objects

    if isinstance(people_made, Person):
        users.append(people_made)  # adding all 'Person' objects to the list 'users'

# goal is to do both weeks. process all week 1's first and select best one... etc
# we still need the week number finder


def create_empty_week(holding_list):
    for empty_day in range(7):
        holding_list.append([ 0, 0, 0, 0, 0, 0])
    return holding_list


week_checker = users[0]
number_of_weeks = len(week_checker.preference_list)
print(f'Number of weekly preferences found = {number_of_weeks}.') # do we need this shit?

# maybe we need the number of weeks for creating empty slots?

# we got the number of weeks. now we just need to put the week ones through the algorithm..

# have to obviously go through each person and check first.

# we need an identifier out here to loop through the weeks.. here's where we can use the number of weeks

# we also have to make the weekly schedule that's going to get copied. inside of one of these loops...

# we need a list for all the week 1 schedule iterations.. but we also need a list for each week 1 iteration

# and does that get cleared at the end after every copy? call it a temporary weekly table

# call an outside function to create the table?

# adding the points and assigned days lists.. needs to have weekly lists and slots for each iteration

# of the week as well...

# where will the iteration section go? I guess outside of this.

# or no. we want the part inside the week to iterate. so it would go inside the week_index loop
list_of_weekly_tables = []
list_of_point_averages = []

iterations = 100

# TODO: Biggest issue currently: the floor has 15 nurses. Meaning three nights will have 7 people assigned.

# TODO: PTO is not exactly accounted for. It can be placed at the lowest of preferences, but a check needs to be made to ensure it was received.

# TODO: Don't move from days that are balanced?

for week_index in range(number_of_weeks):
    temp_weekly_table = []
    create_empty_week(temp_weekly_table)
    list_of_weekly_tables.append([]) # adding in a new list for the week
    list_of_point_averages.append([])
    print(f'This round is for Week {week_index + 1}')
    # creating the weekly slots in each persons points and assigned
    for person in users:
        person.points.append([])
        person.assigned_days.append([])
    for iteration_number in range(iterations):
        # adding in the random shuffle here.
        temp_users_list = users
        random.shuffle(temp_users_list)
        temp_point_average = 0
        for person in temp_users_list:
            person.points[week_index].append(0)
            person.assigned_days[week_index].append(0)
        for preference_number in range(1, 8):
            for person_index, person in enumerate(temp_users_list):
                print(f'Looking at {person.first_name}')
                if person.assigned_days[week_index][iteration_number] == 3:
                    print(f'{person.first_name} got there THREE days')
                    break
                for day_index, daily_preference in enumerate(person.preference_list[week_index]):
                    print(f' Checking for preference {preference_number}. Found {person.first_name}\'s '
                          f'preference of {daily_preference}')
                    if daily_preference == preference_number:
                        print(f'{to_day(day_index)} found as preference {daily_preference}')
                        for slot_index, shift_slot in enumerate(temp_weekly_table[day_index]):
                            if shift_slot == 0:
                                print(f'{person.first_name} placed into slot {slot_index}')
                                temp_weekly_table[day_index][slot_index] = person
                                person.points[week_index][iteration_number] += 54.55 / daily_preference
                                person.assigned_days[week_index][iteration_number] += 1
                                temp_point_average += 54.55 / daily_preference
                                break
                        else:
                            print(f'{person.first_name} didn\'t get their preferred day!')
                            days_assigned = person.assigned_days[week_index][iteration_number]
                            next_preference = preference_number
                            while person.assigned_days[week_index][iteration_number] == days_assigned:
                                next_preference += 1
                                if next_preference == 8:
                                    print(f'******************** Cant find a slot! *************************')
                                    break
                                for next_day_index, next_daily_preference in enumerate(person.preference_list[week_index]):
                                    print(f' Checking for next preference {next_preference}. Found {person.first_name}\'s '
                                          f'preference of {next_daily_preference}')
                                    if next_daily_preference == next_preference:
                                        print(f'{to_day(next_day_index)} found as preference {next_daily_preference}')
                                        for next_slot_index, shift_slot in enumerate(temp_weekly_table[next_day_index]):
                                            if shift_slot == 0:
                                                print(f'{person.first_name} placed into slot, in filling cycle')
                                                temp_weekly_table[next_day_index][next_slot_index] = person
                                                person.points[week_index][iteration_number] += 54.55 / next_daily_preference
                                                person.assigned_days[week_index][iteration_number] += 1
                                                temp_point_average += 54.55 / next_daily_preference
                                                break
                                        else:
                                            print(f'No slot given to {person.first_name}')

                        break
        print(f'Is this the start of a new iteration??')
        # here is where we have gone through the iteration of a certain week.
        # a place where we can copy the schedule made and clear it.
        # but first we need to create the spaces in the list of tables...
        list_of_weekly_tables[week_index].append(temp_weekly_table.copy())
        temp_weekly_table.clear()
        temp_weekly_table = []
        create_empty_week(temp_weekly_table)
        # we can append the list of point averages here as well, with the appropriate
        # iteration average in it's week_index slot.
        print(f'Week {week_index}, Iteration {iteration_number}, Average = {temp_point_average / len(users)}')
        temp_point_average = temp_point_average / len(users)
        list_of_point_averages[week_index].append(temp_point_average)
    print(f'Is this the start of the new week???')

final_schedule = []
final_scores = []
# check the list of tables and find the right ones to append to this final schedule
for week_index, each_week in enumerate(list_of_point_averages):
    best_iteration_index = each_week.index(max(each_week))
    final_schedule.append(list_of_weekly_tables[week_index][best_iteration_index])
    final_scores.append(list_of_point_averages[week_index][best_iteration_index])


print()
print()
print()
print()


for week_iteration, week_index in enumerate(list_of_weekly_tables):
    print(f'Week {week_iteration + 1} Possible Schedules:')
    for each_iteration, each_week in enumerate(week_index):
        print(f'Iteration {each_iteration + 1} - Average Score = {list_of_point_averages[week_iteration][each_iteration]}:')
        for day, each_day in enumerate(each_week):
            print(f'{to_day(day)}:', end='\t')
            for each_object in each_day:
                try:
                    print(each_object.first_name, end='\t')
                except(AttributeError):
                    print('0', end='\t')
            print()
        print()
    print()
    print()

for week_iteration, week_index in enumerate(final_schedule):
    print(f'BEST Week {week_iteration + 1} - SCORE = {final_scores[week_iteration]}:')
    for day, each_day in enumerate(week_index):
        print(f'{to_day(day)}:', end='\t')
        for each_object in each_day:
            try:
                print(each_object.first_name, end='\t')
            except(AttributeError):
                print('0', end='\t')
        print()
    print()
