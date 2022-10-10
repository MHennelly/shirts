const root = ReactDOM.createRoot(
  document.getElementById('try-container')
);

class TryHashing extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: '', hash: ''};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    let x = this.state.value;
    for (let i = 0; i < 100000; i++) {
      x = CryptoJS.SHA512(x).toString();
    }
    this.setState({hash: x})
    event.preventDefault();
  }

  render() {
    return (
      <div class="row justify-content-center">
        <form onSubmit={this.handleSubmit}>
          <div class="form-group row">
            <label class="col-2 col-form-label" for="passInput">Passphrase:</label>
            <div class="col-8">
              <input class="form-control" id="passInput" type="password" value={this.state.value} onChange={this.handleChange} />
            </div>
            <button class="btn btn-outline-dark col-2" type="submit">Submit</button>
          </div>
          <div class="form-group row">
            <label class="col-2 col-form-label" for="hashOutput">Hash:</label>
            <div class="col-10">
              <textarea id="hashOutput" type="text" readonly class="form-control-plaintext" rows="3" value={this.state.hash} />
            </div>
          </div>
        </form>
      </div>
    );
  }
}

const e = <TryHashing />;
root.render(e)
