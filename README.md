# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_19:15:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,003 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 19:15:10 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.018 |  |
| 2026-05-22 19:12:24 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-22 19:08:27 | Badalgama (Maha Oya) | 3.83 | 🟢 Normal | -0.018 |  |
| 2026-05-22 19:08:23 | Hanwella (Kelani Ganga) | 8.09 | 🟠 Minor Flood | -0.027 |  |
| 2026-05-22 19:06:12 | Nagalagam Street (Kelani Ganga) | 1.49 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-05-22 19:06:08 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:05:41 | Glencourse (Kelani Ganga) | 14.93 | 🟢 Normal | -0.166 |  |
| 2026-05-22 19:05:26 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-05-22 19:05:25 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-05-22 19:05:19 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-22 19:05:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-05-22 19:05:11 | Giriulla (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-05-22 19:05:10 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-22 19:04:57 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-22 19:04:25 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:04:11 | Magura (Kalu Ganga) | 4.35 | 🟡 Alert | -0.030 |  |
| 2026-05-22 19:04:09 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:03:52 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.061 |  |
| 2026-05-22 19:03:49 | Rathnapura (Kalu Ganga) | 7.40 | 🟡 Alert | -0.105 |  |
| 2026-05-22 19:03:48 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-22 19:03:35 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-22 19:03:20 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:03:18 | Ellagawa (Kalu Ganga) | 9.48 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-22 19:03:08 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.070 |  |
| 2026-05-22 19:02:45 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:02:43 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-22 19:02:28 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:02:09 | Dunamale (Aththanagalu Oya) | 5.14 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-22 19:01:50 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 19:01:43 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-22 19:01:16 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-22 19:01:04 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-05-22 19:00:31 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:00:10 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 19:02:09 | Dunamale (Aththanagalu Oya) | 5.14 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-22 19:08:23 | Hanwella (Kelani Ganga) | 8.09 | 🟠 Minor Flood | -0.027 |  |
| 2026-05-22 19:05:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-05-22 19:06:12 | Nagalagam Street (Kelani Ganga) | 1.49 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-05-22 19:04:11 | Magura (Kalu Ganga) | 4.35 | 🟡 Alert | -0.030 |  |
| 2026-05-22 19:03:49 | Rathnapura (Kalu Ganga) | 7.40 | 🟡 Alert | -0.105 |  |
| 2026-05-22 19:03:18 | Ellagawa (Kalu Ganga) | 9.48 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-22 19:04:57 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-22 19:03:35 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-22 19:01:43 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-22 19:02:43 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-22 19:05:19 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-22 19:05:10 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-22 19:01:50 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 19:12:24 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-22 19:00:10 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:01:16 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:04:09 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:05:19 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:00:31 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:06:08 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:03:20 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:02:28 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:04:25 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:02:45 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-22 19:05:11 | Giriulla (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-05-22 19:01:04 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-05-22 19:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-22 19:03:48 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-22 19:05:25 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-05-22 19:05:26 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-05-22 19:15:10 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.018 |  |
| 2026-05-22 19:08:27 | Badalgama (Maha Oya) | 3.83 | 🟢 Normal | -0.018 |  |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-22 19:03:52 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.061 |  |
| 2026-05-22 19:03:08 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.070 |  |
| 2026-05-22 19:05:41 | Glencourse (Kelani Ganga) | 14.93 | 🟢 Normal | -0.166 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)