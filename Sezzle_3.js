// like | Dislike - Passed 100% TC

import cx from 'classnames'
import React, { Component } from 'react'

const init = {
    like: 100,
    dislike: 25,
    liked: false,
    disliked: false
}
export default class LikeDislike extends Component {

    constructor(props) {
        super(props)
        this.state = init
    }

    handleLike() {

        this.setState((prev) => ({
            ...init,
            like: prev.liked ? prev.like - 1 : prev.like + 1,
            liked: !prev.liked
        }))
    }

    handleDislike() {
        this.setState((prev) = > ({
            ...init,
            dislike: prev.disliked ? prev.dislike - 1 : prev.dislike + 1,
            disliked: !prev.disliked
        }))
    }

    render() {
        return (
            <>
                <div >
                    < h2 > Like/Dislike </h2 >
                    < button className={`like-button ${this.state.liked && "liked"}`} onClick={() => {
                        this.handleLike()
                    }} > Like | <span className="likes-counter" > {this.state.like} </span > </button >
                    < button className={`dislike-button ${this.state.disliked && "disliked"}`} onClick={() => {
                        this.handleDislike()
                    }}
                    > Dislike | <span className="dislikes-counter" > {this.state.dislike} </span> </button >
                </div >
                <style>
                    {`
                       .like-button, .dislike-button {
                           font-size: 1rem
                           padding: 5px 10px
                           color: # 585858;
                       }

                       .liked, .disliked {
                           font-weight: bold
                           color:  # 1565c0;
                       }
                        `} </style>
            </>
        )
    }
}
