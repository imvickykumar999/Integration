import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
import AuthPage from './component/AuthPage';
import ERPDashboard from './component/ERPDashboard';
import AddEmployeeForm from './component/AddEmployeeForm';
import EmployeeListPage from './component/EmployeeListPage';
import ProtectedRoute from './components/ProtectedRoute';
import CompanyDashboard from './component/CompanyDashboard';

function App() {
    const { isAuthenticated, user } = useSelector((state) => state.auth);

    return (
        <Router>
            <Routes>
                <Route
                    path="/"
                    element={
                        isAuthenticated ? <Navigate to="/dashboard" replace /> : <AuthPage />
                    }
                />
                <Route
                    path="/company-dashboard"
                    element={
                        <ProtectedRoute>
                            {user && user.role === 'PARENT' ? <CompanyDashboard /> : <ERPDashboard />}
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/add-employee"
                    element={
                        <ProtectedRoute>
                            <AddEmployeeForm />
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/employee-list"
                    element={
                        <ProtectedRoute>
                            <EmployeeListPage />
                        </ProtectedRoute>
                    }
                />
            </Routes>
        </Router>
    );
}

export default App;
