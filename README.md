### Introduction
- This is the week 10 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. Define a function called `register student` that takes two mandatory input arguments `first_name` and `last_name`.
   - If there is any other positional argument, take the first one as `middle_name`
   - The keyword argument can take **optional** keywords like `semester`, `year` and `course`.
   - Return a formatted string based on the input. '`{first_name} {last_name} {<middle_name>} is registered for {semester} {year} {course}`'
   - For example:
       - `register_student('Jane', 'Doe', semester='Summer', year='2023')` => `'Jane Doe is registered for Summer 2023'`
       - `register_student('John', 'Doe', 'Jack', semester='Summer', year='2023', course='AC4RM')` => `'John Jack Doe is registered for Summer 2023 AC4RM'`
2. Write SQL queries to do the following:
   - Find all the invoices that are greater than the client's average invoice amount.
   - Find all the products that have never been ordered from the `products` and `order_items` table.
3. Using the 10 principal components from the lecture, train a logistic regression model to predict whether the patient has cancer or not.
   - Split the data into training and testing set (80/20) and use a random seed of 42.
   - Return the model you trained and the predictions on the test set.
   - Compare the test score with the logistic regression model trained on the original dataset (before running PCA) and see which one gives you a better result.
4. Write a regex pattern that will capture the twitter handle ("@janedoe") in the string. However, the string might contain email address (jane.doe@gmail.com).
   - We want the regex pattern to only return the twitter handle. For example:
   - `re.findall(regex_pattern, "His email is john.doe@gmail.com and twitter is @johndoe")` => `[@johndoe]`  
