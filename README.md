# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_16:07:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,630 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 16:07:30 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.028 |  |
| 2025-12-25 16:07:25 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2025-12-25 16:07:03 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:07:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-25 16:06:55 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.054 |  |
| 2025-12-25 16:05:44 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 16:05:27 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-25 16:04:53 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-25 16:04:53 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.069 |  |
| 2025-12-25 16:04:42 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-25 16:04:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:04:13 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -0.032 |  |
| 2025-12-25 16:04:09 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:04:05 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.192 |  |
| 2025-12-25 16:03:51 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2025-12-25 16:03:42 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:03:31 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:03:10 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:02:36 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.005 |  |
| 2025-12-25 16:02:21 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:02:18 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 16:02:17 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:02:13 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.030 |  |
| 2025-12-25 16:01:55 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:34 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:17 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:15 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:09 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:00:57 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:00:47 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:00:29 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-25 16:00:11 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:12:49 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.029 |  |
| 2025-12-25 15:11:11 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.054 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 16:03:51 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2025-12-25 16:07:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-25 16:05:44 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 16:05:27 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-25 16:02:18 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 15:01:39 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 15:04:49 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 16:03:10 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:00:11 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:17 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:55 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:02:13 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:03:31 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:07:03 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:04:09 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:34 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:02:17 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:05:05 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:04:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:03:42 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:09 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:02:21 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:01:15 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 16:02:36 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.005 |  |
| 2025-12-25 16:04:53 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-25 16:04:42 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-25 16:00:29 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-25 15:05:32 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.014 |  |
| 2025-12-25 16:07:25 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2025-12-25 15:03:20 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.022 |  |
| 2025-12-25 16:07:30 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.028 |  |
| 2025-12-25 15:12:49 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.029 |  |
| 2025-12-25 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.030 |  |
| 2025-12-25 16:04:13 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -0.032 |  |
| 2025-12-25 14:08:43 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.043 |  |
| 2025-12-25 16:06:55 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.054 |  |
| 2025-12-25 16:04:53 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.069 |  |
| 2025-12-25 16:04:05 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.192 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)