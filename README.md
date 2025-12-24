# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_13:18:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,622 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 13:18:23 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.005 |  |
| 2025-12-24 13:17:57 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2025-12-24 13:17:40 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:16:06 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-24 13:13:08 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.065 |  |
| 2025-12-24 13:12:12 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-24 13:12:07 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-24 13:09:38 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2025-12-24 13:08:41 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:08:07 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.069 |  |
| 2025-12-24 13:07:47 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.092 |  |
| 2025-12-24 13:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.037 |  |
| 2025-12-24 13:06:53 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:06:42 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:06:31 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.087 |  |
| 2025-12-24 13:06:17 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:05:39 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:04:50 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:04:43 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 13:04:25 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:03:47 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:03:33 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:03:15 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 13:03:12 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:02:57 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:02:54 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:02:41 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:02:22 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:02:19 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:01:49 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 13:01:47 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:01:39 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:01:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-24 13:01:12 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:01:10 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:00:57 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:00:57 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-24 13:00:39 | Thanthirimale (Malwathu Oya) | 2.32 | 🟢 Normal | -0.031 |  |
| 2025-12-24 12:59:37 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:58:41 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 13:01:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-24 13:00:57 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-24 13:12:07 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-24 13:16:06 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-24 13:01:49 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 13:04:43 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 13:03:15 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 13:12:12 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-24 13:01:12 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:01:10 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:02:41 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:01:39 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:05:39 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:06:42 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:02:57 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:08:41 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:00:57 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:01:47 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:06:53 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:17:40 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:04:25 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:59:37 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:02:54 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 13:18:23 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.005 |  |
| 2025-12-24 13:17:57 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2025-12-24 13:09:38 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2025-12-24 13:06:17 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:02:19 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:03:33 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:04:50 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:03:47 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:02:22 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:03:12 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-24 13:00:39 | Thanthirimale (Malwathu Oya) | 2.32 | 🟢 Normal | -0.031 |  |
| 2025-12-24 13:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.037 |  |
| 2025-12-24 13:13:08 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.065 |  |
| 2025-12-24 13:08:07 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.069 |  |
| 2025-12-24 13:06:31 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.087 |  |
| 2025-12-24 13:07:47 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)