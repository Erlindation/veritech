const BASE_URL = 'http://localhost:8000';

function getToken() {
    return localStorage.getItem('token');
}

export async function login(email, password) {
    const res = await fetch(`${BASE_URL}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    });
    if (!res.ok) throw new Error('Credenciales incorrectas');
    const data = await res.json();
    localStorage.setItem('token', data.access_token);
}

export async function register(email, password) {
    const res = await fetch(`${BASE_URL}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    });
    if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || 'Error al registrarse');
    }
    return res.json();
}

export async function getClaims() {
    const res = await fetch(`${BASE_URL}/claims/`, {
        headers: { 'Authorization': `Bearer ${getToken()}` }
    });
    if (res.status === 401) {
        localStorage.removeItem('token');
        window.location.href = 'index.html';
        return [];
    }
    return res.json();
}

export async function createClaim(text) {
    const res = await fetch(`${BASE_URL}/claims/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`
        },
        body: JSON.stringify({ text })
    });
    if (!res.ok) throw new Error('Error al enviar la afirmación');
    return res.json();
}

export async function updateClaim(id, text) {
    const res = await fetch(`${BASE_URL}/claims/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`
        },
        body: JSON.stringify({ text })
    });
    if (!res.ok) throw new Error('Error al actualizar');
    return res.json();
}

export async function deleteClaim(id) {
    const res = await fetch(`${BASE_URL}/claims/${id}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${getToken()}` }
    });
    if (!res.ok) throw new Error('Error al eliminar');
}
