from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

blogs = [
    {"id": 1, "title": "Post 1", "content": "This is the first post Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eros libero, placerat quis diam ac, semper finibus massa. Phasellus placerat mi eget libero bibendum scelerisque. Donec sed ultricies eros, vitae rutrum elit. Phasellus at enim nibh. Quisque egestas, sem nec malesuada lacinia, dolor magna convallis justo, at auctor lectus leo ut odio. Morbi sed risus lacinia, blandit elit vitae, aliquet ante. Nulla in lobortis risus. Phasellus dictum egestas tellus ut fringilla. Mauris efficitur porta dolor ut malesuada. Morbi consequat ex et ipsum scelerisque sollicitudin. Phasellus nisi augue, commodo eget nulla vel, consequat tristique lacus. Suspendisse lacus nunc, bibendum eu laoreet et, bibendum a nisi. Nullam id molestie risus, facilisis lobortis turpis.Aenean molestie elementum rutrum. Phasellus vel ante orci. Nunc fermentum eget erat vel lacinia. Proin luctus lacus nec tempor scelerisque. Mauris fringilla congue libero eu elementum. Sed laoreet, diam et pellentesque molestie, diam nulla ultrices sapien, at sodales ex augue a metus. Aenean ac enim lobortis, pretium sem sed, dignissim quam. Vestibulum lobortis fermentum tortor, ut gravida magna iaculis ac. Cras ut iaculis risus, et iaculis diam. Cras eget ipsum ut lectus blandit fermentum. Quisque at leo pellentesque, ultricies dui at, semper nulla. Phasellus interdum nisl ut nibh imperdiet interdum. Nunc rutrum ex at gravida semper."},
    {"id": 2, "title": "Post 2", "content": "This is the second post.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eros libero, placerat quis diam ac, semper finibus massa. Phasellus placerat mi eget libero bibendum scelerisque. Donec sed ultricies eros, vitae rutrum elit. Phasellus at enim nibh. Quisque egestas, sem nec malesuada lacinia, dolor magna convallis justo, at auctor lectus leo ut odio. Morbi sed risus lacinia, blandit elit vitae, aliquet ante. Nulla in lobortis risus. Phasellus dictum egestas tellus ut fringilla. Mauris efficitur porta dolor ut malesuada. Morbi consequat ex et ipsum scelerisque sollicitudin. Phasellus nisi augue, commodo eget nulla vel, consequat tristique lacus. Suspendisse lacus nunc, bibendum eu laoreet et, bibendum a nisi. Nullam id molestie risus, facilisis lobortis turpis.Aenean molestie elementum rutrum. Phasellus vel ante orci. Nunc fermentum eget erat vel lacinia. Proin luctus lacus nec tempor scelerisque. Mauris fringilla congue libero eu elementum. Sed laoreet, diam et pellentesque molestie, diam nulla ultrices sapien, at sodales ex augue a metus. Aenean ac enim lobortis, pretium sem sed, dignissim quam. Vestibulum lobortis fermentum tortor, ut gravida magna iaculis ac. Cras ut iaculis risus, et iaculis diam. Cras eget ipsum ut lectus blandit fermentum. Quisque at leo pellentesque, ultricies dui at, semper nulla. Phasellus interdum nisl ut nibh imperdiet interdum. Nunc rutrum ex at gravida semper."},
    {"id": 3, "title": "Post 3", "content": "This is the first post Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eros libero, placerat quis diam ac, semper finibus massa. Phasellus placerat mi eget libero bibendum scelerisque. Donec sed ultricies eros, vitae rutrum elit. Phasellus at enim nibh. Quisque egestas, sem nec malesuada lacinia, dolor magna convallis justo, at auctor lectus leo ut odio. Morbi sed risus lacinia, blandit elit vitae, aliquet ante. Nulla in lobortis risus. Phasellus dictum egestas tellus ut fringilla. Mauris efficitur porta dolor ut malesuada. Morbi consequat ex et ipsum scelerisque sollicitudin. Phasellus nisi augue, commodo eget nulla vel, consequat tristique lacus. Suspendisse lacus nunc, bibendum eu laoreet et, bibendum a nisi. Nullam id molestie risus, facilisis lobortis turpis.Aenean molestie elementum rutrum. Phasellus vel ante orci. Nunc fermentum eget erat vel lacinia. Proin luctus lacus nec tempor scelerisque. Mauris fringilla congue libero eu elementum. Sed laoreet, diam et pellentesque molestie, diam nulla ultrices sapien, at sodales ex augue a metus. Aenean ac enim lobortis, pretium sem sed, dignissim quam. Vestibulum lobortis fermentum tortor, ut gravida magna iaculis ac. Cras ut iaculis risus, et iaculis diam. Cras eget ipsum ut lectus blandit fermentum. Quisque at leo pellentesque, ultricies dui at, semper nulla. Phasellus interdum nisl ut nibh imperdiet interdum. Nunc rutrum ex at gravida semper."},
    {"id": 4, "title": "Post 4", "content": "This is the second post.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eros libero, placerat quis diam ac, semper finibus massa. Phasellus placerat mi eget libero bibendum scelerisque. Donec sed ultricies eros, vitae rutrum elit. Phasellus at enim nibh. Quisque egestas, sem nec malesuada lacinia, dolor magna convallis justo, at auctor lectus leo ut odio. Morbi sed risus lacinia, blandit elit vitae, aliquet ante. Nulla in lobortis risus. Phasellus dictum egestas tellus ut fringilla. Mauris efficitur porta dolor ut malesuada. Morbi consequat ex et ipsum scelerisque sollicitudin. Phasellus nisi augue, commodo eget nulla vel, consequat tristique lacus. Suspendisse lacus nunc, bibendum eu laoreet et, bibendum a nisi. Nullam id molestie risus, facilisis lobortis turpis.Aenean molestie elementum rutrum. Phasellus vel ante orci. Nunc fermentum eget erat vel lacinia. Proin luctus lacus nec tempor scelerisque. Mauris fringilla congue libero eu elementum. Sed laoreet, diam et pellentesque molestie, diam nulla ultrices sapien, at sodales ex augue a metus. Aenean ac enim lobortis, pretium sem sed, dignissim quam. Vestibulum lobortis fermentum tortor, ut gravida magna iaculis ac. Cras ut iaculis risus, et iaculis diam. Cras eget ipsum ut lectus blandit fermentum. Quisque at leo pellentesque, ultricies dui at, semper nulla. Phasellus interdum nisl ut nibh imperdiet interdum. Nunc rutrum ex at gravida semper."},
]

@app.route('/')
def homePage():
    return render_template('index.html', posts=blogs)

@app.route('/post/<int:post_id>')
def display_post(post_id):
    post = next((p for p in blogs if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404

@app.route('/create_post', methods=['POST'])
def new_post():
    if request.method == 'POST':
        new_post = {
            "id": len(blogs) + 1,
            "title": request.form['title'],
            "content": request.form['content']
        }
        blogs.append(new_post)
        return render_template('post.html', post=new_post)

@app.route('/all/posts', methods=['GET'])
def get_posts_json():
    return jsonify(blogs)

if __name__ == '__main__':
    app.run(port=5000,debug=True)