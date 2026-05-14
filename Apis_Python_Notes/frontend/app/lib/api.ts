const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";

async function handleResponse(res: Response) {
  const data = await res.json();
  if (!res.ok) {
    // If backend returns a detail message (like FastAPI HTTPException), use it.
    throw new Error(data.detail || "Ocurrió un error en la API");
  }
  return data;
}

export async function fetchData(endpoint: string) {
  const res = await fetch(`${API_URL}${endpoint}`, {
    cache: "no-store",
  });
  return handleResponse(res);
}

export async function postData(endpoint: string, data: any) {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return handleResponse(res);
}

export async function putData(endpoint: string, data: any) {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return handleResponse(res);
}

export async function deleteData(endpoint: string) {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: "DELETE",
  });
  return handleResponse(res);
}
