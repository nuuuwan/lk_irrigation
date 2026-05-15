# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_11:14:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,441 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **47** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 11:14:41 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.097 |  |
| 2026-05-15 11:12:50 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:10:52 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:09:57 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-15 11:09:52 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.047 |  |
| 2026-05-15 11:08:58 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-15 11:08:45 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:08:09 | Baddegama (Gin Ganga) | 3.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 11:07:56 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:07:53 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-05-15 11:07:24 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-15 11:06:10 | Rathnapura (Kalu Ganga) | 4.62 | 🟢 Normal | -0.039 |  |
| 2026-05-15 11:05:47 | Glencourse (Kelani Ganga) | 12.81 | 🟢 Normal | -0.204 |  |
| 2026-05-15 11:05:47 | Moragaswewa (Deduru Oya) | 3.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-15 11:05:45 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-05-15 11:05:43 | Katharagama (Menik Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:05:39 | Dunamale (Aththanagalu Oya) | 4.73 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-05-15 11:04:55 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.039 |  |
| 2026-05-15 11:04:41 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-05-15 11:04:27 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-15 11:04:14 | Badalgama (Maha Oya) | 4.50 | 🟢 Normal | -0.072 |  |
| 2026-05-15 11:03:39 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | -0.054 |  |
| 2026-05-15 11:03:34 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:03:31 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.049 |  |
| 2026-05-15 11:03:28 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-05-15 11:03:21 | Galgamuwa (Mee Oya) | 3.68 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-05-15 11:03:12 | Putupaula (Kalu Ganga) | 2.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 11:03:02 | Hanwella (Kelani Ganga) | 5.95 | 🟢 Normal | -0.090 |  |
| 2026-05-15 11:02:30 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 11:02:24 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:02:17 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-05-15 11:02:08 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:02:03 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:01:52 | Giriulla (Maha Oya) | 3.38 | 🟢 Normal | -0.056 |  |
| 2026-05-15 11:01:49 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 11:01:47 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.032 |  |
| 2026-05-15 11:01:02 | Thanthirimale (Malwathu Oya) | 4.02 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-15 11:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.034 |  |
| 2026-05-15 11:00:17 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.020 |  |
| 2026-05-15 10:31:11 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.097 |  |
| 2026-05-15 10:29:46 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-15 10:29:19 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-15 10:28:47 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-15 10:28:05 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-15 10:27:58 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-15 10:27:53 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 11:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-15 11:05:39 | Dunamale (Aththanagalu Oya) | 4.73 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-05-15 11:03:39 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | -0.054 |  |
| 2026-05-15 11:03:21 | Galgamuwa (Mee Oya) | 3.68 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-05-15 11:04:41 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-05-15 11:01:02 | Thanthirimale (Malwathu Oya) | 4.02 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-15 11:05:47 | Moragaswewa (Deduru Oya) | 3.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-15 11:03:12 | Putupaula (Kalu Ganga) | 2.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 11:02:30 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 11:01:49 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 11:08:09 | Baddegama (Gin Ganga) | 3.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 11:09:57 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-15 11:08:58 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-15 11:02:24 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:07:56 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:08:45 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:02:08 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:03:34 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:05:43 | Katharagama (Menik Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:10:52 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:12:50 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:02:03 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-15 11:05:45 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-05-15 11:04:27 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-15 11:03:28 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-05-15 11:00:17 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.020 |  |
| 2026-05-15 11:02:17 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-05-15 11:07:53 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-05-15 11:01:47 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.032 |  |
| 2026-05-15 11:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.034 |  |
| 2026-05-15 11:06:10 | Rathnapura (Kalu Ganga) | 4.62 | 🟢 Normal | -0.039 |  |
| 2026-05-15 11:04:55 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.039 |  |
| 2026-05-15 11:09:52 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.047 |  |
| 2026-05-15 11:03:31 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.049 |  |
| 2026-05-15 11:01:52 | Giriulla (Maha Oya) | 3.38 | 🟢 Normal | -0.056 |  |
| 2026-05-15 11:04:14 | Badalgama (Maha Oya) | 4.50 | 🟢 Normal | -0.072 |  |
| 2026-05-15 11:03:02 | Hanwella (Kelani Ganga) | 5.95 | 🟢 Normal | -0.090 |  |
| 2026-05-15 11:14:41 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.097 |  |
| 2026-05-15 11:05:47 | Glencourse (Kelani Ganga) | 12.81 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)