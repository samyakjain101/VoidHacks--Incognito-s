import { BadInput } from './../common/bad-input';
import { NotFoundError } from './../common/not-found-error';
import { AppError } from './../common/app-error';
import { HttpClient } from '@angular/common/http';
import { throwError } from 'rxjs';
import { catchError } from 'rxjs/operators'; 

export class DataService {

    constructor(private url: string , private http: HttpClient) { }

    private getHeader(params?: any) {
        let customHeaders = { Authorization: "Token " + localStorage.getItem("token") };
        return { headers: customHeaders, params: params };
    }

    getAll(params?: any) {
        return this.http.get(this.url, this.getHeader())
            .pipe( catchError(this.handleError) );
    }
    create(resource: any) {
        return this.http.post(this.url, resource, this.getHeader())
            .pipe(
                catchError(this.handleError)
            );
    }
    update(resource: any) {
        return this.http.patch(this.url + '/' + resource.id, { isRead: true })
            .pipe(
                catchError(this.handleError)
            )
    }
    delete(id: number) {
        return this.http.delete(this.url + '/' + id)
            .pipe(
                catchError(this.handleError)
            )
    }
    private handleError(error: Response) {
        if (error.status === 400)
            return throwError(new BadInput(error));
        if (error.status === 404)
            return throwError(new NotFoundError());
        return throwError(new AppError(error));
    }
}
