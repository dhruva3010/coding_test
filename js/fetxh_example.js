const apiUrl = 'https://api.github.com/users/Bard'; // Free API example URL

fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log('Data received:', data);
    // Process the data here
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
