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
            if(resp.ok) // если возникла ошибка, то срабатывает исключение и кадет в catch
                throw new Error("HTTP-Error: " + response.status);
            return resp.json();
        });
    
        return response.json();
    } catch(error) {
        console.error("Error", error);
    }
}

console.log("hello world");
