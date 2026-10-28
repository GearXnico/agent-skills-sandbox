const assert = require("node:assert");
const { report } = require("./report");

const output = report([{ status: "paid" }, { status: "pending" }, { status: "paid" }]);
assert.match(output, /paid.*: 2/);
assert.match(output, /pending.*: 1/);
console.log("tests passed");
