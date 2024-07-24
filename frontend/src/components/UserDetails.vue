<template>
    <div v-if="user" class="user-details">
      <img :src="userPicture" alt="Chef Picture" />
      <h1>{{ user.name }}</h1>
      <p><strong>Chef at </strong> {{ user.company }}</p>
      <p><strong>Biography:</strong> {{ user.biography }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Phone Number:</strong> {{ user.phonenumber }}</p>
      <p><strong>Tone:</strong> {{ user.tone }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        user: null,
        userPicture: '' 
      };
    },
    created() {
      this.createUser();
      this.selectRandomPicture();
    },
    methods: {
        selectRandomPicture() {
            const pictures = ['/chef.webp', '/sanji.webp'];
            const randomIndex = Math.floor(Math.random() * pictures.length);
            this.userPicture = pictures[randomIndex];
        },

        async createUser() {
        try {
          let response;
          do {
            response = await fetch('http://127.0.0.1:8000/user', { method: 'POST' });
          } while (!response.ok);
  
          const data = await response.json();
          const userId = data.userId;
          console.log('User created with ID:', userId);  
          this.fetchUser(userId);
        } catch (error) {
          console.error('Failed to create user:', error);
        }
      },
      async fetchUser(userId) {
        try {
          const response = await fetch(`http://127.0.0.1:8000/user/${userId}`);
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          const user = await response.json();
          console.log('User data fetched:', user);  
          this.user = user;
        } catch (error) {
          console.error('Failed to fetch user:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
    .user-details {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    margin: 40px auto;
    }

    .user-details h1 {
    font-size: 2.5em;
    margin: 20px 0;
    color: #333;
    }

    .user-details p {
    font-size: 1.2em;
    color: #555;
    margin: 10px 0;
    }

    .user-details img {
    border-radius: 50%;
    width: 250px;
    height: 250px;
    margin-bottom: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    p {
    font-size: 18px;
    }

    p strong {
    color: #333;
    }

    p::after {
    content: "";
    display: block;
    margin: 10px auto;
    width: 40%;
    height: 2px;
    background-color: #ddd;
    }
    </style>

  