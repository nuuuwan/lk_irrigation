# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_11:11:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,871 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 11:11:32 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2025-12-21 11:10:53 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:09:21 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.058 |  |
| 2025-12-21 11:09:15 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.023 |  |
| 2025-12-21 11:09:14 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2025-12-21 11:08:23 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:06:27 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:05:22 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-21 11:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.068 |  |
| 2025-12-21 11:04:53 | Weraganthota (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.436 | 🔺 Rising |
| 2025-12-21 11:04:37 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:04:34 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2025-12-21 11:04:30 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.031 |  |
| 2025-12-21 11:03:44 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2025-12-21 11:03:38 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-21 11:03:35 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:03:04 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:02:56 | Thanthirimale (Malwathu Oya) | 5.14 | 🟡 Alert | -0.010 |  |
| 2025-12-21 11:02:56 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-21 11:02:55 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-21 11:02:29 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:02:29 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:02:09 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.031 |  |
| 2025-12-21 11:02:06 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:55 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:50 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.019 |  |
| 2025-12-21 11:01:26 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:26 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:20 | Horowpothana (Yan Oya) | 5.09 | 🟢 Normal | -0.150 |  |
| 2025-12-21 11:01:17 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:10 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:07 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 11:00:59 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-21 11:00:45 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-21 11:00:35 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:00:20 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:21:59 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 11:02:56 | Thanthirimale (Malwathu Oya) | 5.14 | 🟡 Alert | -0.010 |  |
| 2025-12-21 11:04:53 | Weraganthota (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.436 | 🔺 Rising |
| 2025-12-21 11:03:38 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-21 10:01:55 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-21 11:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 11:01:26 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:03:35 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:55 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:02:06 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:02:29 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:10 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:07 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:06:27 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:10:53 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:06:27 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:03:04 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:02:29 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:17 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:01:26 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:08:23 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:04:37 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:00:20 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 11:11:32 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2025-12-21 11:05:22 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-21 11:02:55 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-21 11:02:56 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-21 11:00:59 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-21 11:00:45 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-21 11:09:14 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2025-12-21 11:03:44 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2025-12-21 11:01:50 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.019 |  |
| 2025-12-21 11:09:15 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.023 |  |
| 2025-12-21 11:04:34 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2025-12-21 11:04:30 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.031 |  |
| 2025-12-21 11:02:09 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.031 |  |
| 2025-12-21 10:08:24 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.047 |  |
| 2025-12-21 11:09:21 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.058 |  |
| 2025-12-21 11:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.068 |  |
| 2025-12-21 11:01:20 | Horowpothana (Yan Oya) | 5.09 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)