# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_01:31:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,156 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 01:31:18 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-24 01:20:46 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:19:24 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:17:33 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2025-12-24 01:17:20 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-24 01:13:56 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2025-12-24 01:10:47 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.012 |  |
| 2025-12-24 01:10:11 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.033 |  |
| 2025-12-24 01:09:40 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:08:59 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:08:17 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.068 |  |
| 2025-12-24 01:08:12 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:07:39 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:05:49 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:05:24 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:04:23 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:04:04 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | 1.162 | 🔺 Rising |
| 2025-12-24 01:03:54 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.078 |  |
| 2025-12-24 01:02:54 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:02:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2025-12-24 01:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:01:23 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:01:13 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.073 |  |
| 2025-12-24 01:01:12 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.020 |  |
| 2025-12-24 01:01:10 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-24 00:46:03 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 00:43:00 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-24 00:41:34 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 01:04:04 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | 1.162 | 🔺 Rising |
| 2025-12-24 01:02:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2025-12-24 01:31:18 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-23 23:11:14 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 01:17:20 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-24 01:05:49 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:02:54 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:01:10 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-24 00:07:10 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:09:40 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:01:23 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:43 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:07:39 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:19:24 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-24 00:04:39 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:05:24 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 00:00:58 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:00:48 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:04:23 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 00:06:08 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:08:59 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:08:12 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:20:46 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 00:13:00 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 00:09:31 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:13:56 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2025-12-23 18:03:15 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-24 01:10:47 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.012 |  |
| 2025-12-23 21:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.013 |  |
| 2025-12-24 00:06:26 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.020 |  |
| 2025-12-24 01:01:12 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.020 |  |
| 2025-12-24 01:10:11 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.033 |  |
| 2025-12-24 01:17:33 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2025-12-24 01:08:17 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.068 |  |
| 2025-12-24 01:01:13 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.073 |  |
| 2025-12-24 01:03:54 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.078 |  |
| 2025-12-23 23:49:20 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -24.000 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)