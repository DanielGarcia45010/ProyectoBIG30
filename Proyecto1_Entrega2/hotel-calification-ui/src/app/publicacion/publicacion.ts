export class Publicacion {
  id: number;
  username: string;
  classification: number;
  review: string;

  constructor(
    id: number,
    username: string,
    classification: number,
    review: string
  ){
    this.id = id;
    this.username = username;
    this.classification = classification;
    this.review = review;
  }
}
