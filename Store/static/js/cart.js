var btns = document.getElementsByClassName('addtocart')

for (var i = 0; i < btns.lenght; i++) {
    btns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(productId)
    })
}