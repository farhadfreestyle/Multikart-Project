// let url = '/cartapi';

// fetch(url)

//     .then((response) => {
//         return response.json()
//     })

//     .then(data => {
//         let basketIcon = document.querySelector("#cart-icon");
//         basketIcon.innerHTML = "";
//         console.log(data[0])

//         for (let i = 0; i < data.length; i++) {
//             console.log(data.length)
//             basketIcon.innerHTML += `<li>
//                                                 <div class="media"
//                                                 data-product =`${data[i].id}`>
//                                                     <a href="#"><img class="mr-3"
//                                                                      src=""
//                                                                      alt=" Generic placeholder image"></a>
//                                                     <div class="media-body">
//                                                         <a href="#">
//                                                             <h4>`${data[i].product.name}`</h4>
//                                                         </a>    
//                                                         <h4><span>`${data[i].quantity}` x `${data[i].product.price}`</span></h4>
//                                                     </div>
//                                                 </div>
//                                                 <div class="close-circle">
//                                                     <a href="#"><i class="fa fa-times" aria-hidden="true"></i></a>
//                                                 </div>
//                                             </li>`
//         }


//     })