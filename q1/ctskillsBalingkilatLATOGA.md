Main Problem: The lack of crowd control due to slow service in the Canteen.

SUB-PROBLEMS:
1) The student's unhurried pace of choosing their order.

2) The cashier's traditional way of computing money.

3) The system's disordered system of tracking food supplies.

CT SKILLS:
1) The student's unhurried pace of choosing their order. 
   CT SKILL: Decomposition
   SOLUTION: Display a menu with food options and prices so that students can choose more efficiently.

2) The cashier's traditional way of computing money.
   CT SKILL: Automation
   SOLUTION: Create an automatic calculator using codes that can efficiently compute money.

3) The system's disordered system of tracking food supplies.
   CT SKILL: Pattern Recognition
   SOLUTION: Create a system that can keep track of foods that are more frequently sold, and can monitor their supply quantities.



Pseudocode:
'''
// Canteen Food Supply Tracking

FUNCTION ProcessOrder(itemID, quantity):
    IF inventory[itemID].stock >= quantity THEN
        // Deduct ordered amount
        inventory[itemID].stock = inventory[itemID].stock - quantity
        
        // Alert if stock is low
        IF inventory[itemID].stock <= inventory[itemID].reorderLimit THEN
            DISPLAY "Low Stock Alert: " + itemID
        ENDIF
        RETURN "Order Processed"
    ELSE
        RETURN "Error: Out of Stock"
    ENDIF
END FUNCTION

FUNCTION RestockItem(itemID, quantity):
    inventory[itemID].stock = inventory[itemID].stock + quantity
    DISPLAY "Stock Updated for " + itemID
END FUNCTION
'''
