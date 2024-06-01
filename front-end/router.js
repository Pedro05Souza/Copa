// Routes variables
const userCreationEndpoint = 'http://127.0.0.1:8000/user/store/';
const showAllUsersEndpoint = 'http://127.0.0.1:8000/users/';
const updateUserEndpoint = 'http://127.0.0.1:8000/user/update/';
const deleteUserEndpoint = 'http://127.0.0.1:8000/user/delete/';
const getUserUsernameEndpoint =  'http://127.0.0.1:8000/user/{username}';

function postRequest(data, route){
    fetch(`${route}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: String(data.username),
            skill: String(data.skill),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        console.log(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function getRequest(route){
    fetch(`${route}`)
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        return data;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}



