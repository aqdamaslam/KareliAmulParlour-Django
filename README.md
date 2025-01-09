# Online Products Availability Application: Kareli Amul Parlour

## Overview

The "Kareli Amul Parlour" is an online product availability application designed to help customers easily browse and purchase products. It is hosted on AWS services and built using HTML, CSS, JavaScript, Django, and integrates with WhatsApp API for customer support. The application provides real-time product availability information, enabling customers to make informed purchasing decisions.

---

## Application Architecture

### 1. **Frontend Technologies:**
   - **HTML**: The structure of the application’s pages is created using HTML, providing an organized layout for product listings, categories, and product details.
   - **CSS**: The application’s appearance is styled with CSS to enhance user experience, offering a responsive design that works across multiple devices.
   - **JavaScript**: JavaScript is used to add interactivity to the application, such as dynamic product filtering, cart functionality, and form validation.

### 2. **Backend Technologies:**
   - **Django**: The backend of the application is powered by Django, a high-level Python web framework. It handles product data management, user authentication, database interactions, and communicates with the WhatsApp API.
   
### 3. **WhatsApp API Integration**:
   - The WhatsApp API is integrated into the application for customer support. Users can chat with the support team directly through WhatsApp, inquire about product availability, and resolve issues in real-time.

---

## Hosting on AWS Services

The application is hosted on AWS infrastructure, ensuring scalability, security, and reliability.

### 1. **Amazon EC2 (Elastic Compute Cloud)**:
   - The Django application runs on EC2 instances, which provide scalable compute capacity. EC2 ensures that the application can handle a high volume of traffic and scale based on demand.
   
### 2. **Amazon Route 53**:
   - **DNS Management**: Route 53 is used for DNS management, allowing the application to use custom domain names (`www.kareliamulparlour.com`) and route traffic efficiently.
   - **Health Checks**: Route 53 also monitors the health of the EC2 instances to ensure the application remains highly available.

### 3. **DNS Mapping**:
   - The DNS records of the application are managed using AWS Route 53, mapping domain names to the respective IP addresses of the EC2 instances hosting the Django app.

### 4. **DNS Registration**:
   - The custom domain name for the application is registered through AWS Route 53, ensuring reliable and cost-effective domain name registration and management.

---

## Application Features

### 1. **Product Listings**:
   - Users can browse various product categories available at the Amul parlour. Each product displays details such as price, availability, and description.
   
### 2. **Product Availability**:
   - The application allows customers to check real-time availability of products. The availability is updated automatically based on inventory levels maintained in the database.

### 3. **Search and Filter**:
   - A robust search functionality is included, allowing customers to search for products by name or category. Filtering options help users narrow down their search based on criteria like price, type, and brand.

### 4. **Customer Support via WhatsApp**:
   - A WhatsApp API button is embedded within the application, allowing users to connect with the support team instantly. Users can inquire about product availability, order status, and receive instant support.

---

## Technical Stack

### Frontend:
   - **HTML**: For structuring the webpage content.
   - **CSS**: For styling and ensuring a responsive design.
   - **JavaScript**: For adding interactivity to the frontend elements.
   
### Backend:
   - **Django**: For managing the backend logic, database models, and API integration (including WhatsApp API).
   
### AWS:
   - **EC2**: For hosting the application.
   - **Route 53**: For DNS management and domain registration.
   
### WhatsApp API:
   - **WhatsApp API**: For facilitating real-time customer support and communication.

---

