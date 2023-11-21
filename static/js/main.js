// JS code

// getData(url = "/api/v1.0/get").then(resp => {
//     console.log(resp);
// })



// myForm.addEventListener('submit', event => {
//   console.log(myForm.files[0]);
  
//   const url = new URL(myForm.action);
//   const formData = new FormData(myForm);

//   console.log(myForm.files[0]);

//   const fetchOptions = {
//     method: myForm.method,
//     body: formData
//   }

//   console.log(fetchOptions);
//   postFile(url, fetchOptions);

//   event.preventDefault();
// })

const myForm = document.getElementById("myForm");
const inpFile = document.getElementById("inpFile");

myForm.addEventListener('submit', handleSubmit);

/** @param {Event} event */
function handleSubmit(event) {
  event.preventDefault();

  /**@type {HTMLFormElement} */
  const form = event.currentTarget;
  const url = new URL(form.action);
  let formData = new FormData(form);

  /**@type {Parametrs<fetch>[1]} */
  const fetchOptions = {
    method: form.method,
    body: formData
  }
  
  console.log(fetchOptions);
  postFile(url, fetchOptions);
}


// /** @param {Event} event */
// function handleSubmit(event) {
//     const url = new URL(form.action);
//     const formData = new FormData(form);
  
//     /** @type {Parameters<fetch>[1]} */
//     const fetchOptions = {
//       method: form.method,
//       body: formData,
//     };
//     console.log(fetchOptions);
//     // postData(url, formData)
//     fetch(url, fetchOptions);
  
//     event.preventDefault();
// }
