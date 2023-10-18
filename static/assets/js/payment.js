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

    document.querySelector("#submitBtn").addEventListener("click", () => {
        // Get Checkout Session ID
        console.log("Clicked!");
        fetch("/create-checkout-session/coffee")
        .then((result) => { return result.json(); })
        .then((data) => {
            console.log(data);
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({sessionId: data.sessionId});
        })
        .then((res) => {
            console.log(res);
        });
    });

    document.querySelector("#submitBtn2").addEventListener("click", () => {
        // Get Checkout Session ID
        console.log("Clicked!");
        fetch("/create-checkout-session/beer")
        .then((result) => {return result.json(); })
        .then((data) => {
            console.log(data);
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({sessionId: data.sessionId});
        })
        .then((res) => {
            console.log(res);
        });
    });

    document.querySelector("#submitBtn3").addEventListener("click", () => {
        // Get Checkout Session ID
        console.log("Clicked!");
        fetch("/create-checkout-session/crate")
        .then((result) => {return result.json(); })
        .then((data) => {
            console.log(data);
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({sessionId: data.sessionId});
        })
        .then((res) => {
            console.log(res);
        });
    });

});