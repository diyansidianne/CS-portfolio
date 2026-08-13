# Annex A
## Computational Thinking Exercise: "Smart School Canteen Queue"

**Section:** Balingkilat **Score:** ______________

**C# / Name:** 24 Dianne Latoga, 23 Henriah Angela Fetalvero, 22 Charlize Sky Dogillo **Date:** 08/13/2026


Scenario


The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:


Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.


**Step 1: Identify the Big Problem**


Main Problem: The lack of crowd control due to slow service in the Canteen.


**Step 2: Identify three to four Sub-Problems**

Please list possible sub-problems:

1. The student's unhurried pace of choosing their order.
2. The cashier's traditional way of computing money.
3. The system's disordered system of tracking food supplies.


**Step 3: Define Computational Thinking Approaches**

For each sub-problem, apply CT skills:

| Sub-Problem | CT Skill | Example Solution |
| ----------- | ----------- | ----------- |
| The student's unhurried pace of choosing their order.  | Decomposition | Display a menu with food options and prices so that students can choose more efficiently. |
| The cashier's traditional way of computing money. | Automation | Create an automatic calculator using codes that can efficiently compute money. |
| The system's disordered system of tracking food supplies. | Pattern Recognition | Create a system that can keep track of foods that are more frequently sold, and can monitor their supply quantities. |


**Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem**

```
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
```
