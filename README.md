# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_17:03:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,658 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 17:03:24 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:03:19 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:03:15 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:03:06 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2025-12-25 17:02:58 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:02:33 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:02:15 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | -0.030 |  |
| 2025-12-25 17:02:10 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-25 17:02:02 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:01:54 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2025-12-25 17:01:51 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-25 17:01:43 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.030 |  |
| 2025-12-25 17:01:41 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.023 |  |
| 2025-12-25 17:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:01:20 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:01:15 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:00:51 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:00:34 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:00:26 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-25 17:00:08 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:19:18 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.018 |  |
| 2025-12-25 16:15:41 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-25 16:14:45 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-25 16:14:04 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:12:28 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:09:18 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:09:15 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | -0.023 |  |
| 2025-12-25 16:07:30 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.028 |  |
| 2025-12-25 16:07:25 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2025-12-25 16:07:03 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:07:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-25 16:06:55 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.054 |  |
| 2025-12-25 16:05:44 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 16:05:27 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.029 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 17:02:10 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-25 16:07:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-25 16:15:41 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-25 16:05:44 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 16:05:27 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-25 17:02:15 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:03:19 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:02:58 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:55 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:09:18 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:01:20 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:02:33 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:03:15 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:07:03 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:04:09 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:00:08 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:01:15 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:00:34 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:03:42 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:00:51 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:14:04 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:03:24 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:02:36 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.005 |  |
| 2025-12-25 16:14:45 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-25 16:04:53 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-25 17:01:51 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-25 17:00:26 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-25 17:03:06 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2025-12-25 16:19:18 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.018 |  |
| 2025-12-25 16:07:25 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2025-12-25 17:01:54 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2025-12-25 17:01:41 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.023 |  |
| 2025-12-25 16:07:30 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.028 |  |
| 2025-12-25 17:01:43 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.030 |  |
| 2025-12-25 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | -0.030 |  |
| 2025-12-25 16:06:55 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.054 |  |
| 2025-12-25 16:04:53 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.069 |  |
| 2025-12-25 16:04:05 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.192 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)