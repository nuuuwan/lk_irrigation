# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_20:06:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,102 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 20:06:44 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.024 |  |
| 2025-12-22 20:06:16 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:06:00 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.045 |  |
| 2025-12-22 20:05:49 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2025-12-22 20:05:43 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:05:42 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:05:20 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:05:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.034 |  |
| 2025-12-22 20:05:14 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:04:29 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2025-12-22 20:04:28 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:04:17 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-22 20:03:50 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-22 20:03:21 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:03:19 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.032 |  |
| 2025-12-22 20:03:17 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:02:50 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2025-12-22 20:02:43 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-22 20:02:39 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:02:37 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.013 |  |
| 2025-12-22 20:02:25 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:02:07 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.147 |  |
| 2025-12-22 20:01:59 | Horowpothana (Yan Oya) | 3.24 | 🟢 Normal | -0.020 |  |
| 2025-12-22 20:01:42 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-22 20:01:40 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.012 |  |
| 2025-12-22 20:01:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.067 |  |
| 2025-12-22 20:01:30 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:01:18 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:01:11 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:00:27 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:32:45 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:20:14 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-22 19:20:07 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2025-12-22 19:18:42 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:16:34 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.024 |  |
| 2025-12-22 19:16:19 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.013 |  |
| 2025-12-22 19:12:28 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.045 |  |
| 2025-12-22 19:12:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.034 |  |
| 2025-12-22 19:10:49 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 20:04:29 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2025-12-22 20:04:17 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-22 20:03:50 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-22 20:01:18 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:03:21 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:02:25 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:02:39 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:05:20 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:04:28 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:01:30 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:01:52 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:00:27 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:01:11 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:03:17 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:05:43 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:05:14 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:04:45 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:06:16 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:05:14 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2025-12-22 19:02:15 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-22 20:01:42 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-22 20:02:43 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-22 20:01:40 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.012 |  |
| 2025-12-22 20:02:37 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.013 |  |
| 2025-12-22 20:05:49 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2025-12-22 20:01:59 | Horowpothana (Yan Oya) | 3.24 | 🟢 Normal | -0.020 |  |
| 2025-12-22 20:02:50 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2025-12-22 19:00:58 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.022 |  |
| 2025-12-22 20:06:44 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.024 |  |
| 2025-12-22 20:03:19 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.032 |  |
| 2025-12-22 20:05:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.034 |  |
| 2025-12-22 20:06:00 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.045 |  |
| 2025-12-22 19:06:25 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.045 |  |
| 2025-12-22 20:01:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.067 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 20:02:07 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.147 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)