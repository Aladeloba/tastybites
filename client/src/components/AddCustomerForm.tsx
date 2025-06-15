import React, { useState } from "react";
import axios from "axios";
import { NewCustomer } from "../types";

// ✅ Default form values declared outside the component
const defaultForm: NewCustomer = {
  first_name: "",
  surname: "",
  middle_name: "",
  date_of_birth: "",
  home_address: "",
  date_of_registration: "",
  matric_field: "_23120111037",
};

const AddCustomerForm: React.FC = () => {
  const [form, setForm] = useState<NewCustomer>(defaultForm);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.post("http://127.0.0.1:8000/customers/", form);
      alert("Customer added!");
      setForm(defaultForm); // reset form
    } catch (err) {
      console.error(err);
      alert("Failed to add customer.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Customer</h2>
      {Object.entries(form).map(([key, value]) => (
        <div key={key} style={{ marginBottom: "10px" }}>
          <label>{key.replace(/_/g, " ")
            .replace(/\b\w/g, (char) => char.toUpperCase())}:</label> <br />
          <input
            type={key.includes("date") ? "date" : "text"}
            name={key}
            value={value}
            onChange={handleChange}
            required={key !== "middle_name"}
          />
        </div>
      ))}
      <button type="submit" style={{ background: "orange", color: "white" }}>
        Add Customer
      </button>
    </form>
  );
};

export default AddCustomerForm;
