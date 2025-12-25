# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_02:06:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,985 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 02:06:24 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.009 |  |
| 2025-12-26 02:06:00 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-26 02:05:28 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 02:05:04 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2025-12-26 02:04:23 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.029 |  |
| 2025-12-26 02:04:18 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.039 |  |
| 2025-12-26 02:03:54 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.060 |  |
| 2025-12-26 02:03:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2025-12-26 02:03:40 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:03:39 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:03:36 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-26 02:03:31 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:03:28 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-26 02:03:09 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2025-12-26 02:02:23 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:02:22 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:02:19 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.027 |  |
| 2025-12-26 02:02:16 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:02:14 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:01:41 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-26 02:01:28 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:01:25 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:00:45 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:00:29 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:00:12 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.005 |  |
| 2025-12-26 01:49:10 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:40:29 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2025-12-26 01:37:48 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.013 |  |
| 2025-12-26 01:37:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 3.375 | 🔺 Rising |
| 2025-12-26 01:36:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | 3.375 | 🔺 Rising |
| 2025-12-26 01:36:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 3.375 | 🔺 Rising |
| 2025-12-26 01:24:04 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:13:41 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | 0.066 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 01:37:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 3.375 | 🔺 Rising |
| 2025-12-26 02:03:28 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-26 01:13:41 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-26 02:03:36 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-26 02:05:28 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 02:01:25 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:01:28 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:24:04 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:02:14 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:00:29 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:49:10 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:26:35 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:03:31 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:01:05 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:00:45 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:02:23 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:02:16 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:02:22 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:03:40 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:03:37 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:00:12 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.005 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-26 02:06:24 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.009 |  |
| 2025-12-26 01:06:52 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2025-12-26 02:01:41 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-26 02:03:09 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2025-12-26 01:40:29 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2025-12-26 01:37:48 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.013 |  |
| 2025-12-26 02:05:04 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2025-12-26 02:06:00 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-26 00:18:14 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.025 |  |
| 2025-12-26 02:02:19 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.027 |  |
| 2025-12-26 02:04:23 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.029 |  |
| 2025-12-26 02:04:18 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.039 |  |
| 2025-12-26 02:03:54 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.060 |  |
| 2025-12-26 02:03:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2025-12-26 01:04:32 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)