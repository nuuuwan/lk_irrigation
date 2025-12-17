# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_20:14:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,660 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 20:14:11 | Yaka Wewa (Ma Oya) | 1.62 | 🟢 Normal | -0.017 |  |
| 2025-12-17 20:12:35 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-17 20:11:31 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-17 20:10:29 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:09:52 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:08:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.056 |  |
| 2025-12-17 20:08:35 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:08:04 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:07:42 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-17 20:06:02 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 20:05:58 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-17 20:05:58 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2025-12-17 20:05:48 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:05:23 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:05:12 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:04:52 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-17 20:04:37 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:04:35 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2025-12-17 20:03:58 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:03:47 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:03:35 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-17 20:03:28 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.016 |  |
| 2025-12-17 20:03:16 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 20:02:47 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:02:44 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:02:35 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:02:15 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-17 20:02:10 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-17 20:02:04 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:01:52 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:01:32 | Horowpothana (Yan Oya) | 5.73 | 🟢 Normal | -0.010 |  |
| 2025-12-17 20:01:28 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:01:25 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-17 20:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:00:50 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:00:42 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:52:59 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:47:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.056 |  |
| 2025-12-17 19:26:58 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 20:05:58 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2025-12-17 20:12:35 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-17 20:04:52 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-17 20:01:25 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 20:07:42 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-17 20:03:35 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-17 20:05:58 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-17 20:11:31 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-17 20:03:16 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 20:06:02 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 20:02:04 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:04:37 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:01:28 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:04:26 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:05:12 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:02:47 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:02:35 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:09:52 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:10:29 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:00:50 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:00:42 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:02:44 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:03:58 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:05:23 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:08:04 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:05:48 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:03:47 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:01:52 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:04:35 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2025-12-17 20:01:32 | Horowpothana (Yan Oya) | 5.73 | 🟢 Normal | -0.010 |  |
| 2025-12-17 20:02:15 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-17 20:02:10 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-17 20:03:28 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.016 |  |
| 2025-12-17 20:14:11 | Yaka Wewa (Ma Oya) | 1.62 | 🟢 Normal | -0.017 |  |
| 2025-12-17 20:08:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.056 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)