 
// @ts-check

// this is just a simple example, using a button to trigger this function
function displayDate() {

    document.getElementById("js").innerHTML = Date()

    console.log("FUNCTION executed.. ! ")

}

//set date involves dateObject.setFullYear(2020, 11, 3); year, month, day
 //!! month is 0-11, meaning 6 = July

 // this has to be a Date object, with "new"
 // this runs basically on every page.
var current_date_object = new Date();


//some lists of information to reference
var monthNames = ["January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December"];

var day_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

var dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]


// this is for date formatting. adding zero's in front of single digit dates. 1 - 7 - 20 now equals 01 - 07 - 20
function pad(n) {

    // quick if/else syntax. (statement) ? "if true" : "else";
    return (n < 10) ? '0' + n.toString() : n.toString();

}

// this wraps the whole calendar, just passing in the current date we grab at file run
// or, passing in a date in a different month, brings up that months information.
function printCurrentMonth(today) {

    let header_cont = document.createElement("div");
    header_cont.id = ("calendar_head");
    header_cont.classList.add("row");
    header_cont.classList.add("no-gutters");

    let day_grid = document.createElement("div");
    day_grid.id = ("day_grid");
    day_grid.classList.add("row");
    day_grid.classList.add("no-gutters");
    day_grid.classList.add("border");

    let back_button = document.createElement("button");
    back_button.classList.add("col-2");
    back_button.classList.add("btn");
    back_button.id = "back_button";
    let left_arrow_icon = document.createElement("i");
    left_arrow_icon.id = "left_arrow_icon";
    left_arrow_icon.className = "fa fa-chevron-circle-left";
    back_button.appendChild(left_arrow_icon);

    header_cont.appendChild(back_button);

    let month_div = document.createElement("div");
    month_div.id = "calendar_month";
    month_div.classList.add("col-4");
    let month_name = document.createElement("h4");
    month_name.id = "monthName";
    month_name.innerText = monthNames[today.getMonth()];

    month_div.appendChild(month_name);
    header_cont.appendChild(month_div);
    
    let year_div = document.createElement("div");
    year_div.id = "calendar_year";
    year_div.classList.add("col-4");
    let year_name = document.createElement("h4");
    year_name.id = "monthName";
    year_name.innerText = today.getFullYear().toString();

    year_div.appendChild(year_name);
    header_cont.appendChild(year_div);

    let fwd_button = document.createElement("button");
    fwd_button.classList.add("col-2");
    fwd_button.classList.add("btn");
    fwd_button.id = "fwd_button";
    let right_arrow_icon = document.createElement("i");
    right_arrow_icon.id = "left_arrow_icon";
    right_arrow_icon.className = "fa fa-chevron-circle-right";
    fwd_button.appendChild(right_arrow_icon);

    header_cont.appendChild(fwd_button);

    // save button and div made here
    let save_div = document.createElement("div");
    save_div.className = "row saverow";
    save_div.id = "save_div";

    let save_button = document.createElement("button");
    save_button.id = "save_button";
    save_button.className = "btn btn-primary ml-auto";
    save_button.innerText = "Save";

    save_div.appendChild(save_button);

                /*

            saving the data put in:
                separate the day, month, and year variable to pass to the server

                things to figure out:
                    submission of the javascript variables through a http request
                    parsing those variables into the database
                    i.e. setting them equal to the database variables and pushing them in.
                    pulling those variables back out on page load, or on calendar month change.
                    
            */


    back_button.onclick = function () {

        today.setMonth(today.getMonth()-1);

        document.getElementById("calendar_head").remove();
        document.getElementById("day_grid").remove();
        document.getElementById("save_div").remove();

        console.log("Viewing month = " + monthNames[today.getMonth()]);

        return printCurrentMonth(today);

    }


    fwd_button.onclick = function () {
        
        today.setMonth(today.getMonth() + 1);

        document.getElementById("calendar_head").remove();
        document.getElementById("day_grid").remove();
        document.getElementById("save_div").remove();

        console.log("Viewing month = " + monthNames[today.getMonth()]);

        return printCurrentMonth(today);
    };




    // moving to line ~198 for readability
    // let find_beginning_of_month = new Date();

    // find_beginning_of_month.setFullYear(year, month, 1);

    // let first_of_month = find_beginning_of_month.getDay() //integer 0 through 6

    // creating the column titles, days of the week
    let j;
    for(j=0; j<dayNames.length; j++) {
        const dayNameDiv = document.createElement("div");
        dayNameDiv.id = "dayNameDiv";
        dayNameDiv.className = "col";

        const dayName = document.createElement("p");
        dayName.id = "dayName";
        dayName.className = "mb-auto";
        dayName.innerText = dayNames[j];

        dayNameDiv.appendChild(dayName);

        header_cont.appendChild(dayNameDiv);
    }
    

    // grabbing variables all based on the passing in date object
    let month = today.getMonth(); // 0 to 11

    let year = today.getFullYear(); // 4 digit integer

    let day_of_week = dayNames[today.getDay()]; // 0 through 6

    let find_beginning_of_month = new Date();

    find_beginning_of_month.setFullYear(year, month, 1);

    let first_of_month = find_beginning_of_month.getDay() //integer 0 through 6

    // TODO: this would be modified during a leap year
    let month_total = day_count[month]

    let days_selected_array = [];

    let max_days = [];

    let in_current_month = true;
    
    let done_printing = false;
    
    
    // creating the grid for days
    let i;
    for(i=0; i<42; i++) {

        // this is the actual number displayed in the grid
        let print_number;
        
        if (first_of_month == 0) { //from above, based on day of the week of the 1st of this month
            while ( i < month_total ) {
                print_number = i + 1;
                in_current_month = true;
            }
        }else { // runs when the previous month days need to be shown at the beginning of the first week

            // finding the apropriate day from the previous month to display
            // example: i = 0  +  previous month day count = 30  -  day of the week the next month starts = tuesday = 2
            // day to print = 30 - (2 - 1) = 29. so sunday will show 29. monday will be 30. Tuesday will start the new month at 1.
            print_number = i + day_count[month-1] - (first_of_month - 1);
            in_current_month = false;
            

            if (print_number >= day_count[month-1] + 1) { // finished with previous month
                // using the first of the month day of the week to offset the days already printed
                // otherwise, increases as i loops
                print_number = i - (first_of_month - 1);
                in_current_month = true;

                // checking the above calculated print number for the end of this month
                if (print_number >= day_count[month] +1) {
                    // removing the previous months day count from the number, so it start back at 1
                    print_number -= day_count[month];
                    in_current_month = false;
                }
            }
        }
        
            let week_count = 0;

            
            // every 7 days, create a new row
            if (i % 7 == 0 && i !== 0) {
            const end_week = document.createElement("div");
            end_week.className = "w-100";
            day_grid.appendChild(end_week);

            // increment the week count variable every 7 days as well
            week_count += 1;
            
            // building the max days list, based on how many rows are printed
            max_days.push(0);
                
                // a check to see if this is the end of a week while not in the current month
                // indicates an additional row is not necessary
                if(in_current_month == false) { 
                    done_printing = true;
                }

            }

            // actually making the div's for each print_number calculated
            if(done_printing == false) {
                
                const day_container = document.createElement("div");
                day_container.className = "col";
                day_container.classList.add(week_count.toString()); // week tracking added to classlist of div
                day_container.id = "day_container";

                // the day/number printed is being made here
                const day = document.createElement("p");
                if (in_current_month == true) {
                    // too grey the number or not.
                    day.id = "in_month_date";
                } else {
                    day.id = "out_month_date";
                }
                day.innerText = print_number.toString(); 

                day_container.appendChild(day); 
                day_grid.appendChild(day_container);

                // add event listeners to the objects for actions
                day_container.onmouseover = function () {
                    day_container.classList.add("light_circle");
                };
                day_container.onmouseout = function () {
                    day_container.classList.remove("light_circle");
                };

                day_container.onclick = function () { 
                    
                    // TODO: research what setDate() is doing, add that info here.
                    today.setDate(print_number); // date clicked set here, this is working with just an integer passed in?

                    // formatted variable for the day clicked
                    let day_placeholder =
                    pad(today.getMonth() + 1) +
                    pad(today.getDate()) +
                    today.getFullYear();

                    // process for "deselection"
                    if (day_container.classList.contains("circle")) { // should probably change this to selected??
                        
                        day_container.classList.remove("circle");

                        let unselect_day = days_selected_array.indexOf(
                        day_placeholder
                        );

                        days_selected_array.splice(unselect_day, 1);
                        console.log("Current dates selected = " + 
                        days_selected_array);
                        
                        // finding which week/index to adjust in the max days list
                        max_days[day_container.classList.item(1)] -= 1;

                        console.log("Max days array = " + max_days);

                    //process for "selection"
                    } else {
                        // checking max days list for this week
                        if(max_days[day_container.classList.item(1)] == 3) {
                            
                            return console.log("MAX DAYS SELECTED!");

                        } else {

                            day_container.classList.add("circle");

                            days_selected_array.push(day_placeholder);
                            console.log("Dates added array = " +
                            days_selected_array);

                            // finding which week/index to adjust in the max days list
                            max_days[day_container.classList.item(1)] += 1;

                            console.log("Max days array = " + max_days);

                        }
                    }

                };
            }

        }
    
    // end of function, using static html div labeled calendar
    let calendar = document.getElementById("calendar");

    calendar.appendChild(header_cont);
    calendar.appendChild(day_grid);
    calendar.appendChild(save_div);

}

printCurrentMonth(current_date_object);







