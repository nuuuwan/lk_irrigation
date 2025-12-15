# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_13:16:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,606 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 13:16:03 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 13:13:32 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.017 |  |
| 2025-12-15 13:10:41 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:10:01 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.017 |  |
| 2025-12-15 13:09:36 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:09:21 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.009 |  |
| 2025-12-15 13:08:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.021 |  |
| 2025-12-15 13:07:21 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.047 |  |
| 2025-12-15 13:07:17 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:06:55 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-15 13:05:20 | Panadugama (Nilwala Ganga) | 3.37 | 🟢 Normal | -0.031 |  |
| 2025-12-15 13:05:16 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2025-12-15 13:05:04 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:04:59 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:04:40 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 13:04:37 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:04:27 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:04:19 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 13:04:18 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:03:28 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -7.200 |  |
| 2025-12-15 13:03:23 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -7.200 |  |
| 2025-12-15 13:03:22 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:03:15 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | -0.021 |  |
| 2025-12-15 13:03:09 | Weraganthota (Mahaweli Ganga) | -1.27 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-15 13:02:39 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:02:20 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:02:19 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2025-12-15 13:02:06 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2025-12-15 13:02:01 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:02:00 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:01:47 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -111.306 |  |
| 2025-12-15 13:01:41 | Galgamuwa (Mee Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:01:18 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:01:14 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.005 |  |
| 2025-12-15 13:01:11 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:00:58 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 13:00:14 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:00:09 | Yaka Wewa (Ma Oya) | 3.95 | 🟢 Normal | -111.306 |  |
| 2025-12-15 13:00:06 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 13:03:09 | Weraganthota (Mahaweli Ganga) | -1.27 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-15 13:06:55 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-15 13:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 13:04:40 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 13:16:03 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 13:04:19 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 13:02:00 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:10:41 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:09:36 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:05:04 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:04:37 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:01:18 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:07:17 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:03:22 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:04:59 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:00:58 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:04:18 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 13:01:14 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.005 |  |
| 2025-12-15 13:09:21 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.009 |  |
| 2025-12-15 13:04:27 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:01:11 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:02:01 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:02:20 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:00:14 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:01:41 | Galgamuwa (Mee Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:02:39 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-15 13:00:06 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.011 |  |
| 2025-12-15 13:13:32 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.017 |  |
| 2025-12-15 13:10:01 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.017 |  |
| 2025-12-15 13:02:19 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2025-12-15 13:03:15 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | -0.021 |  |
| 2025-12-15 13:08:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.021 |  |
| 2025-12-15 13:02:06 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2025-12-15 13:05:16 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2025-12-15 13:05:20 | Panadugama (Nilwala Ganga) | 3.37 | 🟢 Normal | -0.031 |  |
| 2025-12-15 12:03:23 | Horowpothana (Yan Oya) | 3.97 | 🟢 Normal | -0.038 |  |
| 2025-12-15 13:07:21 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.047 |  |
| 2025-12-15 13:03:28 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -7.200 |  |
| 2025-12-15 13:01:47 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -111.306 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)