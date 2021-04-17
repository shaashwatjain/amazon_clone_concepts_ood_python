from cart import *
from user import change_details, details


def testCreateCart(done):
    # No username
    try:
        new_cart()
        done(False, "Cart is created even if a user is not provided")
    except:
        done(True, "Cart is not created if a user is not provided")

    # Valid username
    try:
        new_cart("test")
        done(True, "Cart is created only if a user is provided")
    except:
        done(False, "Cart is not created even if user is provided")


def testIsCartEmpty(done):
    # Cart must be empty
    try:
        assert is_empty_cart("test") == True
        done(True, "Cart is empty as expected")
    except:
        done(False, "Cart is not empty when it should be")

    # Add item
    try:
        cart = carts["test"]
        item = Item("soap", "Body soap", 100, 10,
                    ["https://5.imimg.com/data5/LW/GN/MY-4990337/bath-soap-500x500.jpg"], "test")
        cart.add_to_cart(item, qty=1)
    except:
        done(False, "Failed to add item to cart")
        return

    # Cart must not be empty
    try:
        assert is_empty_cart("test") == False
        done(True, "Cart is not empty as expected")
    except:
        done(False, "Cart is empty when it should not be")


def testUpdateCartItemQty(done):
    # Get old qty
    cart = carts["test"]
    old_qty = cart.items[0][1]

    # Update qty - should fail if negative quantity
    try:
        assert update_cart_item("test", 0, -1) == False
        done(True, "Cart item quanity is not updated with -ve qty")
    except:
        done(False, "Cart item quantity is updated when it should not be. (-ve qty)")
        return

    # Update qty
    try:
        assert update_cart_item("test", 0, old_qty+1) == True
    except:
        done(False, "Could not update cart item quantity")
        return

    # Ensure qty has changed to new value
    new_qty = cart.items[0][1]
    try:
        assert new_qty == old_qty + 1
        done(True, "Cart item quanity is updated to the correct value")
    except:
        done(False, "Cart item quantityis not updated to the correct value")


def testDeleteCartItem(done):
    # Get number of items in cart
    cart = carts["test"]
    # old_count = len(cart.items)
    old_count = len(list(filter(lambda item: item[1] > 0, cart.items or [])))

    # Delete item - should fail for non-existent item
    try:
        assert delete_cart_item("test", 100) == False
        done(True, "Cart does not delete a non-existent item")
    except:
        done(False, "Cart deletes a non-existent item")
        return

    # Delete item
    try:
        assert delete_cart_item("test", 0) == True
    except:
        done(False, "Cold not delete item from cart")
        return

    # Ensure number of items in cart has reduced
    # new_count = len(cart.items)
    new_count = len(list(filter(lambda item: item[1] > 0, cart.items or [])))
    try:
        assert new_count == old_count - 1
        done(True, "Item is deleted from cart")
    except:
        done(False, "Item is not deleted from cart")


def testBuyCart(done):
    # Init
    details["test"] = User("test", "test")
    details["test"].change_details("test", address="#42, Test address, India")

    # Try to buy empty cart
    try:
        assert buy("test") == False
        done(True, "Buying an empty cart is not possible as expected")
    except:
        done(False, "Buying an empty cart is possible when it should not be")

    # Add item
    try:
        cart = carts["test"]
        item = Item("soap", "Body soap", 100, 10,
                    "https://5.imimg.com/data5/LW/GN/MY-4990337/bath-soap-500x500.jpg", "test")
        cart.add_to_cart(item, qty=1)
    except:
        done(False, "Failed to add item to cart")
        return

    # Buy successfully
    try:
        assert buy("test") == True
        assert cart.items is None
        done(True, "Buying from cart is successful")
    except:
        done(False, "Buying from cart is not successful")
