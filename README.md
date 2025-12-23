# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_13:06:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,720 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 13:06:17 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:06:13 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:05:43 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:05:38 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.276 |  |
| 2025-12-23 13:05:18 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2025-12-23 13:04:33 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-23 13:04:27 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:04:19 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.051 |  |
| 2025-12-23 13:04:14 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:04:09 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:03:47 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:03:33 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:03:26 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -36.000 |  |
| 2025-12-23 13:03:24 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:03:24 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -36.000 |  |
| 2025-12-23 13:03:15 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-23 13:02:45 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:02:29 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2025-12-23 13:02:26 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:02:20 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-23 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | -0.050 |  |
| 2025-12-23 13:02:07 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2025-12-23 13:01:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-23 13:01:56 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.010 |  |
| 2025-12-23 13:01:50 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.041 |  |
| 2025-12-23 13:01:30 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:01:26 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:01:24 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:01:13 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 13:00:54 | Thanthirimale (Malwathu Oya) | 3.26 | 🟢 Normal | -0.046 |  |
| 2025-12-23 13:00:51 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | -0.040 |  |
| 2025-12-23 13:00:49 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2025-12-23 13:00:08 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:17:46 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:11:18 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:08:29 | Thanthirimale (Malwathu Oya) | 3.30 | 🟢 Normal | -0.046 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 13:02:20 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-23 13:04:33 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-23 13:01:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-23 13:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 13:01:13 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:00:08 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:01:26 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:03:47 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:03:24 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:01:24 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:05:43 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:02:45 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:01:30 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:04:09 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:06:13 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:05:12 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:03:33 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:04:14 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:02:26 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:04:27 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:06:17 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:02:46 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:02:44 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 13:05:18 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2025-12-23 13:03:15 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-23 13:01:56 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.010 |  |
| 2025-12-23 13:02:07 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2025-12-23 12:04:11 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2025-12-23 13:02:29 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2025-12-23 13:00:49 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2025-12-23 12:01:32 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2025-12-23 13:00:51 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | -0.040 |  |
| 2025-12-23 13:01:50 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.041 |  |
| 2025-12-23 13:00:54 | Thanthirimale (Malwathu Oya) | 3.26 | 🟢 Normal | -0.046 |  |
| 2025-12-23 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | -0.050 |  |
| 2025-12-23 13:04:19 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.051 |  |
| 2025-12-23 13:05:38 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.276 |  |
| 2025-12-23 13:03:26 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)