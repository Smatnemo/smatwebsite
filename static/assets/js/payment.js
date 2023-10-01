// console.log("Sanity check!");
// use fetch api to make XHR request to config/
// Get publishable key
fetch("/config/")
.then((result) => { 
    return result.json(); })
.then((data) => {
    // Initialize Stripe.js
    // its properties can be added, updated, or removed
    const stripe = Stripe(data.publicKey);
});