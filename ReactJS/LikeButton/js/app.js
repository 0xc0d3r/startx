var LikeButton = React.createClass({
    getInitialState: function(){
      return {liked: false};
    },
    handleClick: function(){
      this.setState({liked : !this.state.liked});
    },
    render: function(){
      var text = this.state.liked ? 'like' : 'haven\'t liked';
      return (
        <div>
          <input type="button" onClick={this.handleClick} value={this.state.liked ? 'Unlike' : 'Like'} />
          &emsp;You {text} this.
        </div>
      );
    }
});

React.render(
  <LikeButton/>,
  document.getElementById('like')
);
