fetch("localhost:5000/products")
  .then (res => res.json())
  .then (data => {
  data.forEach( object => {
    const productName = document.createElement('div')
    productName.classList.add('product-name')
    const productImg = document.createElement('img')
    productImg.classList.add('product-image')
    const productPrice = document.createElement("p")
    productPrice.classList.add('price-tag')
    const showPageBtn =document.createElement('button')
    showPageBtn.classList.add('show-page-button')

    const productNameNode = document.createTextNode(object.productName)
    const productPriceNode = document.createTextNode(`$${object.price}.00`)
    const showPageNode = document.createTextNode(object.id)

    console.log(object.price)
    console.log(productPriceNode)

    productName.appendChild(productNameNode)
    productPrice.appendChild(productPriceNode)
    showPageBtn.appendChild(showPageNode)

    console.log(productPrice)

    const productNameDiv = document.getElementById('product-name')
    productNameDiv.appendChild(productName)

    const productImgDiv = document.getElementById('product-img')
    productImg.setAttribute("src", object.img)
    productImgDiv.appendChild(productImg)

    const priceBtn = document.getElementById("btns-wrapper")
    priceBtn.appendChild(productPrice)
    priceBtn.appendChild(showPageBtn)
  })