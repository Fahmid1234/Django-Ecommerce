// const plus = document.querySelector(".plus-cart"),
// minus = document.querySelector(".minus-cart"),
// num = document.querySelector("#quantity");
// let a = 1;

// plus.addEventListener("click", ()=>{
//   a++;
//   num.innerText = a;
// });
// minus.addEventListener("click", ()=>{
//   a--;
//   num.innerText = a;
// });

$(".plus-cart").click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[1];
    // console.log(id);
    $.ajax({
        type: "GET",
        url: "/plus_cart",
        data: {
            prod_id: id,
        },
        success: function (data) {
            eml.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.total_amount;
        },
    });
});


$(".minus-cart").click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[1];
    // console.log(id);
    $.ajax({
      type: "GET",
      url: "/minus_cart",
      data: {
        prod_id: id,
      },
      success: function (data) {
        eml.innerText = data.quantity;
        document.getElementById("amount").innerText = data.amount;
        document.getElementById("totalamount").innerText = data.total_amount;
      },
    });
  });

  $(".remove-cart").click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this;
    // console.log(id);
    $.ajax({
      type: "GET",
      url: "/remove_cart",
      data: {
        prod_id: id,
      },
      success: function (data) {
        document.getElementById("amount").innerText = data.amount;
        document.getElementById("totalamount").innerText = data.total_amount;
        eml.parentNode.parentNode.parentNode.parentNode.remove();
      },
    });
  });
  