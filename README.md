# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_06:31:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,896 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 06:31:32 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | -0.045 |  |
| 2025-12-10 06:24:12 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.005 |  |
| 2025-12-10 06:11:06 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-10 06:11:02 | Weraganthota (Mahaweli Ganga) | -1.12 | 🟢 Normal | -0.017 |  |
| 2025-12-10 06:10:06 | Panadugama (Nilwala Ganga) | 4.46 | 🟢 Normal | -0.062 |  |
| 2025-12-10 06:08:55 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 06:08:39 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.363 |  |
| 2025-12-10 06:08:28 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.001 |  |
| 2025-12-10 06:07:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | -0.042 |  |
| 2025-12-10 06:06:39 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.078 |  |
| 2025-12-10 06:06:34 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-10 06:06:18 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.030 |  |
| 2025-12-10 06:05:43 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.019 |  |
| 2025-12-10 06:05:20 | Horowpothana (Yan Oya) | 4.36 | 🟢 Normal | 0.375 | 🔺 Rising |
| 2025-12-10 06:05:02 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-10 06:04:55 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.039 |  |
| 2025-12-10 06:04:37 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-10 06:04:32 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-10 06:04:32 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-10 06:04:31 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:04:21 | Pitabeddara (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.270 |  |
| 2025-12-10 06:04:03 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.032 |  |
| 2025-12-10 06:04:01 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.013 |  |
| 2025-12-10 06:03:12 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.206 |  |
| 2025-12-10 06:02:53 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:02:29 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 06:02:24 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:02:21 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:01:51 | Yaka Wewa (Ma Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2025-12-10 06:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-10 06:01:31 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:01:24 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-10 06:01:12 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:00:56 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-10 06:00:15 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 06:05:20 | Horowpothana (Yan Oya) | 4.36 | 🟢 Normal | 0.375 | 🔺 Rising |
| 2025-12-10 06:01:24 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-10 06:04:32 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-10 06:04:32 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-10 06:11:06 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-10 06:08:55 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 06:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-10 06:02:29 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 06:24:12 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.005 |  |
| 2025-12-10 06:01:12 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:01:31 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:02:53 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:02:24 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:04:31 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:02:21 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-10 06:08:28 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.001 |  |
| 2025-12-10 06:05:02 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-10 06:00:56 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-10 06:04:37 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-10 06:06:34 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-10 06:04:01 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.013 |  |
| 2025-12-10 06:11:02 | Weraganthota (Mahaweli Ganga) | -1.12 | 🟢 Normal | -0.017 |  |
| 2025-12-10 06:05:43 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.019 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-10 06:01:51 | Yaka Wewa (Ma Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-10 06:06:18 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.030 |  |
| 2025-12-10 06:04:03 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.032 |  |
| 2025-12-10 06:00:15 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.034 |  |
| 2025-12-10 06:04:55 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.039 |  |
| 2025-12-10 06:07:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | -0.042 |  |
| 2025-12-10 06:31:32 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | -0.045 |  |
| 2025-12-10 06:10:06 | Panadugama (Nilwala Ganga) | 4.46 | 🟢 Normal | -0.062 |  |
| 2025-12-10 06:06:39 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.078 |  |
| 2025-12-10 06:03:12 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.206 |  |
| 2025-12-10 06:04:21 | Pitabeddara (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.270 |  |
| 2025-12-10 06:08:39 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.363 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)