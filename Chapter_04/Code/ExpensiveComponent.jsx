import React from "react";
const ExpensiveComponent = React.memo(({ value }) => {
    console.log("Rendering Expensive Component...");
    return <div>Value: {value}</div>;
});
export default ExpensiveComponent;
