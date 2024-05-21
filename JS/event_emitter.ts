type Callback = (...args: any[]) => any;
type Subscription = {
    unsubscribe: () => void
}

class EventEmitter {
    private eventRecord: Record<string, Callback[]>

    constructor() {
        this.eventRecord = {}
    }
    
    subscribe(eventName: string, callback: Callback): Subscription {
        if (eventName in this.eventRecord) {
            this.eventRecord[eventName].push(callback)
        } else {
            this.eventRecord[eventName] = [callback]
        }
        return {
            unsubscribe: () => {
                const itemIndex = this.eventRecord[eventName].indexOf(callback)
                this.eventRecord[eventName].splice(itemIndex, 1)
            }
        };
    }
    
    emit(eventName: string, args: any[] = []): any[] {
        if (!(eventName in this.eventRecord)) {
            return []
        }
        const results = this.eventRecord[eventName].map((callback) => {
            return callback(...args)
        })
        return results
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */