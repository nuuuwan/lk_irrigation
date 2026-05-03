# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_18:02:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,971 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 18:02:57 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:43 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:02:27 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:26 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:02:22 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:06 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:50 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:44 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 18:01:38 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-05-03 18:01:37 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:01:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:28 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:27 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.034 |  |
| 2026-05-03 18:01:26 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.040 |  |
| 2026-05-03 18:01:03 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:47 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:33 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:14 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 17:15:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:15:27 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.032 |  |
| 2026-05-03 17:13:30 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.042 |  |
| 2026-05-03 17:11:24 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:10:36 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 18:01:38 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-05-03 17:05:22 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-03 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 18:01:44 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 18:02:43 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:06 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:47 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:57 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:15:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:28 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:05:29 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:04:36 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:02:14 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:03 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:22 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:11:24 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:14 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:27 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:50 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:05:18 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:04:18 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:01:25 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-05-03 18:01:37 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-05-03 17:09:02 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:02:26 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-03 16:02:50 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-05-03 17:15:27 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.032 |  |
| 2026-05-03 18:01:27 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.034 |  |
| 2026-05-03 17:06:56 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.034 |  |
| 2026-05-03 18:01:26 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.040 |  |
| 2026-05-03 17:01:38 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.041 |  |
| 2026-05-03 17:13:30 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.042 |  |
| 2026-05-03 17:04:17 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.044 |  |
| 2026-05-03 17:02:44 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.059 |  |
| 2026-05-03 17:03:00 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)