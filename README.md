# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_20:21:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,876 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 20:21:28 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | -0.016 |  |
| 2025-12-15 20:18:51 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.016 |  |
| 2025-12-15 20:18:33 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2025-12-15 20:18:10 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:16:05 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2025-12-15 20:11:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-15 20:09:51 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.030 |  |
| 2025-12-15 20:09:07 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.015 |  |
| 2025-12-15 20:08:47 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.048 |  |
| 2025-12-15 20:07:48 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:07:41 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | -0.029 |  |
| 2025-12-15 20:07:21 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.046 |  |
| 2025-12-15 20:07:00 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:05:32 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:04:56 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-15 20:04:50 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.031 |  |
| 2025-12-15 20:04:37 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 20:04:35 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:04:22 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:04:06 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:03:58 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:03:54 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:03:52 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:03:48 | Horowpothana (Yan Oya) | 3.59 | 🟢 Normal | -0.048 |  |
| 2025-12-15 20:03:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 20:02:56 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2025-12-15 20:02:48 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:02:47 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:02:42 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:02:38 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:02:29 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:02:21 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2025-12-15 20:02:13 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:02:09 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.020 |  |
| 2025-12-15 20:00:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:29:00 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 20:11:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-15 20:04:37 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 20:03:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 20:04:56 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-15 20:03:52 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:02:13 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:18:10 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:02:48 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:02:42 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:03:58 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:00:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:07:48 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:07:00 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:04:22 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:05:32 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:16:05 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2025-12-15 20:18:33 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2025-12-15 20:04:06 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:03:54 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:02:29 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:04:35 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:02:38 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:02:47 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:01:10 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-15 20:09:07 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.015 |  |
| 2025-12-15 20:21:28 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | -0.016 |  |
| 2025-12-15 20:18:51 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.016 |  |
| 2025-12-15 20:02:56 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2025-12-15 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-15 20:02:09 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.020 |  |
| 2025-12-15 20:02:21 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2025-12-15 20:07:41 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | -0.029 |  |
| 2025-12-15 20:09:51 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.030 |  |
| 2025-12-15 20:04:50 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.031 |  |
| 2025-12-15 20:07:21 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.046 |  |
| 2025-12-15 20:03:48 | Horowpothana (Yan Oya) | 3.59 | 🟢 Normal | -0.048 |  |
| 2025-12-15 20:08:47 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.048 |  |
| 2025-12-15 18:00:44 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2025-12-15 18:01:57 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)