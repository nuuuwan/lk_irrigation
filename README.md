# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_15:10:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,912 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 15:10:13 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:09:33 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.012 |  |
| 2025-12-22 15:08:13 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:06:42 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:06:07 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:05:43 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:05:35 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 15:04:31 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:04:24 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:04:05 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2025-12-22 15:04:01 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:03:37 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:03:36 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 15:03:34 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:03:22 | Galgamuwa (Mee Oya) | 1.10 | 🟢 Normal | -0.200 |  |
| 2025-12-22 15:03:19 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:03:15 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:03:08 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 15:02:46 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:02:44 | Thanthirimale (Malwathu Oya) | 4.50 | 🟢 Normal | -0.020 |  |
| 2025-12-22 15:02:44 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.039 |  |
| 2025-12-22 15:02:30 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:01:58 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:01:42 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | -0.040 |  |
| 2025-12-22 15:01:40 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 15:01:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.041 |  |
| 2025-12-22 15:01:34 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:01:17 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:01:16 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:01:11 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:01:08 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:01:08 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:00:51 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:00:18 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:00:10 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:00:08 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:22:19 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:18:30 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.012 |  |
| 2025-12-22 14:18:09 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 15:04:05 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2025-12-22 15:01:40 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 15:05:35 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 15:03:36 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 15:03:08 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 15:01:08 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:01:11 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:01:34 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:04:31 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:02:30 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:06:42 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:02:46 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:03:15 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:10:13 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:06:07 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:00:51 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:04:01 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:01:16 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:01:17 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:03:37 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:01:08 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:22:19 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:08:13 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:03:34 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:05:43 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:04:24 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:00:18 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:00:08 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:00:10 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:01:58 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2025-12-22 15:03:19 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:18:09 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2025-12-22 15:09:33 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.012 |  |
| 2025-12-22 15:02:44 | Thanthirimale (Malwathu Oya) | 4.50 | 🟢 Normal | -0.020 |  |
| 2025-12-22 15:02:44 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.039 |  |
| 2025-12-22 15:01:42 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | -0.040 |  |
| 2025-12-22 15:01:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.041 |  |
| 2025-12-22 15:03:22 | Galgamuwa (Mee Oya) | 1.10 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)