# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_21:14:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,013 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 21:14:16 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-13 21:12:59 | Panadugama (Nilwala Ganga) | 5.29 | 🟡 Alert | -0.027 |  |
| 2026-05-13 21:12:42 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:11:28 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:10:50 | Pitabeddara (Nilwala Ganga) | 1.74 | 🟢 Normal | -0.071 |  |
| 2026-05-13 21:10:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.027 |  |
| 2026-05-13 21:08:57 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-13 21:08:17 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:07:26 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.271 |  |
| 2026-05-13 21:06:16 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-13 21:06:08 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:06:08 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-13 21:05:51 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:05:39 | Putupaula (Kalu Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 21:04:21 | Moragaswewa (Deduru Oya) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-05-13 21:04:11 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.039 |  |
| 2026-05-13 21:04:08 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-05-13 21:04:04 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.080 |  |
| 2026-05-13 21:03:56 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-05-13 21:03:55 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.050 |  |
| 2026-05-13 21:03:48 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-05-13 21:03:14 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-13 21:03:03 | Giriulla (Maha Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 21:02:39 | Magura (Kalu Ganga) | 5.16 | 🟡 Alert | -0.010 |  |
| 2026-05-13 21:02:21 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-05-13 21:02:19 | Rathnapura (Kalu Ganga) | 5.86 | 🟡 Alert | -0.092 |  |
| 2026-05-13 21:02:19 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | -0.020 |  |
| 2026-05-13 21:02:11 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | -0.033 |  |
| 2026-05-13 21:02:09 | Moraketiya (Walawe Ganga) | 2.03 | 🟢 Normal | -0.039 |  |
| 2026-05-13 21:01:57 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:01:33 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:01:30 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-13 21:01:25 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:00:57 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 21:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.051 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 20:09:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.86 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-05-13 21:02:39 | Magura (Kalu Ganga) | 5.16 | 🟡 Alert | -0.010 |  |
| 2026-05-13 21:02:19 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | -0.020 |  |
| 2026-05-13 21:12:59 | Panadugama (Nilwala Ganga) | 5.29 | 🟡 Alert | -0.027 |  |
| 2026-05-13 21:02:19 | Rathnapura (Kalu Ganga) | 5.86 | 🟡 Alert | -0.092 |  |
| 2026-05-13 21:03:14 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-13 21:08:57 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-13 21:14:16 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-13 21:06:08 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-13 21:00:57 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 21:03:03 | Giriulla (Maha Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 21:05:39 | Putupaula (Kalu Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 21:01:57 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:11:28 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:01:25 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:01:33 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:05:51 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:12:42 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:08:17 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-13 21:04:21 | Moragaswewa (Deduru Oya) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-05-13 21:06:16 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-13 21:01:30 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-13 21:02:21 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-05-13 21:04:08 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-05-13 21:03:56 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-05-13 21:10:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.027 |  |
| 2026-05-13 21:03:48 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-05-13 21:02:11 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | -0.033 |  |
| 2026-05-13 21:04:11 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.039 |  |
| 2026-05-13 21:02:09 | Moraketiya (Walawe Ganga) | 2.03 | 🟢 Normal | -0.039 |  |
| 2026-05-13 21:03:55 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.050 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-13 21:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.051 |  |
| 2026-05-13 20:07:14 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.055 |  |
| 2026-05-13 21:10:50 | Pitabeddara (Nilwala Ganga) | 1.74 | 🟢 Normal | -0.071 |  |
| 2026-05-13 21:04:04 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.080 |  |
| 2026-05-13 21:07:26 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.271 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)