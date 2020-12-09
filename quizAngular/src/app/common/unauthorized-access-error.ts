import { AppError } from './app-error';

export class UnauthorizedAcessError extends AppError {
    constructor(error: Response) {
        super(error);
        this.newMethod();
        console.log("i was here");
        
    }

    private newMethod() {
        localStorage.removeItem('token');
        localStorage.removeItem('expiry');
        localStorage.removeItem('user');
    }
}