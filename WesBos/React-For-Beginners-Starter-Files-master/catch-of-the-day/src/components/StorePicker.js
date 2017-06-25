import React from 'react';
import { getFunName } from '../helpers';


class StorePicker extends React.Component {
	
	// How to get "this" bound to the main class
		// Option 1: When method is reused multiple times
			// constructor() {
			// 	super();
			// 	this.goToStore = this.goToStore.bind(this);
			// }
		// Option 2: When you only use method a small number of times
			// Add this.goToStore.bind(this) to your event (creates one function tied to the method)
			// As arrow event: (e) => this.goToStore(e) (creates multiple functions for each rendered component)

	goToStore(event) {
		event.preventDefault();
		console.log('You changed the URL');
		// First grab text from box
		const storeId = this.storeInput.value;
		console.log(`Going to ${storeId}`);
		// Second transition from / to /store/:storeId
		this.context.router.transitionTo(`/store/${storeId}`);
	}

	render() {
		// Any where else
		// onSubmit shortcut: (e) =>this.goToStore(e)
		return (
			<form className="store-selector" onSubmit={this.goToStore.bind(this)}>
				{ /* This is a comment within JSX */}
				<h2>Please Enter A Store</h2>
				<input type="text" required placeholder="Store Name" defaultValue={getFunName()} ref={(input) => { this.storeInput = input}} />
				<button type="submit">Visit Store</button>
			</form>
		)
	}
}

// Must surface the router from the parent 

StorePicker.contextTypes = {
	router: React.PropTypes.object
}

export default StorePicker;