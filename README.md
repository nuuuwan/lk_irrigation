# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_19:12:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,064 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 19:12:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.060 |  |
| 2025-12-22 19:10:49 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2025-12-22 19:07:51 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.018 |  |
| 2025-12-22 19:06:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2025-12-22 19:06:36 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.030 |  |
| 2025-12-22 19:06:34 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:06:25 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-22 19:06:25 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.045 |  |
| 2025-12-22 19:05:53 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:05:29 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:05:26 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.196 |  |
| 2025-12-22 19:05:14 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2025-12-22 19:05:01 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:04:45 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:04:19 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:03:22 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2025-12-22 19:02:49 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:02:48 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | -0.010 |  |
| 2025-12-22 19:02:22 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:02:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:02:15 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-22 19:01:54 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:01:52 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:01:18 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:01:10 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:01:04 | Horowpothana (Yan Oya) | 3.26 | 🟢 Normal | -0.021 |  |
| 2025-12-22 19:00:58 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.022 |  |
| 2025-12-22 19:00:58 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 18:06:02 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2025-12-22 18:04:39 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-22 19:00:58 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 19:06:25 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-22 19:05:01 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:01:10 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:01:34 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:02:49 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:05:29 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:01:18 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:10:59 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:02:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:01:52 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:30 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:01:54 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:05:53 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:04:19 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:06:34 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:08:04 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:04:45 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:02:22 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 19:10:49 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2025-12-22 19:05:14 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2025-12-22 19:02:15 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-22 19:02:48 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | -0.010 |  |
| 2025-12-22 19:07:51 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.018 |  |
| 2025-12-22 19:03:22 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2025-12-22 19:01:04 | Horowpothana (Yan Oya) | 3.26 | 🟢 Normal | -0.021 |  |
| 2025-12-22 19:00:58 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.022 |  |
| 2025-12-22 19:06:36 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.030 |  |
| 2025-12-22 19:06:25 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.045 |  |
| 2025-12-22 18:01:40 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | -0.051 |  |
| 2025-12-22 19:12:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.060 |  |
| 2025-12-22 19:06:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |
| 2025-12-22 19:05:26 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)