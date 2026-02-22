// JavaScript is a high-level, interpreted programming language that 
// runs in the browser and allows you to make web pages interactive.



// HTML → Structure
// CSS → Styling
// JavaScript → Behavior



// Example:


// Button click

// Form validation

// Calling backend APIs

// Dynamic content loading





//  2️⃣ How Browser Executes JavaScript

// When you open a webpage:

// Browser downloads HTML

// Builds DOM (Document Object Model)

// Loads CSS

// Executes JavaScript

// JavaScript runs inside browser’s engine:

// Chrome → V8 Engine

// Firefox → SpiderMonkey





//  3️⃣ Variables in JavaScript

// There are 3 ways:

 var name = "Mohit";
 let age = 25;
 const country = "India";


// 🔹 Difference
// Keyword	    Can Reassign	     Scope
// var	            Yes	            Function
// let	            Yes	              Block
// const	        No	              Block

// 

//  4️⃣ Data Types


// Primitive Types

// String

// Number

// Boolean

// Null

// Undefined

 let name = "Mohit";
 let age = 25;
 let isActive = true;
 Non-Primitive




// Object

 let student = {
   name: "Basant",
   age: 25
 };


// Array
 let courses = ["Python", "Django"];



//  5️⃣ What is DOM? (Very Important)


// DOM (Document Object Model) is a tree-like structure that represents HTML elements as objects.

// Example HTML:

 <h1 id="title">Hello</h1>

// Browser converts it into:

// document
 └── h1 (id="title")


// Accessing DOM
 const heading = document.getElementById("title");

// Other methods:

 document.getElementsByClassName()
 document.querySelector()
 document.querySelectorAll()
 Modifying DOM
 heading.innerText = "Welcome Students";
 heading.style.color = "blue";

// This is dynamic UI update.



//  6️⃣ Events (User Interaction)


// An event is an action performed by the user or browser.

// Examples:

// click

// submit

// change

// keypress

// Button Click Example

// HTML:

 <button id="btn">Click Me</button>

// JS:

 document.getElementById("btn")
 .addEventListener("click", function() {
     alert("Button Clicked");
 });




// 🟢 7️⃣ Forms Handling (Important for Backend Integration)

// HTML:

 <form id="loginForm">
   <input type="email" id="email">
   <input type="password" id="password">
   <button type="submit">Login</button>
 </form>



// JS:

 document.getElementById("loginForm")
 .addEventListener("submit", function(event) {

     event.preventDefault();  // prevents page reload

     const email = document.getElementById("email").value;
     const password = document.getElementById("password").value;

     console.log(email, password);
 });



// Why preventDefault()?
// Because form normally reloads page.

//  8️⃣ Fetch API (Backend Communication)


// Fetch API is used to send HTTP requests from browser to server.

// GET Request


 fetch("http://127.0.0.1:8000/api/courses/")
 .then(response => response.json())
 .then(data => {
     console.log(data);
 });



// Flow:

// Browser → HTTP Request → Django → JSON Response → JS handles it

// POST Request



// fetch("http://127.0.0.1:8000/api/login/", {
     method: "POST",
     headers: {
         "Content-Type": "application/json"
     },
     body: JSON.stringify({
         email: email,
         password: password
     })
 })
 .then(res => res.json())
 .then(data => {
     console.log(data);
 });



// Important:

// method

// headers

// body

// JSON.stringify()




 {/* JWT Authentication Handling

When using Django JWT login:

Server returns:



{
  "access": "token_here",
  "refresh": "refresh_token"
}



Store token:

localStorage.setItem("access", data.access);



Send token:

fetch("http://127.0.0.1:8000/api/courses/", {
  headers: {
    "Authorization": "Bearer " + localStorage.getItem("access")
  }
})





JWT = Digital identity card
Server checks signature before giving data.









🟢  Rendering Data on Page
data.forEach(course => {
    const p = document.createElement("p");
    p.innerText = course.title;
    document.body.appendChild(p);
});

This makes frontend dynamic. */}













{/* Example */}


{/* Complete Frontend Flow (Mini LMS)

Login Page
⬇
Send credentials
⬇
Receive JWT
⬇
Store in localStorage
⬇
Call protected API
⬇
Render courses */}