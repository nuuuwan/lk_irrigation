# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_00:19:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,188 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 00:19:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-21 00:19:01 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:16:26 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:13:12 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.008 |  |
| 2026-01-21 00:11:36 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:10:03 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:09:27 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:09:02 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-21 00:05:01 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:04:53 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:04:49 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:04:37 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.014 |  |
| 2026-01-21 00:04:35 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-01-21 00:04:34 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.041 |  |
| 2026-01-21 00:04:21 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:04:00 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.523 | 🔺 Rising |
| 2026-01-21 00:03:47 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:03:45 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-21 00:03:30 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:03:17 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:03:15 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:59 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 00:02:44 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.005 |  |
| 2026-01-21 00:02:42 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:29 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.643 |  |
| 2026-01-21 00:02:25 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:13 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-21 00:02:13 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-01-21 00:02:08 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:05 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.021 |  |
| 2026-01-21 00:02:02 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:01:31 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.643 |  |
| 2026-01-21 00:01:14 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:01:06 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 23:50:59 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 00:04:00 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.523 | 🔺 Rising |
| 2026-01-21 00:04:35 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-01-21 00:03:45 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-21 00:09:02 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-21 00:19:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-21 00:02:13 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-21 00:02:59 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 00:01:06 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:19:01 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:04:49 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:04:21 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:29 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:25 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-20 18:01:04 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-20 23:36:59 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:03:17 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:03:15 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:09:27 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:11:36 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:42 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:08 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-20 21:01:57 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:05:01 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:10:03 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 18:01:15 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:02 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:04:53 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:01:14 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:03:30 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 21:10:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:44 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.005 |  |
| 2026-01-21 00:13:12 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.008 |  |
| 2026-01-21 00:04:37 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.014 |  |
| 2026-01-21 00:02:13 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-01-21 00:02:05 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.021 |  |
| 2026-01-21 00:04:34 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.041 |  |
| 2026-01-21 00:02:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.643 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)