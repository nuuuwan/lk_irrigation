# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_21:25:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,927 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 21:25:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-24 21:20:38 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:18:18 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-24 21:13:16 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2025-12-24 21:12:49 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -0.043 |  |
| 2025-12-24 21:08:28 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-24 21:07:28 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:06:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2025-12-24 21:06:20 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-24 21:05:42 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:05:19 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:05:17 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:04:48 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-24 21:04:41 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:04:37 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:04:33 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:04:28 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:04:18 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:04:14 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-24 21:03:56 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:03:48 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.052 |  |
| 2025-12-24 21:03:27 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.126 |  |
| 2025-12-24 21:03:22 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:03:07 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:02:55 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:02:34 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-24 21:02:32 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:02:31 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2025-12-24 21:02:04 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2025-12-24 21:01:59 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 21:01:39 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-24 21:01:21 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.041 |  |
| 2025-12-24 21:01:10 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:00:55 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:00:33 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-24 21:00:04 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 21:02:04 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2025-12-24 21:02:34 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-24 21:04:48 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-24 21:18:18 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-24 21:06:20 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-24 21:08:28 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-24 21:25:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-24 21:01:59 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 21:03:22 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:03:56 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:20:38 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:07:28 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:00:04 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:04:33 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:04:41 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:04:37 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:00:55 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:03:07 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:02:32 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:05:19 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:05:42 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:04:18 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:05:17 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:01:10 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:02:55 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 21:00:33 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-24 21:01:39 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-24 21:04:14 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-24 21:13:16 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2025-12-24 21:02:31 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2025-12-24 21:01:21 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.041 |  |
| 2025-12-24 21:12:49 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -0.043 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-24 21:03:48 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.052 |  |
| 2025-12-24 21:06:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2025-12-24 21:03:27 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)