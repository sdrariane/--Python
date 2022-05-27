<h1> 👽 Linear Regression Algorithm </h1>

<p>In a few words, linear regression is a statistical method for modeling relationships between a dependent variable with a given set of independent variables. It is okay if you did not understand a damn thing - at first, neither me - but we gonna dissecate that terms before see the code.</p>

<p> **Independent Variables:** is the cause. Its value is independent of other variables in your study. </p>

> Is the temperature of the room. You vary the room temperature by making it cooler for half the participants, and warmer for the other half.

<p> **Dependent Variables:** is the effect. Its value depends on changes in the independent variable.</p>

> Is math test scores. You measure the math skills of all participants using a standardized test and check whether they differ based on room temperature.

<p> So, that code represents the relationship between a extrinsic parameter of the human factor (independent variable) and another intrinsic parameter of the human factor (dependent variable).</p>

<h2>🛸 Simple Linear Regression </h2>
<p>Is an approach for predicting a response using a single feature. It is assumed that the two variables are **linearly related**. Hence, we try to find a linear function that predicts the response value(y) as accurately as possible as a function of the feature or independent variable(x). Let us consider a dataset where we have a value of response ***y*** for every feature ***x***:</p>

>A linear relationship is one where increasing or decreasing one variable ***n*** times will cause a corresponding increase or decrease of ***n*** times in the other variable too. In simpler words, if you double one variable, the other will double as well.

Dataset | v1 | v2 | v3 | v4 | v5 | v6 | v7 | v8 | v9 | v10
|:-----:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
***x*** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
***y*** | 1 | 3 | 2 | 5 | 7 | 8 | 8 | 9 | 10 | 12 |

<p> For generality, we define:</p>

- ***x*** as feature vector, i.e ***x*** = [x_1, x_2, …., x_n],
- ***y*** as response vector, i.e ***y*** = [y_1, y_2, …., y_n]
- for ***n*** observations (in above example, n=10).

<p> A scatter plot of the above dataset looks like: </p>

![](https://media.geeksforgeeks.org/wp-content/uploads/python-linear-regression-1.png)

<p>Now, the task is to find ***a line that fits best in the above scatter plot*** so that we can predict the response for any new feature values. (i.e a value of ***x*** not present in a dataset). This line is called a ***regression line***. The equation of regression line is represented as: </p>

$$h(x_i)= β_0 + β_1 ⋅ x_i$$

<p>The first part represents the predicted response value for ith observation; the second and third part about β are regression coefficients and represent y-intercept and slope of regression line respectively - once we’ve estimated these coefficients, we can use the model to predict responses! Now consider:</p>

$$y_i = β_0 + β_i ⋅ x_i + ε_i  = h(x_i) + ε_i$$

$$ε_i = y_i - h(x_i)$$

<p>Here, ε is a residual error in ith observation.  So, our aim is to minimize the total residual error. We define the squared error or cost function, J as: </p>

$$J(β_0, β_1) = (1/2n) ⋅ \sum_{i=1}^n ε_i^2$$

<p>The values in the parentheses of J are the determined values.</p>

$$β_1 = SS_xy/SS_xx$$

$$β_0 = y̅ -β _1 ⋅ x̅$$

$$SS_xy = \sum_{i=1}^n (x_i - x̅) ⋅ (y_i - y̅) = \sum_{i=1}^n (y_i⋅x_i - n ⋅ x̅ ⋅ y̅)$$

$$SS_xx = \sum_{i=1}^n (x_i - x̅)^2 = \sum_{i=1}^n (x_i^2 - n ⋅ (x̅)^2)$$

<p>And graph obtained looks like this:</p>

![](https://media.geeksforgeeks.org/wp-content/uploads/python-linear-regression-2.png)
