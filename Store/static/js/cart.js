var btns = document.getElementsByClassName('addtocart')

for (var i = 0; i < btns.lenght; i++) {
    btns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(productId)
    })
}

let btns = document.getElementsByClassName('addtocart')
for (let i = 0; i < btns.length; i++) {
    btns[i].addEventListener('click', function() {
        let productId = this.dataset.product
        let action = this.dataset.action
        location.reload()
        if (user === "AnonymousUser") {
            alert("bạn chưa đăng nhập")
        } else {
            updateCart(productId, action)
        }
    })
}

function updateCart(id, action){
    let url = "/updatecart"
    fetch(url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({"productId": id, "action": action})
    })
.then(response => response.json())
.then(data => console.log(data))
}