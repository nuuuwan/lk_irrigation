# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_01:11:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,713 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 01:11:33 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | -0.018 |  |
| 2026-06-14 01:07:24 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-14 01:06:54 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:06:25 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:05:58 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | -0.030 |  |
| 2026-06-14 01:05:55 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:05:42 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:05:36 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.038 |  |
| 2026-06-14 01:05:23 | Rathnapura (Kalu Ganga) | 4.42 | 🟢 Normal | -0.090 |  |
| 2026-06-14 01:04:32 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.110 |  |
| 2026-06-14 01:04:31 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.041 |  |
| 2026-06-14 01:04:30 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | -0.010 |  |
| 2026-06-14 01:04:23 | Giriulla (Maha Oya) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-06-14 01:04:11 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | -0.010 |  |
| 2026-06-14 01:03:54 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:03:42 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | -0.011 |  |
| 2026-06-14 01:03:27 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-06-14 01:03:09 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.030 |  |
| 2026-06-14 01:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-06-14 01:02:37 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:02:07 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-14 01:01:43 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:01:33 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:01:28 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:01:13 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-14 01:01:00 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-14 01:00:46 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-06-14 00:48:12 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.110 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 01:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | -0.010 |  |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-14 01:07:24 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-14 01:01:00 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-14 00:14:18 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-14 01:01:13 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-14 00:09:08 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:01:43 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:01:28 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:03:09 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:02:37 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:06:25 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:03:54 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:05:55 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:06:54 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:01:33 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:50 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:04:30 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:05:42 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:25:26 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:27 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:03:19 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-14 01:02:07 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-14 01:04:11 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | -0.010 |  |
| 2026-06-14 01:00:46 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-06-14 01:03:42 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | -0.011 |  |
| 2026-06-14 01:11:33 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | -0.018 |  |
| 2026-06-14 01:04:23 | Giriulla (Maha Oya) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-06-14 01:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-06-13 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.021 |  |
| 2026-06-14 01:05:58 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | -0.030 |  |
| 2026-06-14 01:03:09 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.030 |  |
| 2026-06-14 01:03:27 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-06-14 00:03:04 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.036 |  |
| 2026-06-14 01:05:36 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.038 |  |
| 2026-06-13 18:05:47 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-14 01:04:31 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.041 |  |
| 2026-06-14 01:05:23 | Rathnapura (Kalu Ganga) | 4.42 | 🟢 Normal | -0.090 |  |
| 2026-06-14 01:04:32 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)