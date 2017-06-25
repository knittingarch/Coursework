import React from 'react';

class Order extends React.Component {
	render() {
		const orderIds = Object.keys(this.props.order);
		const total = orderIds.reduce() * 
		return (
			<div className="order-wrap">
				<h2>Your Order</h2>
				<h3>{this.props.fishes.name}</h3>
				<p>{this.props.fishes.price}</p>

			</div>
		)
	}
}

export default Order;