/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length;
};

// 测试用例
console.log(argumentsLength(5)); // 输出: 1
console.log(argumentsLength({}, null, "3")); // 输出: 3
console.log(argumentsLength(1, 2, 3)); // 输出: 3
console.log(argumentsLength()); // 输出: 0
console.log(argumentsLength("a", [1, 2], {x: 1}, true, null)); // 输出: 5