function deafGrandma() {
    let regex = /[a-z]/g;
    let goodbyeCount = 0;
    if (str == "GOODBYE" && goodbyeCount == 0) {
      console.log("LEAVING SO SOON?");
      goodbyeCount++;
    } else if (str == "GOODBYE" && goodbyeCount == 1) {
      return "LATER, SKATER!";
    } else if (str.length == 0) {
      console.log("WHAT?!");
    } else if (regex.test(str) == true) {
      console.log("SPEAK UP KID!");
    } else if (regex.test(str) == false) {
      console.log("NO, NOT SINCE 1946!");
    } 
  };


deafGrandma();

// neeed window.prompt to sucessfuly use user inputs