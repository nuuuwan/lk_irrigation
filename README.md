# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_14:11:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,658 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 14:11:19 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:07:51 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:06:58 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:06:57 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:06:26 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:06:26 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:05:55 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2025-12-24 14:05:41 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:05:28 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.052 |  |
| 2025-12-24 14:05:21 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:04:46 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2025-12-24 14:04:18 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:04:13 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.031 |  |
| 2025-12-24 14:03:58 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:52 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:47 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2025-12-24 14:03:24 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:20 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:07 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:07 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 14:03:05 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-24 14:02:57 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 14:02:56 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:02:40 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:02:31 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:02:24 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-24 14:02:18 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-24 14:01:51 | Thanthirimale (Malwathu Oya) | 2.28 | 🟢 Normal | -0.039 |  |
| 2025-12-24 14:01:44 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:01:28 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:01:24 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.037 |  |
| 2025-12-24 14:01:14 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:01:05 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:00:46 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-24 14:00:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-24 13:18:23 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.005 |  |
| 2025-12-24 13:17:57 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:17:40 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:16:06 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-24 13:13:08 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.065 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 14:04:46 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2025-12-24 14:02:24 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-24 14:00:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-24 13:16:06 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-24 14:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-24 14:03:07 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 14:02:57 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 14:02:40 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:01:28 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:02:18 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:58 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:07 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:06:26 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:11:19 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:02:31 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:20 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:01:14 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:01:05 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:24 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:06:26 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:52 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:01:44 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:05:41 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:06:57 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:06:58 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:07:51 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:04:18 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:02:56 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:05:21 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:18:23 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.005 |  |
| 2025-12-24 14:03:47 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2025-12-24 14:00:46 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-24 14:03:05 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-24 14:04:13 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.031 |  |
| 2025-12-24 14:01:24 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.037 |  |
| 2025-12-24 14:01:51 | Thanthirimale (Malwathu Oya) | 2.28 | 🟢 Normal | -0.039 |  |
| 2025-12-24 14:05:55 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2025-12-24 14:05:28 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.052 |  |
| 2025-12-24 13:13:08 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)