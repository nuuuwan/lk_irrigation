# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_22:16:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,447 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 22:16:28 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.016 |  |
| 2026-05-09 22:15:42 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.106 |  |
| 2026-05-09 22:11:58 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:10:32 | Katharagama (Menik Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-05-09 22:09:50 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-05-09 22:09:22 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 22:07:42 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-09 22:07:32 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-05-09 22:06:28 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.092 |  |
| 2026-05-09 22:05:39 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:05:27 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.040 |  |
| 2026-05-09 22:05:20 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-05-09 22:05:17 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.079 |  |
| 2026-05-09 22:04:34 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:04:12 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-09 22:04:11 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:04:02 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.041 |  |
| 2026-05-09 22:03:33 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:03:30 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-05-09 22:03:10 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:03:10 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:03:08 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-05-09 22:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | -0.049 |  |
| 2026-05-09 22:02:35 | Kuda Oya (Kirindi Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:02:19 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:02:14 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:02:12 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-05-09 22:02:00 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:01:53 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:01:47 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:01:42 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:01:33 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.011 |  |
| 2026-05-09 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-05-09 22:01:10 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.070 |  |
| 2026-05-09 22:01:01 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:00:15 | Wellawaya (Kirindi Oya) | 3.62 | 🟢 Normal | 1.032 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 22:00:15 | Wellawaya (Kirindi Oya) | 3.62 | 🟢 Normal | 1.032 | 🔺 Rising |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-09 22:07:42 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-09 21:05:53 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-09 22:04:12 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-09 22:09:22 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 22:01:53 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:03:10 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:01:47 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:01:01 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:02:00 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:04:34 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:03:33 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:11:58 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:04:11 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:02:14 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:09:50 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-05-09 22:07:32 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-05-09 22:02:35 | Kuda Oya (Kirindi Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:03:10 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:01:42 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:05:39 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:01:33 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.011 |  |
| 2026-05-09 22:16:28 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.016 |  |
| 2026-05-09 22:03:30 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-05-09 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-05-09 22:02:12 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-05-09 22:10:32 | Katharagama (Menik Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-05-09 22:03:08 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-05-09 22:05:20 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-05-09 22:05:27 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.040 |  |
| 2026-05-09 22:04:02 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.041 |  |
| 2026-05-09 22:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | -0.049 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-09 22:01:10 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.070 |  |
| 2026-05-09 22:05:17 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.079 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-09 22:06:28 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.092 |  |
| 2026-05-09 22:15:42 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)