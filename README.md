
This project is a simple microblog application built with Flask and MongoDB. 
It allows users to post entries, view posts by date, and filter posts using a calendar interface. 
The application uses environment variables to connect to the MongoDB database and includes basic functionality to post, view, and filter entries.

## Features
- **Post Entries**: Users can submit posts that are stored in MongoDB.
- **View Posts**: All posts are displayed on the homepage with their respective dates.
- **Date Filtering**: Users can select a date from the calendar to view posts from that specific day.
- **MongoDB Integration**: Posts are stored in a MongoDB database.
- **Environment Variables**: The application uses a `.env` file to store sensitive information like the MongoDB connection URI.

## Technologies
- **Flask**: Python web framework used to build the application.
- **MongoDB**: NoSQL database used for storing posts.
- **HTML/CSS**: Frontend used to display posts and calendar.
- **dotenv**: Loads environment variables from the `.env` file.

