const Mock = require('mockjs')
let id = Mock.mock('@id')
console.log(id)

let obj = Mock.mock({
    id:'@id()',
    username:'@cname()',
    date:'@date()',
    avatar:'@image("200×200","red","#FFF","avatar")',//生成图片
    description:'@paragraph()',//描述
    ip:'@ip()',
    email:'@email()'
})
console.log(obj)



