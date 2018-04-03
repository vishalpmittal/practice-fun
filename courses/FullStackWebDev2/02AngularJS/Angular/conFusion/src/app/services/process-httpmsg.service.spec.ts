import { TestBed, inject } from '@angular/core/testing';

import { processHTTPMsgService } from './process-httpmsg.service';

describe('processHTTPMsgService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [processHTTPMsgService]
    });
  });

  it('should be created', inject([processHTTPMsgService], (service: processHTTPMsgService) => {
    expect(service).toBeTruthy();
  }));
});
