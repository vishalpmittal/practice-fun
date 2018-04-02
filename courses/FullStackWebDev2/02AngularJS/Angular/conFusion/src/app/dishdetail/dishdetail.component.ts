import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormGroupDirective} from '@angular/forms';
import { Dish } from '../shared/dish';
import { Comment } from '../shared/comment'

import { DishService } from '../services/dish.service';

import { Params, ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'app-dishdetail',
  templateUrl: './dishdetail.component.html',
  styleUrls: ['./dishdetail.component.scss']
})

export class DishdetailComponent implements OnInit {

  ddForm: FormGroup;
  @ViewChild(FormGroupDirective) commentFormDirective;
  dish: Dish;
  dishIds: number[];
  prev: number;
  next: number;
  ddAuthorComment: Comment;

  ddFormErrors = {
    'author': '',
    'comment': ''
  };

  ddValidationMessages = {
    'author': {
      'required': 'Author Name is required.',
      'minlength': 'Author Name must be at least 2 characters long.'
    },
    'comment': {
      'required': 'Comment is required.'
    },
  };

  constructor(private dishservice: DishService,
    private route: ActivatedRoute,
    private location: Location,
    private ddfb: FormBuilder) {
      this.createForm();
    }

  ngOnInit() {
    this.dishservice.getDishIds().subscribe(dishIds => this.dishIds = dishIds);
    this.route.params
      .switchMap((params: Params) => this.dishservice.getDish(+params['id']))
      .subscribe(dish => { this.dish = dish; this.setPrevNext(dish.id); });
  }

  setPrevNext(dishId: number) {
    let index = this.dishIds.indexOf(dishId);
    this.prev = this.dishIds[(this.dishIds.length + index - 1)%this.dishIds.length];
    this.next = this.dishIds[(this.dishIds.length + index + 1)%this.dishIds.length];
  }

  goBack(): void {
    this.location.back();
  }

  createForm() {
    this.ddForm = this.ddfb.group({
      author: ['', [Validators.required, Validators.minLength(2)] ],
      comment: ['', [Validators.required] ],
      rating: 5,
      date: ''
    });

    this.ddForm.valueChanges.subscribe(data => this.onValueChanged(data));
    this.onValueChanged(); // (re)set validation messages now
  }

  ddCommentOnSubmit() {
    this.ddAuthorComment = this.ddForm.value;
    this.ddAuthorComment.date = (new Date()).toISOString();
    this.dish.comments.push(this.ddAuthorComment)
    this.ddForm.reset({
      author: '',
      comment: '',
      rating: 5,
      date: ''
    });

    this.commentFormDirective.resetForm();
  }

  onValueChanged(data?: any) {
    if (!this.ddForm) { return; }

    const form = this.ddForm;

    for (const field in this.ddFormErrors) {
      // clear previous error message (if any)
      this.ddFormErrors[field] = '';
      const control = form.get(field);

      if (control && control.dirty && !control.valid) {
        const messages = this.ddValidationMessages[field];

        for (const key in control.errors) {
          this.ddFormErrors[field] += messages[key] + ' ';
        }
      }
    }
  }

}
