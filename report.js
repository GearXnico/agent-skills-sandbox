const chalk = require("chalk");
const { groupBy } = require("lodash");

function report(orders) {
  const byStatus = groupBy(orders, "status");
  return Object.keys(byStatus)
    .sort()
    .map((status) => `${chalk.bold(status)}: ${byStatus[status].length}`)
    .join("\n");
}

module.exports = { report };
