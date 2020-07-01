# TODO: scheduler is doing both weeks before looping to next iteration. I would prefer it to do all the iterations
# TODO: for one week and then move to the next? It's messing up something with points...

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
    def __init__(self, first_name, last_name):
        # init method may have arguments. taken in by class instantiation
        self.first_name = first_name  # passing in the arguments so they can be called with the method

        self.last_name = last_name

        self.full_name = (first_name + ' ' + last_name)

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


maddie = Person('Madeline', 'Stickler')  # creating the person, aka instantiation
maddie.add_preference([7, 1, 2, 3, 4, 5, 6])  # changing to a preference of days of the week, 1 through 7. like rankings


fritz = Person('Franz', 'Carmine')
fritz.add_preference([5, 1, 6, 7, 2, 3, 4])
maddie.add_preference([5, 1, 6, 7, 2, 3, 4])


kellen = Person('Kellen', 'Driscoll')
kellen.add_preference([6, 3, 5, 7, 1, 2, 4])
fritz.add_preference([6, 3, 5, 7, 1, 2, 4])

james = Person('James', 'Payne')
james.add_preference([4, 2, 7, 3, 5, 6, 1])
kellen.add_preference([4, 2, 7, 3, 5, 6, 1])

lexy = Person('Alexys', 'Nielson')
lexy.add_preference([2, 1, 6, 4, 7, 5, 3])
james.add_preference([2, 1, 6, 4, 7, 5, 3])

jeremy = Person('Jeremy', 'Nichols')
jeremy.add_preference([4, 5, 6, 3, 2, 7, 1])
lexy.add_preference([4, 5, 6, 3, 2, 7, 1])

tyler = Person('Tyler', 'Shell')
tyler.add_preference([1, 2, 3, 4, 5, 6, 7])
jeremy.add_preference([1, 2, 3, 4, 5, 6, 7])

hunter = Person('Hunter', 'McCollum')
hunter.add_preference([4, 2, 7, 5, 6, 3, 1])
tyler.add_preference([4, 2, 7, 5, 6, 3, 1])

marlon = Person('Marlon', 'Quidlig')
marlon.add_preference([6, 3, 4, 7, 5, 2, 1])
hunter.add_preference([6, 3, 4, 7, 5, 2, 1])

daryl = Person('Daryl', 'Something')
daryl.add_preference([4, 7, 5, 2, 3, 6, 1])
marlon.add_preference([4, 7, 5, 2, 3, 6, 1])

matt = Person('Mathew', 'McMahon')
matt.add_preference([6, 3, 7, 2, 1, 5, 4])
daryl.add_preference([6, 3, 7, 2, 1, 5, 4])

mike = Person('Mike', 'Morgan')
mike.add_preference([5, 7, 3, 4, 2, 1, 6])
matt.add_preference([5, 7, 3, 4, 2, 1, 6])

michelle = Person('Michelle', 'Handtmann')
michelle.add_preference([6, 3, 5, 2, 1, 7, 4])
mike.add_preference([6, 3, 5, 2, 1, 7, 4])

crystal = Person('Crystal', 'Maas')
crystal.add_preference([3, 2, 1, 7, 6, 5, 4])
michelle.add_preference([3, 2, 1, 7, 6, 5, 4])
crystal.add_preference([7, 1, 2, 3, 4, 5, 6])

# ********** algorithm starts below. will eventually run in a continually checking loop that returns it's outputs...


for people_made in gc.get_objects():  # garbage collector function to retrieve created objects

    if isinstance(people_made, Person):
        users.append(people_made)  # adding all 'Person' objects to the list 'users'


def scheduler(list_of_people, iterations):

    average_points = [] # placeholder we can fill with numbers later
    list_iteration = []
    schedule_iteration_results = []  # this is the resulting table.. slots filled and what not

    for each_loop in range(iterations):
        list_iteration.append(list_of_people.copy())
        random.shuffle(list_iteration[each_loop])       # shuffling up the copies put into the table list iteration

    for lists in list_iteration:
        for people in lists:
            print(people.first_name, end='\t')
        print()

    week_checker = list_of_people[0]
    number_of_weeks = len(week_checker.preference_list)
    print(f'Number of weekly preferences found = {number_of_weeks}.')

        average_points.append([])  # this makes the first index, for selected week
        schedule_iteration_results.append([])  # this is the resulting table.. slots filled and what not


    for loop_number in range(iterations):
        print(f'starting loop {loop_number + 1}')
        whole_schedule = []
        # now we have to put this weekly scheduling into another loop for each week!.. lol
        # for selected_week in range(number_of_weeks):

        for selected_week in range(number_of_weeks): #  this gets copied at the end of each iteration?
            print(f'starting week {selected_week + 1}')
            schedule_average = 0  # we want to store each weeks average seperately, by week.
            whole_schedule.append([])  # this makes the first index, for selected week

            for empty_day in range(7):  # this makes second index [day] and third index 'slot'
                whole_schedule[int(selected_week)].append([0, 0, 0, 0, 0, 0])
            # create the points and assigned days lists for each person here
            for person in list_iteration[loop_number]:
                person.points.append([])  # this is the first index selected week
                person.assigned_days.append([])  # this is the first index selected week, unique for each person
                for each_loop in range(iterations):
                    person.points[selected_week].append(0)  # this makes second index 'loop_number' available
                    person.assigned_days[selected_week].append(0)

            for preference_checked in range(1, 8): # checking preferences 1 through 7, all possibilities
                for person in list_iteration[loop_number]:  # accessing the randomized lists of people, changes each loop
                    # print('Checking ', person.first_name, 'for their preference', preference_checked)
                    # print(f'about to check selected_week: {selected_week}, and loop_number: {loop_number}')
                    if person.assigned_days[selected_week][loop_number] == 3:  # checks the slot for this loop?
                        # first identifiers goes into weekly loop, second identifier specifies index of iteration
                        # print(person.first_name, 'has 3 days already')
                        break
                    for day_of_the_week, persons_preference in enumerate(person.preference_list[selected_week]):
                        # print('Checking ', to_day(day_of_the_week), '. Their preference = ', persons_preference, 'Looking for ', preference_checked) # sweet! enumerate is cool. gettin two at once
                        if persons_preference == preference_checked:
                            for slot_number, a_slot in enumerate(whole_schedule[selected_week][day_of_the_week]):
                                # print('The shift slot is =', a_slot, ' and slot number =', slot_number)
                                if a_slot == 0:
                                    whole_schedule[selected_week][day_of_the_week][slot_number] = person
                                    person.assigned_days[selected_week][loop_number] += 1
                                    person.last_assigned_preference = persons_preference
                                    person.points[selected_week][loop_number] += 54.55 / preference_checked
                                    #print('Assigned day', person.assigned_days[selected_week][loop_number], 'to ', person.first_name)
                                    break  # breaks out of slot checking
                            else:  # this will only run if the for loop exhausts without a break...
                                # that days slots are already filled. we look to the next preference number
                                assigned_incoming = person.assigned_days[selected_week][loop_number]
                                next_preference = preference_checked + 1
                                # print(person.first_name, 'didn\'t get their spot in the day')
                                while person.assigned_days[selected_week][loop_number] == assigned_incoming:
                                    if next_preference is 8:
                                        print(f'breaking the second check on {person.first_name} in loop {loop_number + 1}')
                                        break
                                    for day_of_the_week_check_2, persons_preference_check_2 in enumerate(
                                            person.preference_list[selected_week]):
                                        # print('Now checking ', to_day(day_of_the_week_check_2), '. Their preference =', persons_preference_check_2
                                        #      , 'Now looking for ', next_preference)  # sweet! enumerate is cool. gettin two at once
                                        if persons_preference_check_2 == next_preference:
                                            for slot_number_check_2, a_slot_check_2 in enumerate(
                                                    whole_schedule[selected_week][day_of_the_week_check_2]):
                                                # print('The shift slot is = ', a_slot_check_2, 'and slot number = ', slot_number_check_2)
                                                if a_slot_check_2 == 0:
                                                    whole_schedule[selected_week][day_of_the_week_check_2][slot_number_check_2] = person
                                                    person.assigned_days[selected_week][loop_number] += 1
                                                    person.last_assigned_preference = persons_preference_check_2
                                                    person.points[selected_week][loop_number] += 30 / next_preference

                                                    #print('assigned day, on second check, to ', person.first_name)
                                                    break
                                            else:
                                                # print(person.first_name, 'didnt get their second checked day!?')
                                                next_preference += 1
                                                continue
                            break  # this is stopping the check of days after they've been put in the slot, to not waste time

            schedule_iteration_results[selected_week] = whole_schedule.copy() # this isn't right. it still needs to be appended into this results table. i think.

            for week_number, week in enumerate(schedule_iteration_results):
                print(f'Week Number = {week_number + 1 }')
                for day_number, each_day in enumerate(week):
                    print(f'{to_day(day_number)}:', end='\t')   #   shit's all messed up.
                    for people in each_day:
                        print(people, end='\t')
                print()

            for people in list_iteration[loop_number]:
                schedule_average += people.points[selected_week][loop_number]
            schedule_average = schedule_average / len(list_iteration[loop_number])
            print(f'Loop {loop_number + 1}, Week {selected_week + 1}, Average points = {schedule_average}')
            average_points[selected_week].append(schedule_average)
            print(f'average points list = {average_points}')

    final_schedule = []

    # scan average points list for best week 1, then add to results, and continue for week 2, etc.
    for week_number, weekly_points in enumerate(average_points):
        best_schedule_index = weekly_points.index(max(weekly_points))
        final_schedule.append(schedule_iteration_results[week_number][best_schedule_index].copy())
        print(f'Week {week_number + 1} best schedule score = {weekly_points[best_schedule_index]} at index {best_schedule_index}')

    return final_schedule


schedule_table = scheduler(users, 1)

#for those in users:
 #   print(those.full_name, ' has a score of ', int(those.points), 'and ', those.assigned_days, 'days assigned.',
  #        'Last day assigned was a preference ', those.last_assigned_preference)

#print(schedule_table[list of weeks][list of days][list of slots][object])

print()

for num, each_week in enumerate(schedule_table):
    print(f'Week {num + 1}:')
    for count, each_day in enumerate(each_week):
        print(to_day(count), end='\t\t')
        for slot, each_slot in enumerate(each_day):
            for each_object in each_slot:
                try:
                    print(each_object.first_name, end='\t')
                except(AttributeError):
                    print('0', end='\t')
            print()
        print()
