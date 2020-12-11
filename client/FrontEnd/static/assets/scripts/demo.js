 
import {data, mockData} from "./mockData"

const form = document.getElementById("add-item-form")

function sendData(e){
    
    const formData = new FormData(form)

    formData.forEach(i => {
        console.log(i)
    })


    //will be replace with our API
    fetch("https://httpbin.org/post", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => alert(JSON.stringify(data))
    .catch(err => console.log(err))
    
}


document.addEventListener("DOMContentLoaded", () => {

    data.forEach(i => {

        const productDiv = document.createElement("div")
        const nameDiv = document.createElement("div")
        const priceDiv = document.createElement("div")

        const productNode = document.createTextNode(i.product_name)

        const productPriceNode = document.createTextNode(i.price)

        nameDiv.appendChild(productNode)
        priceDiv.appendChild(productPriceNode)
        productDiv.appendChild(priceDiv)

        document.getElementById("products-container").appendChild(productDiv)
    })

    form.addEventListener('submit', e => {
        e.preventDefault()
        sendData(e)
    })
})

const cc = document.getElementById("cc-info")

cc.addEventListener("onchange", e => {
    console.log(e.target.value)
})

console.log(cc.value)