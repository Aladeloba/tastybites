import React, { useEffect, useState } from "react";
import axios from "axios";
import { Customer } from "../types";

const CustomerList: React.FC = () => {
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [editData, setEditData] = useState<Partial<Customer>>({});

  // Fetch customers
  const fetchCustomers = () => {
    axios
      .get("http://127.0.0.1:8000/customers/")
      .then((res) => setCustomers(res.data))
      .catch((err) => console.error("Failed to fetch customers", err));
  };

  useEffect(() => {
    fetchCustomers();
  }, []);

  const startEdit = (customer: Customer) => {
    setEditingId(customer.id!);
    setEditData(customer);
  };

  const handleEditChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEditData({ ...editData, [e.target.name]: e.target.value });
  };

  const saveEdit = async () => {
    if (!editingId) return;
    try {
      await axios.put(`http://127.0.0.1:8000/customers/${editingId}`, editData);
      setEditingId(null);
      fetchCustomers();
    } catch (err) {
      console.error("Update failed", err);
    }
  };

  const deleteCustomer = async (id: number) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/customers/${id}`);
      fetchCustomers();
    } catch (err) {
      console.error("Delete failed", err);
    }
  };

  return (
    <div>
      <h2 style={{ color: "orange" }}>Customer List</h2>
      <ul>
        {customers.map((c) => (
          <li key={c.id} style={{ marginBottom: "1rem", border: "1px solid orange", padding: "10px", borderRadius: "8px" }}>
            {editingId === c.id ? (
              <>
                <input name="first_name" value={editData.first_name || ""} onChange={handleEditChange} />
                <input name="surname" value={editData.surname || ""} onChange={handleEditChange} />
                <br />
                <button onClick={saveEdit} style={{ marginRight: "5px" }}>💾 Save</button>
                <button onClick={() => setEditingId(null)}>Cancel</button>
              </>
            ) : (
              <>
                <strong>{c.first_name} {c.surname}</strong><br />
                DOB: {c.date_of_birth}<br />
                Address: {c.home_address}<br />
                Registered: {c.date_of_registration}<br />
                <button onClick={() => startEdit(c)}>✏️ Edit</button>
                <button
                  onClick={() => deleteCustomer(c.id)}
                  style={{ marginLeft: "5px", backgroundColor: "crimson", color: "white" }}
                >
                  🗑️ Delete
                </button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CustomerList;
