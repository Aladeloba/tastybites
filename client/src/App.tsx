import React from 'react';
import AddCustomerForm from "./components/AddCustomerForm";
import CustomerList from "./components/CustomerList";

const App: React.FC = () => {
  return (
    <div style={{padding: "20px", fontFamily: "Arial", backgroundColor: "#fff7f0"}}>
      <h1 style={{color: "orange"}}>
        TastyBites Customer Manager
      </h1>
      <AddCustomerForm/>
      <hr />
      <CustomerList />
    </div>
  );
};

export default App;
