@app.route('/')
def index():
  conn=get_db_connection()
  posts=conn.execute('SELECT * FROM posts').fetchall()
  conn.close()
  return render_template('index.html',posts=posts)



def get_post(post_id):
  conn=get_db_connection()
  post=conn.execute('SELECT * FROM posts WHERE id=?',
                    (post_id,)).fetchone()
  conn.close()
  if post is None:
    abort(404)
  return post

@app.route('/<int:post_id>')
def post(post_id):
  post=get_post(post_id)
  return render_template('post.html',post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method=='POST':
      title=request.form['title']
      content=request.form['content']

      if not title:
        flash('Title is required!')
      else:
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                      (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/create_1',methods=('GET','POST'))
def create_1():
  if request.method=='POST':
    peru=request.form['peru']
    addr=request.form['addr']
    phone=request.form['phone']

    if not peru:
      flash('Name is required!')
    elif not phone:
      flash('Phone number is required')
    elif not addr:
      flash('Address is required')
    else:
      conn=get_db_connection()
      conn.execute('INSERT INTO info (peru,phone,addr) VALUES (?,?,?)',
                   (peru,phone,addr))
      conn.commit()
      conn.close()
      return redirect(url_for('index'))
  
  return render_template('create_1.html')


@app.route('/infolist')
def infolist():
  conn=get_db_connection()
  infos=conn.execute('SELECT * FROM info').fetchall()
  conn.close()
  return render_template('info.html',infos=infos)
