class Person {
    constructor(firstName, lastName, age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.profile_pic = 'https://picsum.photos/id/237/40/40'
    }
    getFullName() {
        return this.firstName + " " + this.lastName;
    }
    getGreeting() {
        return "Welcome to the site, " + this.firstName;
    }
};

const personToHTML = person => {
    return `
        <section class="person">
            <h1>${ person.getFullName() }</h1>
            <p>${ person.getGreeting() }</p>
            <img src="${ person.profile_pic }" />
        </section>
    `
}

const brenda = new Person("Brenda", "Wallace", 54);
const neha = new Person("Neha", "Patel", 15);

console.log(personToHTML(brenda));
console.log(personToHTML(neha));