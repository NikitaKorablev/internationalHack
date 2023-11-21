async function postData(url = "", data = {}) {
    try {
        const response = await fetch(url, { 
            method: 'POST', // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
        .then(resp => {
            if(!resp.ok) // если возникла ошибка, то срабатывает исключение и кадет в catch
                throw new Error("HTTP-Error: " + resp.status);
            return resp;
        });
    
        return response.json();
    } catch(error) {
        console.error("Error", error);
    }
}

async function postFile(url = "/api/v1.0/post", fetchOptions) {
    try {
        const response = await fetch(url, fetchOptions)
        .then(resp => {
            if(!resp.ok) // если возникла ошибка, то срабатывает исключение и кадет в catch
                throw new Error("HTTP-Error: " + resp.status);
            return resp;
        });
    
        return response.json();
    } catch(error) {
        console.error("Error", error);
    }
}

async function getData(url = "") {
    try {
        const response = await fetch(url, { 
            method: 'GET', // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            }
        })
        .then(resp => {
            if(!resp.ok) // если возникла ошибка, то срабатывает исключение и кадет в catch
                throw new Error("HTTP-Error: " + resp.status);
            return resp;
        });
    
        return response.json();
    } catch(error) {
        console.error("Error", error);
    }
}