# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_07:19:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,839 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 07:19:26 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:16:53 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:16:21 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:15:51 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.008 |  |
| 2026-01-17 07:11:01 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-17 07:09:48 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:06:57 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.020 |  |
| 2026-01-17 07:06:15 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:05:41 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:05:32 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.029 |  |
| 2026-01-17 07:05:20 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:05:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-01-17 07:04:47 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:04:47 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:04:44 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.093 |  |
| 2026-01-17 07:04:43 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.003 |  |
| 2026-01-17 07:04:41 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:04:18 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 07:03:54 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:03:49 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:03:35 | Kithulgala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.325 |  |
| 2026-01-17 07:03:34 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.042 |  |
| 2026-01-17 07:03:23 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:03:21 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-01-17 07:02:36 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.177 |  |
| 2026-01-17 07:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.131 |  |
| 2026-01-17 07:02:27 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:02:25 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:02:24 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:02:15 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:02:13 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:01:43 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.112 |  |
| 2026-01-17 07:01:36 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:01:30 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:01:28 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:01:23 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 07:00:19 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:33:57 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 07:11:01 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-17 07:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 07:04:18 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 07:01:23 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:02:15 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:01:28 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:16:21 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:55 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:02:13 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:04:41 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:01:36 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:19:26 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:00:19 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:03:23 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:09:48 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:02:25 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:03:49 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:04:47 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:06:15 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:02:27 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 07:04:43 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.003 |  |
| 2026-01-17 07:15:51 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.008 |  |
| 2026-01-17 07:03:54 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:01:30 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:04:47 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:05:41 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:05:20 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:16:53 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-01-17 07:03:21 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-01-17 07:06:57 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.020 |  |
| 2026-01-17 07:05:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-01-17 07:05:32 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.029 |  |
| 2026-01-17 06:09:19 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.038 |  |
| 2026-01-17 07:03:34 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.042 |  |
| 2026-01-17 07:04:44 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.093 |  |
| 2026-01-17 07:01:43 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.112 |  |
| 2026-01-17 07:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.131 |  |
| 2026-01-17 07:02:36 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.177 |  |
| 2026-01-17 07:03:35 | Kithulgala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.325 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)