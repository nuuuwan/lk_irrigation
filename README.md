# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_17:04:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,859 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 17:04:02 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | -0.038 |  |
| 2025-12-23 17:03:55 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:44 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2025-12-23 17:03:40 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:39 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:31 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:15 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 17:03:13 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2025-12-23 17:02:46 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.010 |  |
| 2025-12-23 17:02:21 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-23 17:02:09 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:01:50 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:01:15 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.041 |  |
| 2025-12-23 17:01:13 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:01:07 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:00:39 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -36.000 |  |
| 2025-12-23 17:00:38 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | -36.000 |  |
| 2025-12-23 17:00:30 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 17:00:08 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:58:56 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-23 16:13:53 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:13:31 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-23 16:12:45 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:12:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:09:31 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:08:57 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:07:27 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:06:56 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:06:15 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:05:51 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 16:58:56 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-23 17:02:21 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 17:00:30 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 17:03:15 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 16:02:50 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 17:01:13 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:00:08 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:01:50 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:02:43 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:01:09 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:40 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:06:15 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:12:45 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:12:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:06:56 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:03:10 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:01:07 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:08:57 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:02:09 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:39 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:55 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:31 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:02:32 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:07:27 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:04:23 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-23 16:04:22 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-23 17:02:46 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.010 |  |
| 2025-12-23 16:03:28 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-23 17:03:13 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2025-12-23 16:03:30 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2025-12-23 17:03:44 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2025-12-23 17:04:02 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | -0.038 |  |
| 2025-12-23 17:01:15 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.041 |  |
| 2025-12-23 16:03:52 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.052 |  |
| 2025-12-23 16:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.080 |  |
| 2025-12-23 16:04:00 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.149 |  |
| 2025-12-23 17:00:39 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)