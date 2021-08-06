var btna = document.getElementById('diva');
var lista = document.getElementById('aa');
var gwc = document.getElementById('gwc');
var aaa = document.getElementById('aaa');
var shopping_number = document.getElementById('shopping_number')
var pay = document.getElementById('to_pay')
//console.log(shopping_number);

var nb = document.getElementById('shopping_number').innerText;
//console.log(nb);
var thing1_nb = 1;
var thing1_price = 45.00;
var flag1 = 0;
var flag2 = 0;
var total_price = 0;

lista.onclick = function () {
    flag2 = 1;
    if (flag1 == 1) {
        thing1_nb++;
        var thing1_number = document.getElementById('thing1_number');
        thing1_number.innerHTML = '¥45 / x' + thing1_nb;
    }
    if (flag1 == 0) {
        flag1 = 1;
        nb++;
        shopping_number.innerHTML = nb;
        lista.style.backgroundColor = 'red';
        var div1 = document.createElement('div');
        //var shopnumber=12;
        div1.innerHTML = '<div class="cart-items-item" id="aaa">\n' +
            '                  <a href="#" class="cart-img mr-2 float-left">\n' +
            '                    <img class="img-fluid" src="assets/img/shop/devcloud01.jpg" alt="Product 1">\n' +
            '                  </a>\n' +
            '                  <div class="float-left">\n' +
            '                    <h5 class="mb-0">\n' +
            '                      空气滤芯\n' +
            '                    </h5>\n' +
            '                    <p class="mb-0" id="thing1_number">¥45.00 / x1</p>\n' +
            '                    <a href="#" class="close cart-remove text-primary"> <i class="fa fa-times" ></i> </a>\n' +
            '                  </div>\n' +
            '                </div>';

        gwc.insertBefore(div1, gwc.children[0]);
        var chahao = document.getElementsByClassName('close cart-remove text-primary');
        console.log(chahao);
        for (var j = 0; j < chahao.length; j++) {
            chahao[j].onclick = function () {
                flag1 = 0;
                thing1_nb = 1;
                nb--;
                shopping_number.innerHTML = nb;
                gwc.removeChild(this.parentNode.parentNode.parentNode)
            }
        }
    }
    total_price = thing1_nb * thing1_price;
    console.log(total_price);
    var all_price = document.getElementById('total_price');
    //console.log(all_price);
    all_price.innerHTML = total_price;
    document.getElementById('total_price').value = total_price;
}
pay.onclick = function(){
    var pay_price = document.getElementById('pay_price');
    console.log(pay_price);
    pay_price.innerHTML = '¥' + total_price;

}
// var chahao1 = document.getElementsByClassName('close cart-remove text-primary');
// console.log(chahao1);
// for (var j = 0; j < chahao1.length; j++) {
//     chahao1[j].onclick = function () {
//         nb--;
//         shopping_number.innerHTML = nb;
//         gwc.removeChild(this.parentNode.parentNode)
//     }
// }
//
//
// flag2 = 0;
// var chhao = document.getElementsByClassName('close cart-remove text-primary');
// console.log(chhao);
// for (var k = 0; k < chhao.length; k++) {
//     chahao[k].onclick = function () {
//         gwc.removeChild(this.parentNode.parentNode)
//     }
//
//
//     var chahao = document.querySelectorAll("close cart-remove text-primary");
//     for (var k = 0; k < chahao.length; k++) {
//         chahao.onclick =