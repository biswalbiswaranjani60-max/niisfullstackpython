import React, { useState } from "react";

function EmployeeForm() {
  const [employee, setEmployee] = useState({
    name: "",
    email: "",
    password: "",
    department: ""
  });

  const [data, setData] = useState([]);

  // handle input change
  const handleChange = (e) => {
    setEmployee({ ...employee, [e.target.name]: e.target.value });
  };

  // handle form submit
  const handleSubmit = (e) => {
    e.preventDefault();

    if (!employee.name || !employee.email || !employee.password || !employee.department) {
      alert("All fields are required!");
      return;
    }

    setData([...data, employee]);

    setEmployee({
      name: "",
      email: "",
      password: "",
      department: ""
    });
  };

  return (
    <div className="container">
      <h2>Employee Registration</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Enter Name"
          value={employee.name}
          onChange={handleChange}
        />

        <input
          type="email"
          name="email"
          placeholder="Enter Email"
          value={employee.email}
          onChange={handleChange}
        />

        <input
          type="password"
          name="password"
          placeholder="Enter Password"
          value={employee.password}
          onChange={handleChange}
        />

        <input
          type="text"
          name="department"
          placeholder="Enter Department"
          value={employee.department}
          onChange={handleChange}
        />

        <button type="submit">Register</button>
      </form>

      <h3>Employee List</h3>

      <table border="1">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Department</th>
          </tr>
        </thead>
        <tbody>
          {data.map((emp, index) => (
            <tr key={index}>
              <td>{emp.name}</td>
              <td>{emp.email}</td>
              <td>{emp.department}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EmployeeForm;