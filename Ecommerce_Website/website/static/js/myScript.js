$('.plus-cart').click(function(){
    console.log('Button clicked')

    var id = $(this).attr('pid').toString()
    var quantitySpan = $(this).siblings('#quantity')
    
     $.ajax({
        type: 'GET',
        url: '/pluscart',
        data: {
            cart_id: id
        },
        
        success: function(data){
            console.log(data)
            quantitySpan.text(data.quantity)
            if (document.getElementById(`quantity${id}`)) {
                document.getElementById(`quantity${id}`).innerText = data.quantity;
            }
            
            if (document.getElementById(`summary-qty-${id}`)) {
                document.getElementById(`summary-qty-${id}`).innerText = data.quantity;
            }

            document.getElementById('amount_tt').innerText = parseFloat(data.amount).toFixed(2);
            document.getElementById('totalamount').innerText = parseFloat(data.total).toFixed(2);

            if (data.cart_length && data.cart_length >= 1) {
                $('#nav-cart').html('Cart <span class="count-badge" style="background-color: #ffffff !important; color: #db2777 !important; border-radius: 20px; font-size: 11px; font-weight: 800; padding: 2px 7px; margin-left: 6px; display: inline-block; line-height: 1.4; border: 1px solid rgba(255, 255, 255, 0.4);">' + data.cart_length + '</span>');
            } else {
                $('#nav-cart').html('Cart');
            }
        }
    })
})

$('.minus-cart').click(function(){
    console.log('Button clicked')

    var id = $(this).attr('pid').toString()
    var quantitySpan = $(this).siblings('#quantity')

    $.ajax({
        type: 'GET',
        url: '/minuscart',
        data: {
            cart_id: id
        },
        
        success: function(data){
            console.log(data)
            quantitySpan.text(data.quantity)
            if (document.getElementById(`quantity${id}`)) {
                document.getElementById(`quantity${id}`).innerText = data.quantity;
            }
            
            if (document.getElementById(`summary-qty-${id}`)) {
                document.getElementById(`summary-qty-${id}`).innerText = data.quantity;
            }

            document.getElementById('amount_tt').innerText = parseFloat(data.amount).toFixed(2);
            document.getElementById('totalamount').innerText = parseFloat(data.total).toFixed(2);

            if (data.cart_length && data.cart_length >= 1) {
                $('#nav-cart').html('Cart <span class="count-badge" style="background-color: #ffffff !important; color: #db2777 !important; border-radius: 20px; font-size: 11px; font-weight: 800; padding: 2px 7px; margin-left: 6px; display: inline-block; line-height: 1.4; border: 1px solid rgba(255, 255, 255, 0.4);">' + data.cart_length + '</span>');
            } else {
                $('#nav-cart').html('Cart');
            }
        }
    })
})

$('.remove-cart').click(function(e){
    e.preventDefault();
    var id = $(this).attr('pid').toString()
    
    var currentRow = $(this).closest('.cart-item-row');
    var adjacentHr = currentRow.next('hr');

    $.ajax({
        type: 'GET',
        url: '/removecart',
        data: {
            cart_id: id
        },

        success: function(data){
            document.getElementById('amount_tt').innerText = parseFloat(data.amount).toFixed(2);
            document.getElementById('totalamount').innerText = parseFloat(data.total).toFixed(2);
            
            currentRow.remove();
            adjacentHr.remove();

            if (document.getElementById(`summary-row-${id}`)) {
                document.getElementById(`summary-row-${id}`).remove();
            }

            if (data.cart_length && data.cart_length >= 1) {
                $('#nav-cart').html('Cart <span class="count-badge" style="background-color: #ffffff !important; color: #db2777 !important; border-radius: 20px; font-size: 11px; font-weight: 800; padding: 2px 7px; margin-left: 6px; display: inline-block; line-height: 1.4; border: 1px solid rgba(255, 255, 255, 0.4);">' + data.cart_length + '</span>');
            } else {
                $('#nav-cart').html('Cart');
                
                var cartView = document.getElementById('cart-view-container');
                if (cartView) {
                    cartView.style.display = 'none';
                }
                
                var containerDiv = document.querySelector('.container.my-5');
                if (containerDiv) {
                    var emptyTemplate = `
                        <div id="cart-empty-container" style="text-align: center; padding: 60px 20px; background-color: #ffffff; border: 1px solid #fbcfe8; border-radius: 12px; max-width: 500px; margin: 40px auto; box-shadow: 0 4px 12px rgba(219,39,119,0.02);">
                            <div style="font-size: 48px; color: #f472b6; margin-bottom: 16px;"><i class="fas fa-shopping-basket"></i></div>
                            <h2 class="text-center" style="color: #0f172a; font-weight: 800; font-size: 26px; margin: 0 0 10px 0; letter-spacing: -0.5px;">Your Cart is Empty</h2>
                            <p style="color: #64748b; font-size: 14px; margin-bottom: 20px;">Head back to our homepage to explore the collection</p>
                            <a href="/" class="btn btn-sm text-white" style="background-color: #db2777; padding: 10px 20px; border-radius: 6px; font-weight: bold; text-decoration: none; display: inline-block;">Return to Home Page</a>
                        </div>
                    `;
                    $(containerDiv).append(emptyTemplate);
                }
            }
        }
    })
})





