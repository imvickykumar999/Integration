import React from 'react';

const EmployeeListPage = () => {
  // Mock employee data
  const employees = [
    {
      id: 'EMP001',
      name: 'Sarah Johnson',
      department: 'Human Resources',
      position: 'HR Manager',
      email: 'sarah.johnson@company.com',
      phone: '(555) 123-4567',
      status: 'Active'
    },
    {
      id: 'EMP002',
      name: 'Michael Chen',
      department: 'Engineering',
      position: 'Senior Software Engineer',
      email: 'michael.chen@company.com',
      phone: '(555) 234-5678',
      status: 'Active'
    },
    {
      id: 'EMP003',
      name: 'Emily Rodriguez',
      department: 'Marketing',
      position: 'Marketing Coordinator',
      email: 'emily.rodriguez@company.com',
      phone: '(555) 345-6789',
      status: 'Deactive'
    },
    {
      id: 'EMP004',
      name: 'David Thompson',
      department: 'Finance',
      position: 'Financial Analyst',
      email: 'david.thompson@company.com',
      phone: '(555) 456-7890',
      status: 'Active'
    },
    {
      id: 'EMP005',
      name: 'Lisa Park',
      department: 'Operations',
      position: 'Operations Manager',
      email: 'lisa.park@company.com',
      phone: '(555) 567-8901',
      status: 'Active'
    },
    {
      id: 'EMP006',
      name: 'James Wilson',
      department: 'Engineering',
      position: 'DevOps Engineer',
      email: 'james.wilson@company.com',
      phone: '(555) 678-9012',
      status: 'Deactive'
    },
    {
      id: 'EMP007',
      name: 'Amanda Foster',
      department: 'Sales',
      position: 'Sales Representative',
      email: 'amanda.foster@company.com',
      phone: '(555) 789-0123',
      status: 'Active'
    },
    {
      id: 'EMP008',
      name: 'Robert Kim',
      department: 'IT Support',
      position: 'IT Specialist',
      email: 'robert.kim@company.com',
      phone: '(555) 890-1234',
      status: 'Active'
    },
    {
      id: 'EMP009',
      name: 'Jessica Brown',
      department: 'Legal',
      position: 'Legal Counsel',
      email: 'jessica.brown@company.com',
      phone: '(555) 901-2345',
      status: 'Deactive'
    }
  ];

  const StatusPill = ({ status }) => {
    const isActive = status === 'Active';
    
    const pillStyle = {
      display: 'inline-block',
      padding: '4px 12px',
      borderRadius: '16px',
      fontSize: '12px',
      fontWeight: '600',
      color: 'white',
      backgroundColor: isActive ? '#10b981' : '#ef4444',
      textAlign: 'center',
      minWidth: '70px'
    };

    return <span style={pillStyle}>{status}</span>;
  };

  const containerStyle = {
    padding: '24px',
    backgroundColor: '#f3f4f6',
    minHeight: '100vh',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
  };

  const headingStyle = {
    fontSize: '28px',
    fontWeight: '700',
    color: '#8b5cf6',
    marginBottom: '24px',
    letterSpacing: '-0.025em'
  };

  const cardStyle = {
    backgroundColor: 'white',
    borderRadius: '8px',
    boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
    overflow: 'hidden'
  };

  const tableStyle = {
    width: '100%',
    borderCollapse: 'collapse'
  };

  const headerStyle = {
    backgroundColor: '#8b5cf6',
    borderBottom: '1px solid #7c3aed'
  };

  const headerCellStyle = {
    padding: '12px 16px',
    textAlign: 'left',
    fontSize: '14px',
    fontWeight: '600',
    color: 'white',
    textTransform: 'uppercase',
    letterSpacing: '0.05em'
  };

  const rowStyle = {
    borderBottom: '1px solid #f3f4f6',
    transition: 'background-color 0.15s ease-in-out'
  };

  const cellStyle = {
    padding: '16px',
    fontSize: '16px',
    color: '#374151'
  };

  const nameStyle = {
    fontWeight: '600',
    color: '#111827'
  };

  const emailStyle = {
    color: '#6b7280'
  };

  return (
    <div style={containerStyle}>
      <h1 style={headingStyle}>Employees</h1>
      
      <div style={cardStyle}>
        <table style={tableStyle}>
          <thead style={headerStyle}>
            <tr>
              <th style={headerCellStyle}>Employee ID</th>
              <th style={headerCellStyle}>Name</th>
              <th style={headerCellStyle}>Department</th>
              <th style={headerCellStyle}>Position</th>
              <th style={headerCellStyle}>Email</th>
              <th style={headerCellStyle}>Phone</th>
              <th style={headerCellStyle}>Status</th>
            </tr>
          </thead>
          <tbody>
            {employees.map((employee, index) => (
              <tr 
                key={employee.id} 
                style={{
                  ...rowStyle,
                  backgroundColor: index % 2 === 0 ? 'white' : '#fafafa'
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.backgroundColor = '#ede9fe';
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.backgroundColor = index % 2 === 0 ? 'white' : '#fafafa';
                }}
              >
                <td style={cellStyle}>
                  <span style={{ fontFamily: 'monospace', fontSize: '13px' }}>
                    {employee.id}
                  </span>
                </td>
                <td style={{...cellStyle, ...nameStyle}}>{employee.name}</td>
                <td style={cellStyle}>{employee.department}</td>
                <td style={cellStyle}>{employee.position}</td>
                <td style={{...cellStyle, ...emailStyle}}>{employee.email}</td>
                <td style={cellStyle}>{employee.phone}</td>
                <td style={cellStyle}>
                  <StatusPill status={employee.status} />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default EmployeeListPage;