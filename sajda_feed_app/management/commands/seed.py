from django.core.management.base import BaseCommand
from sajda_feed_app.models import *
import random
import datetime
from django.contrib.auth.models import User

class Command(BaseCommand):
	help = 'seeding database'

	def handle(self,*args, **kwargs):
		seed_data()

def seed_data():
    print('Generating admin user')
    print('username: admin, password: 1234')

    user = User.objects.create_user('admin', password='1234')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    print('Create CustomUser for access_token')

    CustomUser.objects.create(user=user, access_token='some-random-access-token')

    print('Generating Quran cards')

    for i in range(5):
        QuranCard.objects.create(
            title=f'Surah number { i }', 
            ayah_number=f'{i}', 
            description='Very meaningful surah and beautiful meaning',
            arabic_text='رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِن لَّدُنكَ رَحْمَةً ۚ إِنَّكَ أَنتَ ٱلْوَهَّابُ ٨',
            )

    print('Generating Hadith cards')

    for i in range(5):
        HadithCard.objects.create(
            title=f'Hadith number { i }',
            hadith_text='حَدَّثَنَا عَبْدُ اللَّهِ بْنُ عَبْدِ الرَّحْمَنِ، أَخْبَرَنَا عُمَرُ بْنُ حَفْصِ بْنِ غِيَاثٍ، حَدَّثَنَا أَبِي، عَنِ الْعَلاَءِ بْنِ خَالِدٍ الْكَاهِلِيِّ، عَنْ شَقِيقِ بْنِ سَلَمَةَ، عَنْ عَبْدِ اللَّهِ بْنِ مَسْعُودٍ، قَالَ قَالَ رَسُولُ اللَّهِ صلى الله عليه وسلم ‏ "‏ يُؤْتَى بِجَهَنَّمَ يَوْمَئِذٍ لَهَا سَبْعُونَ أَلْفَ زِمَامٍ مَعَ كُلِّ زِمَامٍ سَبْعُونَ أَلْفَ مَلَكٍ يَجُرُّونَهَا ‏"‏ ‏.‏ قَالَ عَبْدُ اللَّهِ بْنُ عَبْدِ الرَّحْمَنِ وَالثَّوْرِيُّ لاَ يَرْفَعُهُ',
            narrator='Abu Hurairah r.a',
            description='Hell will be brought forth on that Day (of Resurrection) having seventy thousand bridles, and with every handle will be seventy thousand angels dragging it',
            )

    print('Generating Dhikr cards')
    
    # Define start and end dates for the range
    s_date = datetime.datetime(2022, 1, 1)
    e_date = datetime.datetime(2022, 12, 31)

    # Generate a random date within the specified range
    r_date = s_date + datetime.timedelta(days=random.randint(0, (e_date - s_date).days))


    for i in range(5):
        DhikrCard.objects.create(
            title=f'Dhikr against evil number { i }',
            description='Allahumma salli ghala seidina Muhammad!',
            user_progress=random.randint(1,100),
            last_read_date=r_date,
        )

    print('Generating YouTubeCard cards')
    
    for i in range(5):
    	YouTubeCard.objects.create(
    		title='Awe some lecture about Quran',
    		description='Nouman Ali Khan give in depth knowledge about some ayah!',
    		video_id='Y8kCy2ktANA?si=UqKqfhmAAosGuLj2',
    		in_app=True,
    		)


