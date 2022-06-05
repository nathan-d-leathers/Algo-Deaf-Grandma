function deafGrandma() {
    let regex = /[a-z]/g;
    let goodbyeCount = 0;
    let str = window.prompt("Hey Kid! ")

    while (goodbyeCount < 2) {
    if (str == "GOODBYE" && goodbyeCount == 0) {
      str = window.prompt("LEAVING SO SOON?");
      goodbyeCount++;
    } else if (str == "GOODBYE" && goodbyeCount == 1) {
      str = alert("LATER, SKATER!");
    } else if (str.length == 0) {
      str = window.prompt("WHAT?!");
    } else if (regex.test(str) == true) {
      str = window.prompt("SPEAK UP KID!");
    } else if (regex.test(str) == false) {
      str = window.prompt("NO, NOT SINCE 1946!");
    } 
    }
  };


console.log(deafGrandma());