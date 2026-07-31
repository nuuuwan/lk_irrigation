# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_00:11:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 00:11:57 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:11:56 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-01 00:11:13 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-01 00:10:37 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:10:19 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.018 |  |
| 2026-08-01 00:10:18 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-08-01 00:08:29 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-08-01 00:06:33 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 00:06:22 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 00:06:15 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-01 00:05:52 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-01 00:05:44 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-08-01 00:05:31 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 00:04:59 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:04:43 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 00:04:35 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.040 |  |
| 2026-08-01 00:04:05 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-01 00:03:45 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 00:03:43 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:03:29 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-08-01 00:03:14 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:03:02 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-01 00:02:56 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:02:49 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:02:34 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.012 |  |
| 2026-08-01 00:02:04 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:02:02 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:01:20 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:01:20 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.044 |  |
| 2026-08-01 00:00:44 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 23:30:27 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-31 23:25:28 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.221 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 00:03:29 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-08-01 00:08:29 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-08-01 00:10:18 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-08-01 00:03:02 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-01 00:06:15 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-31 23:08:09 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-01 00:11:13 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-01 00:04:43 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 00:06:33 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 00:03:45 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 00:06:22 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 00:11:56 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-31 22:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 00:05:31 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 00:05:52 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-31 18:04:08 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:00:44 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:03:43 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-31 23:03:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:02:04 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 23:03:12 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:10:37 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:04:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:04:59 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:03:14 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:11:57 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:02:56 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:02:02 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:05 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:01:20 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:02:49 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:04:05 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-01 00:02:34 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.012 |  |
| 2026-08-01 00:10:19 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.018 |  |
| 2026-08-01 00:05:44 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-08-01 00:04:35 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.040 |  |
| 2026-08-01 00:01:20 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.044 |  |
| 2026-07-31 22:05:21 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)