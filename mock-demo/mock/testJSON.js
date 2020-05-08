const fs = require('fs')
const path = require('path')
const JSON5 = require('json5')

//读取json文件
function getJSONFile(filepath){
    //读取指定json文件
    var json = fs.readFileSync(path.resolve(__dirname,filepath),'utf-8');
    return JSON5.parse(json)
}

var json = getJSONFile('./userinfo.json5');

console.log('json',json)