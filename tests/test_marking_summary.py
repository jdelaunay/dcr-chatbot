import unittest

from dcrai.chat.faq_runtime import marking_summary


class MarkingSummaryTests(unittest.TestCase):
    def test_lists_ids_by_state_without_values_or_effect_parameters(self):
        payload = {'events': [
            {'id': 'FAQ_Retrieve', 'included': True, 'enabled': True, 'pending': False, 'executed': '2026-01-01',
             'value': 'secret-value', 'eventType': {'Parameters': {'header#X-API-Key': '"secret-key"'}}},
            {'id': 'Outcome_Answer', 'included': True, 'enabled': True, 'pending': True, 'executed': None,
             'description': 'applicant answer text'},
            {'id': 'Hidden', 'included': False, 'enabled': False, 'pending': True, 'executed': None},
        ]}
        text = marking_summary(payload)
        self.assertEqual(text, "pending=['Outcome_Answer'] enabled=2/3 executed=['FAQ_Retrieve']")
        for leaked in ('secret', 'applicant'):
            self.assertNotIn(leaked, text)

    def test_unreadable_payload(self):
        for payload in (None, {}, {'events': 'x'}, 'text'):
            self.assertEqual(marking_summary(payload), 'unavailable')


if __name__ == '__main__':
    unittest.main()
