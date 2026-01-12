# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_04:28:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,142 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 04:28:46 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-13 04:24:01 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-13 04:23:47 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.015 |  |
| 2026-01-13 04:22:17 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-13 04:12:13 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:12:02 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.039 |  |
| 2026-01-13 04:11:54 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.041 |  |
| 2026-01-13 04:11:23 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.052 |  |
| 2026-01-13 04:09:48 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.048 |  |
| 2026-01-13 04:08:13 | Horowpothana (Yan Oya) | 3.48 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-13 04:06:53 | Baddegama (Gin Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-01-13 04:06:08 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:06:01 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.287 |  |
| 2026-01-13 04:05:58 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 04:05:33 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-01-13 04:05:04 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 04:04:54 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:03:58 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.005 |  |
| 2026-01-13 04:03:46 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 04:03:34 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-01-13 04:03:31 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-01-13 04:03:22 | Dunamale (Aththanagalu Oya) | 1.45 | 🟢 Normal | -0.048 |  |
| 2026-01-13 04:03:01 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-13 04:02:56 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 04:02:40 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 04:02:38 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:02:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:01:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:01:09 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:00:59 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:00:11 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-13 03:56:45 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.039 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 04:03:34 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-01-13 04:22:17 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-13 03:09:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-13 04:08:13 | Horowpothana (Yan Oya) | 3.48 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-13 04:02:40 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 04:28:46 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-13 04:05:04 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 04:03:46 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 04:02:56 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 04:05:58 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 04:24:01 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-13 04:00:11 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-13 03:01:50 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:04:54 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:15 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:27 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-13 03:10:44 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:02:38 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:01:09 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 03:12:33 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:02:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:00:59 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 03:05:23 | Manampitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:12:13 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:06:08 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-13 04:03:58 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.005 |  |
| 2026-01-13 04:05:33 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-01-13 04:03:01 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-13 04:23:47 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.015 |  |
| 2026-01-13 04:06:53 | Baddegama (Gin Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-01-13 04:12:02 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.039 |  |
| 2026-01-13 03:10:09 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.041 |  |
| 2026-01-13 04:11:54 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.041 |  |
| 2026-01-13 04:03:22 | Dunamale (Aththanagalu Oya) | 1.45 | 🟢 Normal | -0.048 |  |
| 2026-01-13 04:09:48 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.048 |  |
| 2026-01-13 04:11:23 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.052 |  |
| 2026-01-13 04:06:01 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.287 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)