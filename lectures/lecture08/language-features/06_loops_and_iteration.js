/************************/
/* 1. While loop syntax */
/************************/
console.log('\nwhile loop:');
let i = 0;
while (i < 5) {
    console.log('The counter is:', i);
    i++;
}

/**********************/
/* 2. For loop syntax */
/**********************/
console.log('\nfor loop:');
for (let i = 0; i < 5; i++) {
    console.log('The counter is:', i);
}

/********************/
/* 3. For...of loop */
/********************/
const my_list = ['apple', 'orange', 'banana', 'mango', 'peach'];
console.log('\nfor...of loop:');
for (const item of my_list) {
    console.log('The item is:', item);
}
