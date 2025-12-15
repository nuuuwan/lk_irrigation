# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_01:20:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,038 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 01:20:59 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:16:46 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.008 |  |
| 2025-12-16 01:09:06 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 01:08:40 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-16 01:08:11 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2025-12-16 01:07:25 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-16 01:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 01:06:14 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-16 01:04:47 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:04:46 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-16 01:03:59 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2025-12-16 01:03:33 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:03:31 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:03:30 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:03:21 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:02:57 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:02:53 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:02:45 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:02:34 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:02:29 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-16 01:02:26 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | -0.039 |  |
| 2025-12-16 01:02:24 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 01:02:14 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:02:14 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:01:25 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | -0.020 |  |
| 2025-12-16 01:01:13 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.040 |  |
| 2025-12-16 00:54:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-16 00:52:49 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 01:08:40 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-16 01:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 00:32:44 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-16 00:00:27 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-16 01:09:06 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 01:02:24 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 01:02:14 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:02:34 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:03:30 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:03:21 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:03:31 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:02:14 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:06:36 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:02:53 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:03:33 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-16 00:06:05 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-16 00:54:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:02:57 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:02:45 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:04:47 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:20:59 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-16 01:16:46 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.008 |  |
| 2025-12-16 01:06:14 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:03:53 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-16 01:07:25 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-16 01:04:46 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-16 01:02:29 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:05:44 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:06:33 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2025-12-16 00:52:49 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.017 |  |
| 2025-12-15 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-16 01:01:25 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | -0.020 |  |
| 2025-12-16 01:08:11 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2025-12-16 01:03:59 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2025-12-16 01:02:26 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | -0.039 |  |
| 2025-12-16 01:01:13 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.040 |  |
| 2025-12-15 23:01:31 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.041 |  |
| 2025-12-15 18:00:44 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2025-12-15 18:01:57 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)