# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_23:49:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,095 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 23:49:20 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -24.000 |  |
| 2025-12-23 23:49:17 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -24.000 |  |
| 2025-12-23 23:19:29 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -53.143 |  |
| 2025-12-23 23:18:26 | Panadugama (Nilwala Ganga) | 3.50 | 🟢 Normal | -53.143 |  |
| 2025-12-23 23:11:14 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 23:10:31 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:09:31 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:08:49 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2025-12-23 23:08:02 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-23 23:07:27 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.068 |  |
| 2025-12-23 23:07:09 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-23 23:06:43 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-23 23:06:35 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:06:20 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.034 |  |
| 2025-12-23 23:05:15 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:04:56 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:04:27 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:03:57 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-23 23:03:44 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 23:03:41 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.021 |  |
| 2025-12-23 23:03:02 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.031 |  |
| 2025-12-23 23:02:55 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2025-12-23 23:02:33 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:02:18 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:02:10 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:02:00 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:01:55 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:01:53 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:00:51 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:00:49 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:00:41 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:00:40 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:00:20 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.039 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 23:08:49 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2025-12-23 23:00:20 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-23 23:06:43 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-23 23:11:14 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 23:03:44 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 23:02:33 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:04:27 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:00:41 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:00:49 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:28:49 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:10:31 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:02:00 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:43 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:07:39 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:04:56 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:02:10 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:00:51 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:01:53 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:01:55 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:00:48 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:09:31 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:05:15 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:06:35 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:00:40 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:02:18 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 23:07:09 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-23 23:03:57 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:03:15 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-23 23:08:02 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-23 21:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.013 |  |
| 2025-12-23 23:02:55 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2025-12-23 23:03:41 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.021 |  |
| 2025-12-23 23:03:02 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.031 |  |
| 2025-12-23 23:06:20 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.034 |  |
| 2025-12-23 23:07:27 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.068 |  |
| 2025-12-23 23:49:20 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -24.000 |  |
| 2025-12-23 23:19:29 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -53.143 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)