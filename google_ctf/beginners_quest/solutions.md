# My solutions for Google CTF Beginners Quest 2021

Website link to competition homepage: <https://capturetheflag.withgoogle.com/beginners-quest/>.

## Chemical Plant

Num: 1
Category: Rev

We were given a website which queries us for a password. Checking the source code we find the following:

~~~js
const checkPassword = () => {
  const v = document.getElementById("password").value;
  const p = Array.from(v).map(a => 0xCafe + a.charCodeAt(0));

  if(p[0] === 52037 &&
     p[6] === 52081 &&
     p[5] === 52063 &&
     p[1] === 52077 &&
     p[9] === 52077 &&
     p[10] === 52080 &&
     p[4] === 52046 &&
     p[3] === 52066 &&
     p[8] === 52085 &&
     p[7] === 52081 &&
     p[2] === 52077 &&
     p[11] === 52066) {
    window.location.replace(v + ".html");
  } else {
    alert("Wrong password!");
  }
}
~~~

We can reverse engineer this check through generating a dictionary of the index:value pairs and subtract out the 0xCafe offset.

~~~py
offset = 0xCafe

indices = [0,6,5,1,9,10,4,3,8,7,2,11]
vals = [52037,52081,52063,52077,52077,52080,52046,52066,52085,52081,52077,52066]

dic = dict()
for i in range(12):
    dic[indices[i]] = vals[i]

password = ""
for i in range(12):
    password += chr(dic[i] - offset)

print(password)
~~~

Entering "GoodPassword" into the password bar gives us a CCTV "live" feed with the flag at the bottom.

Flag: CTF{IJustHopeThisIsNotOnShodan}

## Apartment Logic Lock

Num: 2
Category: Misc
