// ES6 code goes here


fetch("")
.then (res => res.json())
.then (data => {
    data.forEach(i => {
        const productName = document.createElement('div')
        productName.classList.add('product-name')
        const productImg = document.createElement('img')
        productImg.classList.add('product-image')
        const productPrice = document.createElement("button")
        productPrice.classList.add('price-btn')
    
        const productNameNode = document.createTextNode(i.productName)
        const productPriceNode = document.createTextNode(i.price)
    
        productName.appendChild(productNameNode)
        // productImg.appendChild(productImgNode)
        productPrice.appendChild(productPriceNode)
    
        const productNameDiv = document.getElementById('product-name')
        productNameDiv.appendChild(productName)
    
        const productImgDiv = document.getElementById('product-img')
        productImg.setAttribute("src", i.img)
        productImgDiv.appendChild(productImg)
    
        const priceBtn = document.getElementById("btns-wrapper")
        priceBtn.appendChild(productPrice)
})