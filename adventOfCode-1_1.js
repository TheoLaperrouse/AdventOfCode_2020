const fs = require("fs");

const lines = fs.readFileSync("input-1_1.txt",{encoding:'utf-8'}).split('\n').filter((x) => Boolean(x)).map(x => parseInt(x))

lines.map(entry1 => {
    lines.map(entry2 =>{
        if(entry1 + entry2 == 2020){
            console.log(entry1 * entry2);
            process.exit(1)
        }
    })
})