# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_03:15:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,230 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 03:15:39 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-24 03:13:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.037 |  |
| 2025-12-24 03:12:06 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:08:55 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:08:42 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.081 |  |
| 2025-12-24 03:08:40 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:08:03 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:07:35 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:07:33 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:07:28 | Urawa (Nilwala Ganga) | 2.70 | 🟡 Alert | 0.381 | 🔺 Rising |
| 2025-12-24 03:07:12 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2025-12-24 03:05:43 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:05:40 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-24 03:05:01 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 03:04:53 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2025-12-24 03:04:30 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-24 03:04:24 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:03:57 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:03:21 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 03:03:02 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | -0.048 |  |
| 2025-12-24 03:02:56 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:02:51 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:02:44 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-24 03:02:39 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:02:31 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:01:47 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:01:35 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:01:17 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-24 03:00:45 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-24 02:50:33 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.048 |  |
| 2025-12-24 02:48:12 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:40:28 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:40:26 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:38:39 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2025-12-24 02:33:18 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:20:05 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:20:03 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:20:02 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:20:01 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 03:07:28 | Urawa (Nilwala Ganga) | 2.70 | 🟡 Alert | 0.381 | 🔺 Rising |
| 2025-12-24 02:08:17 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 198.000 | 🔺 Rising |
| 2025-12-24 03:04:53 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2025-12-24 03:02:44 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-24 03:15:39 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-24 03:05:40 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-24 03:05:01 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 03:03:21 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 03:01:35 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:03:57 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:05:43 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:01:47 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:43 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:05:07 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:08:55 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:07:35 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:08:40 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 00:04:39 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:02:31 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:02:39 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:12:06 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:02:56 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:34:35 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:08:03 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:04:24 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:06:41 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:17:51 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:02:51 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:13:28 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:07:12 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2025-12-24 03:04:30 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-24 03:00:45 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:03:15 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-24 03:01:17 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-24 03:13:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.037 |  |
| 2025-12-24 03:03:02 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | -0.048 |  |
| 2025-12-24 03:08:42 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)