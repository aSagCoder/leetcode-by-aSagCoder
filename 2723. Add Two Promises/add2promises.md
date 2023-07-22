# 2723. Add Two Promises 

<a href="https://leetcode.com/problems/add-two-promises/description/"> Description Here </a>

# SOLUTION - 

```js
/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    const num1 = await promise1;
    const num2 = await promise2;

    const sum = num1 + num2

    return Promise.resolve(sum)
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
```
