const my_list = ['apple', 'orange', 'banana', 'mango', 'peach'];

/*************************************/
/* 1.a List's built-in foreach method */
/*************************************/
console.log('\nforeach method of list:');
// - forEach method  applies an iteraction 
// - function to each element of a list.
my_list.forEach(item => console.log(item));


//1.b. Alternative syntax: define the function argument first:
console.log('\nforeach (alternate strategy):');
const printFunction = item => console.log(item);
my_list.forEach(printFunction);

    


/**********/
/* 2. Map */
/**********/
console.log('\nmap method of list:');
// The map function applies a transformation function to each element of a list, 
// and returns a new list of values.

const my_nums = [1, 2, 3, 4, 5];
const square_nums = my_nums.map(item => item ** 2);
console.log(square_nums);

/*************/
/* 3. Filter */
/*************/
console.log('\nfilter method of list:');
// The filter function applies a filtering function to each element of a list (which evaluates to true or false). 
// It returns a new list with only those items where filtering function returned true.
const nums_greater_than_2 = my_nums.filter(item => item > 2);
console.log(nums_greater_than_2);

/*************/
/* 4. Reduce */
/*************/
console.log('\nreduce method of list:');
// The reduce function applies a transformation function 
// pairwise on all elements of the list in order to 
// reduce it down to a single value. The function will take 
// the first two elements of the list as arguments, return a value, 
// and then the function will run again, using that return value 
// and the third element of the list, etc. 
// For example, reduce can be used to find the sum of a list like so:
const sum_of_nums = my_nums.reduce((a, b) => a + b);
console.log(sum_of_nums);


const sum_of_nums_with_initial_value = my_nums.reduce((a, b) => a + b, 200);
console.log(sum_of_nums_with_initial_value);


/***********************/
/* 5. Chaining Methods */
/***********************/

// first square all the numbers, then add them altogether:
console.log('\nchaining list methods together:');
const sum_of_squares = my_nums.map(
        item => item ** 2
    ).reduce(
        (a, b) => a + b
    );
console.log(sum_of_squares);