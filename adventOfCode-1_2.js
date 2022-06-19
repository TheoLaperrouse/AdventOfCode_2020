const fs = require("fs");

const lines = fs.readFileSync("input.txt",{encoding:'utf-8'}).split('\n').filter((x) => Boolean(x)).map(x => parseInt(x))

lines.map(entry1 => {
    lines.map(entry2 =>{
        lines.map(entry3 =>{
            if(entry1 + entry2 + entry3 == 2020){
                console.log(entry1 * entry2 * entry3);
                process.exit(1)
            }
        })
    })
})