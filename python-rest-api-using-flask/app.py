from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."}
]

# GET request to fetch all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# GET request to fetch a single post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return jsonify({"message": "Post not found"}), 404
    return jsonify(post)

# POST request to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    new_post['id'] = len(posts) + 1
    posts.append(new_post)
    return jsonify(new_post), 201

# PUT request to update an existing post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return jsonify({"message": "Post not found"}), 404

    data = request.get_json()
    post.update(data)
    return jsonify(post)

# DELETE request to delete a post by ID
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return jsonify({"message": "Post deleted"})

if __name__ == '__main__':
    app.run(debug=True)
