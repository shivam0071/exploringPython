// Resources 
//Documentations -  https://devdocs.io/javascript/
// Resources and Free Books - https://www.javascript.com/resources
// https://jsbooks.revolunet.com/


// We will be covering basics and this will be comparable to python tutorial and tips.txt


//_______________________________________________________________________________________________________________________________
// **** JAVA SCRIPT ***
// JavaScript is a scripting language that enables you to create dynamically updating content, 
// control multimedia, animate images, and pretty much everything else. 
// (Okay, not everything, but it is amazing what you can achieve with a few lines of JavaScript code.)

// JS is dynamic type like python, just like in python we have BIFs(built in Functions) in JS we also have some globals(global objects) such as
// console.log(), eval(), String, Number , Math, Date
//example - node JavaScriptTutorialAndTips.js
global.console.log("Hello There!!");
// >> Hello There!!
// same as 
console.log("Hello There!!");
// >> Hello There!!
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

//_______________________________________________________________________________________________________________________________



//_______________________________________________________________________________________________________________________________
// **** STRINGS ***
// The String global object is a constructor for strings or a sequence of characters.
// Strings are immutable(that means it doesn't support str[1] = e ) 
// {this is trying to make changes to an alphabet residing in that memory location...which we can't...)

let str = 'abcd'; // let here means this variable can have any value in the future, can be changes to number etc

// NOT SUPPORTED!!!!! We CAN NOT do (can do in python):
    //  str * 2, str* str 
    // str.count() , str.strip()


// supports

    // > str + str
    // 'abcdabcd'

    // SLICING
        // str.slice(beginIndex[, endIndex])
        
        // > str.slice(2)
        // 'cd'

        // > str.slice(1,3) 'a"bc"d' , 1 inclusive and 3 exclusive
        // 'bc'

    // SPLIT - The split() method splits a String object into an array of strings by separating the string into substrings, 
    // using a specified separator string to determine where to make each split.
    // str.split([separator[, limit]])
        // str.split('b');
        // [ 'a', 'cd' ]

        // > str.split('b',1);
        // [ 'a' ]
//________________________________________________________________________________________________________________________________