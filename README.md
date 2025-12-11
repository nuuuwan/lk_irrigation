# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_06:11:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,737 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 06:11:42 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.072 |  |
| 2025-12-11 06:10:54 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2025-12-11 06:09:36 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-11 06:08:45 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.052 |  |
| 2025-12-11 06:06:37 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-11 06:06:31 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 06:05:25 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2025-12-11 06:04:44 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:04:13 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.022 |  |
| 2025-12-11 06:04:09 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-11 06:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.136 |  |
| 2025-12-11 06:04:01 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:03:55 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-11 06:03:27 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:03:23 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 06:02:56 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.073 |  |
| 2025-12-11 06:02:45 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.051 |  |
| 2025-12-11 06:02:38 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-11 06:02:29 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:02:18 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2025-12-11 06:02:09 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.226 |  |
| 2025-12-11 06:02:00 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:01:59 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.041 |  |
| 2025-12-11 06:01:58 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:01:51 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.037 |  |
| 2025-12-11 06:01:33 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-11 06:01:28 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -72.000 |  |
| 2025-12-11 06:01:27 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -72.000 |  |
| 2025-12-11 06:01:23 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:01:19 | Yaka Wewa (Ma Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-11 06:01:03 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-11 06:00:13 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:38:18 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.226 |  |
| 2025-12-11 05:30:09 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.073 |  |
| 2025-12-11 05:13:44 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.072 |  |
| 2025-12-11 05:13:42 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.072 |  |
| 2025-12-11 05:12:55 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.037 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 06:09:36 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-11 06:01:33 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-11 06:04:09 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 06:06:37 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-11 06:03:23 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 06:06:31 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 06:00:13 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:00:48 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:02:00 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:01:23 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:04:44 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:04:01 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:01:58 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:03:27 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:02:29 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:10:54 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2025-12-11 06:03:55 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-11 06:01:03 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-11 06:02:38 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-11 06:02:18 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2025-12-11 06:05:25 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2025-12-11 06:01:19 | Yaka Wewa (Ma Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-11 06:04:13 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.022 |  |
| 2025-12-11 06:01:51 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.037 |  |
| 2025-12-11 06:01:59 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.041 |  |
| 2025-12-11 06:02:45 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.051 |  |
| 2025-12-11 06:08:45 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.052 |  |
| 2025-12-11 06:11:42 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.072 |  |
| 2025-12-11 06:02:56 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.073 |  |
| 2025-12-11 06:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.136 |  |
| 2025-12-11 05:03:07 | Horowpothana (Yan Oya) | 4.75 | 🟢 Normal | -0.158 |  |
| 2025-12-11 06:02:09 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.226 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |
| 2025-12-11 06:01:28 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)