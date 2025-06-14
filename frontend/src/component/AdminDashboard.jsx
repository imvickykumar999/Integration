import React from 'react';
import { Users, Building2, UserPlus, Settings, TreePine } from 'lucide-react';

const AdminDashboard = () => {
  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: 'white',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    }}>
      <div style={{
        maxWidth: '1200px',
        margin: '0 auto',
        padding: '40px 20px'
      }}>
        {/* Header Section */}
        <div style={{
          marginBottom: '40px'
        }}>
          <h1 style={{
            color: 'black',
            fontSize: '32px',
            fontWeight: 'bold',
            margin: '0 0 8px 0',
            letterSpacing: '-0.5px'
          }}>
            SheGeeks - Admin Dashboard
          </h1>
          <p style={{
            color: '#666',
            fontSize: '16px',
            margin: '0',
            fontWeight: '400'
          }}>
            Welcome, Admin! Here you can manage company employees.
          </p>
        </div>

        {/* Statistics Cards */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '24px',
          marginBottom: '40px'
        }}>
          {/* Employees Card */}
          <div style={{
            backgroundColor: '#7E44EE',
            borderRadius: '12px',
            padding: '32px',
            color: 'white',
            position: 'relative',
            boxShadow: '0 4px 12px rgba(126, 68, 238, 0.15)',
            transition: 'transform 0.2s ease, box-shadow 0.2s ease'
          }}
          onMouseEnter={(e) => {
            e.target.style.transform = 'translateY(-2px)';
            e.target.style.boxShadow = '0 8px 24px rgba(126, 68, 238, 0.25)';
          }}
          onMouseLeave={(e) => {
            e.target.style.transform = 'translateY(0)';
            e.target.style.boxShadow = '0 4px 12px rgba(126, 68, 238, 0.15)';
          }}>
            <div style={{
              display: 'flex',
              alignItems: 'flex-start',
              justifyContent: 'space-between',
              marginBottom: '20px'
            }}>
              <div>
                <h3 style={{
                  fontSize: '18px',
                  fontWeight: '600',
                  margin: '0 0 8px 0'
                }}>
                  Employees
                </h3>
                <div style={{
                  fontSize: '36px',
                  fontWeight: 'bold',
                  margin: '0'
                }}>
                  3
                </div>
              </div>
              <Users size={32} style={{ opacity: 0.9 }} />
            </div>
            <div style={{
              fontSize: '14px',
              opacity: 0.9,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '4px'
            }}>
              View All Employees →
            </div>
          </div>

          {/* Departments Card */}
          <div style={{
            backgroundColor: '#7E44EE',
            borderRadius: '12px',
            padding: '32px',
            color: 'white',
            position: 'relative',
            boxShadow: '0 4px 12px rgba(126, 68, 238, 0.15)',
            transition: 'transform 0.2s ease, box-shadow 0.2s ease'
          }}
          onMouseEnter={(e) => {
            e.target.style.transform = 'translateY(-2px)';
            e.target.style.boxShadow = '0 8px 24px rgba(126, 68, 238, 0.25)';
          }}
          onMouseLeave={(e) => {
            e.target.style.transform = 'translateY(0)';
            e.target.style.boxShadow = '0 4px 12px rgba(126, 68, 238, 0.15)';
          }}>
            <div style={{
              display: 'flex',
              alignItems: 'flex-start',
              justifyContent: 'space-between',
              marginBottom: '20px'
            }}>
              <div>
                <h3 style={{
                  fontSize: '18px',
                  fontWeight: '600',
                  margin: '0 0 8px 0'
                }}>
                  Departments
                </h3>
                <div style={{
                  fontSize: '36px',
                  fontWeight: 'bold',
                  margin: '0'
                }}>
                  N/A
                </div>
              </div>
              <Building2 size={32} style={{ opacity: 0.9 }} />
            </div>
            <div style={{
              fontSize: '14px',
              opacity: 0.9,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '4px'
            }}>
              Manage Departments →
            </div>
          </div>
        </div>

        {/* Quick Actions Section */}
        <div style={{
          backgroundColor: 'white',
          border: '1px solid #e0e0e0',
          borderRadius: '12px',
          padding: '32px',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.04)'
        }}>
          <h2 style={{
            color: 'black',
            fontSize: '24px',
            fontWeight: 'bold',
            margin: '0 0 24px 0'
          }}>
            Quick Actions
          </h2>

          <div style={{
            display: 'flex',
            flexDirection: 'column',
            gap: '16px'
          }}>
            {/* Add New Employee */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '16px',
              padding: '16px',
              border: '1px solid #f0f0f0',
              borderRadius: '8px',
              cursor: 'pointer',
              transition: 'all 0.2s ease',
              backgroundColor: 'white'
            }}
            onMouseEnter={(e) => {
              e.target.style.backgroundColor = '#f8f8f8';
              e.target.style.borderColor = '#7E44EE';
              e.target.style.transform = 'translateX(4px)';
            }}
            onMouseLeave={(e) => {
              e.target.style.backgroundColor = 'white';
              e.target.style.borderColor = '#f0f0f0';
              e.target.style.transform = 'translateX(0)';
            }}>
              <UserPlus size={24} color="black" />
              <span style={{
                color: 'black',
                fontSize: '16px',
                fontWeight: '500'
              }}>
                Add New Employee
              </span>
            </div>

            {/* Manage Existing Employees */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '16px',
              padding: '16px',
              border: '1px solid #f0f0f0',
              borderRadius: '8px',
              cursor: 'pointer',
              transition: 'all 0.2s ease',
              backgroundColor: 'white'
            }}
            onMouseEnter={(e) => {
              e.target.style.backgroundColor = '#f8f8f8';
              e.target.style.borderColor = '#7E44EE';
              e.target.style.transform = 'translateX(4px)';
            }}
            onMouseLeave={(e) => {
              e.target.style.backgroundColor = 'white';
              e.target.style.borderColor = '#f0f0f0';
              e.target.style.transform = 'translateX(0)';
            }}>
              <Users size={24} color="black" />
              <span style={{
                color: 'black',
                fontSize: '16px',
                fontWeight: '500'
              }}>
                Manage Existing Employees
              </span>
            </div>

            {/* Manage Departments */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '16px',
              padding: '16px',
              border: '1px solid #f0f0f0',
              borderRadius: '8px',
              cursor: 'pointer',
              transition: 'all 0.2s ease',
              backgroundColor: 'white'
            }}
            onMouseEnter={(e) => {
              e.target.style.backgroundColor = '#f8f8f8';
              e.target.style.borderColor = '#7E44EE';
              e.target.style.transform = 'translateX(4px)';
            }}
            onMouseLeave={(e) => {
              e.target.style.backgroundColor = 'white';
              e.target.style.borderColor = '#f0f0f0';
              e.target.style.transform = 'translateX(0)';
            }}>
              <Settings size={24} color="black" />
              <span style={{
                color: 'black',
                fontSize: '16px',
                fontWeight: '500'
              }}>
                Manage Departments
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;