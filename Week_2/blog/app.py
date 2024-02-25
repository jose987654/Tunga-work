from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for blog posts
blog_posts = [
    {"id": 1, "title": "Post 1", "content": "This is the first post Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eros libero, placerat quis diam ac, semper finibus massa. Phasellus placerat mi eget libero bibendum scelerisque. Donec sed ultricies eros, vitae rutrum elit. Phasellus at enim nibh. Quisque egestas, sem nec malesuada lacinia, dolor magna convallis justo, at auctor lectus leo ut odio. Morbi sed risus lacinia, blandit elit vitae, aliquet ante. Nulla in lobortis risus. Phasellus dictum egestas tellus ut fringilla. Mauris efficitur porta dolor ut malesuada. Morbi consequat ex et ipsum scelerisque sollicitudin. Phasellus nisi augue, commodo eget nulla vel, consequat tristique lacus. Suspendisse lacus nunc, bibendum eu laoreet et, bibendum a nisi. Nullam id molestie risus, facilisis lobortis turpis.Aenean molestie elementum rutrum. Phasellus vel ante orci. Nunc fermentum eget erat vel lacinia. Proin luctus lacus nec tempor scelerisque. Mauris fringilla congue libero eu elementum. Sed laoreet, diam et pellentesque molestie, diam nulla ultrices sapien, at sodales ex augue a metus. Aenean ac enim lobortis, pretium sem sed, dignissim quam. Vestibulum lobortis fermentum tortor, ut gravida magna iaculis ac. Cras ut iaculis risus, et iaculis diam. Cras eget ipsum ut lectus blandit fermentum. Quisque at leo pellentesque, ultricies dui at, semper nulla. Phasellus interdum nisl ut nibh imperdiet interdum. Nunc rutrum ex at gravida semper."},
    {"id": 2, "title": "Post 2", "content": "This is the second post.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eros libero, placerat quis diam ac, semper finibus massa. Phasellus placerat mi eget libero bibendum scelerisque. Donec sed ultricies eros, vitae rutrum elit. Phasellus at enim nibh. Quisque egestas, sem nec malesuada lacinia, dolor magna convallis justo, at auctor lectus leo ut odio. Morbi sed risus lacinia, blandit elit vitae, aliquet ante. Nulla in lobortis risus. Phasellus dictum egestas tellus ut fringilla. Mauris efficitur porta dolor ut malesuada. Morbi consequat ex et ipsum scelerisque sollicitudin. Phasellus nisi augue, commodo eget nulla vel, consequat tristique lacus. Suspendisse lacus nunc, bibendum eu laoreet et, bibendum a nisi. Nullam id molestie risus, facilisis lobortis turpis.Aenean molestie elementum rutrum. Phasellus vel ante orci. Nunc fermentum eget erat vel lacinia. Proin luctus lacus nec tempor scelerisque. Mauris fringilla congue libero eu elementum. Sed laoreet, diam et pellentesque molestie, diam nulla ultrices sapien, at sodales ex augue a metus. Aenean ac enim lobortis, pretium sem sed, dignissim quam. Vestibulum lobortis fermentum tortor, ut gravida magna iaculis ac. Cras ut iaculis risus, et iaculis diam. Cras eget ipsum ut lectus blandit fermentum. Quisque at leo pellentesque, ultricies dui at, semper nulla. Phasellus interdum nisl ut nibh imperdiet interdum. Nunc rutrum ex at gravida semper."},
]

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', posts=blog_posts)

# Route to display a specific blog post
@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404

# Route to handle form submission for creating a new post
@app.route('/create_post', methods=['POST'])
def create_post():
    if request.method == 'POST':
        new_post = {
            "id": len(blog_posts) + 1,
            "title": request.form['title'],
            "content": request.form['content']
        }
        blog_posts.append(new_post)
        return render_template('post.html', post=new_post)

# Route that returns JSON data
@app.route('/api/posts', methods=['GET'])
def get_posts_json():
    return jsonify(blog_posts)

if __name__ == '__main__':
    app.run(port=5000,debug=True)