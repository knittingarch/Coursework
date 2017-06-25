import React from 'react';
import Fish from './Fish';
import Header from './Header';
import Inventory from './Inventory';
import Order from './Order';
import sampleFishes from '../sample-fishes';
// where did the name sampleFishes come from???

class App extends React.Component {
	constructor() {
		super();
		this.addFish = this.addFish.bind(this);
		this.loadSamples = this.loadSamples.bind(this);
		this.addToOrder = this.addToOrder.bind(this);
		// initial state
		this.state = {
			fishes: {},
			order: {},
		};
	}
	// the param being passed in is the object being created in AddFishForm
	addFish(fish) {
		// make a copy of the current state
		// performance-taxing way: this.state.fishes.fish1 = fish;
		const fishes = {...this.state.fishes};
		// add a new fish
		const timestamp = Date.now();
		fishes[`fish-${timestamp}`] = fish;
		// set or update the state
		// first "fishes" is the state, second "fishes" is the object
		this.setState({
			fishes: fishes
		});
	}

	loadSamples() {
		this.setState({
			fishes: sampleFishes
		});
	}

	addToOrder(key) {
		// get a copy of the stats
		const order = {...this.state.order};
		// update or add new number of fish ordered
		order[key] = order[key] + 1 || 1;
		// update the state
		this.setState({
			order: order
		});
	}

	render() {
		return (
			<div className="catch-of-the-day">
				<div className="menu">
					<Header tagline="Fresh Seafood Market" />
					<ul className="list-of-fishes">
						{
							Object
							.keys(this.state.fishes)
							.map(key => <Fish key={key} id={key} details={this.state.fishes[key]} addToOrder={this.addToOrder} />)
						}
					</ul>
				</div>
				<Order fishes={this.state.fishes} order={this.state.order} />
				<Inventory addFish={this.addFish} loadSamples={this.loadSamples} />
			</div>
		)
	}
}

export default App;