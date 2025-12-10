# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_05:13:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,703 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 05:13:44 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2025-12-11 05:13:42 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2025-12-11 05:12:55 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.029 |  |
| 2025-12-11 05:11:17 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.037 |  |
| 2025-12-11 05:09:36 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-11 05:08:44 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.028 |  |
| 2025-12-11 05:08:43 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.005 |  |
| 2025-12-11 05:08:18 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:06:10 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:06:04 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.036 |  |
| 2025-12-11 05:06:03 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.147 |  |
| 2025-12-11 05:04:59 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:04:55 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-11 05:04:48 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:04:38 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-11 05:04:37 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-11 05:04:09 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-11 05:04:03 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-11 05:03:44 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.060 |  |
| 2025-12-11 05:03:41 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:03:30 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:03:10 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:03:07 | Horowpothana (Yan Oya) | 4.75 | 🟢 Normal | -0.158 |  |
| 2025-12-11 05:02:21 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2025-12-11 05:02:09 | Yaka Wewa (Ma Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-11 05:01:44 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.030 |  |
| 2025-12-11 05:01:25 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 05:01:11 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:01:04 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:00:48 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:00:31 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:45:40 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.147 |  |
| 2025-12-11 04:32:37 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-11 04:26:04 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.028 |  |
| 2025-12-11 04:21:08 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 05:13:44 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2025-12-11 05:04:38 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-11 04:00:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2025-12-11 05:09:36 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-11 05:04:55 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-11 05:04:03 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-11 05:01:25 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 04:01:31 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 05:08:43 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.005 |  |
| 2025-12-11 05:00:31 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:00:48 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:01:11 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:03:30 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:03:10 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:08:18 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:03:41 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:01:04 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:06:10 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:04:48 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:04:59 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:19:35 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-11 05:02:09 | Yaka Wewa (Ma Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-11 05:04:09 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-11 05:02:21 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2025-12-11 04:17:01 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.025 |  |
| 2025-12-11 05:08:44 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.028 |  |
| 2025-12-11 05:12:55 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.029 |  |
| 2025-12-11 05:01:44 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.030 |  |
| 2025-12-11 05:06:04 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.036 |  |
| 2025-12-11 05:11:17 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.037 |  |
| 2025-12-11 05:03:44 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.060 |  |
| 2025-12-11 05:06:03 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.147 |  |
| 2025-12-11 05:03:07 | Horowpothana (Yan Oya) | 4.75 | 🟢 Normal | -0.158 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)