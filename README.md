# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_15:09:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,490 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 15:09:54 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.029 |  |
| 2025-12-26 15:09:01 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:08:39 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | -0.018 |  |
| 2025-12-26 15:08:04 | Weraganthota (Mahaweli Ganga) | -1.64 | 🟢 Normal | -0.049 |  |
| 2025-12-26 15:07:08 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-26 15:06:33 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:06:10 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-26 15:06:05 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2025-12-26 15:05:36 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:05:34 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:05:28 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2025-12-26 15:05:26 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-26 15:05:15 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2025-12-26 15:05:08 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-26 15:04:53 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 15:04:40 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:04:16 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:04:04 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:04:00 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:03:57 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2025-12-26 15:03:39 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.060 |  |
| 2025-12-26 15:03:09 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.040 |  |
| 2025-12-26 15:02:58 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:02:47 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:02:32 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:02:27 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-26 15:02:25 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:02:19 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-26 15:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.071 |  |
| 2025-12-26 15:02:06 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:01:45 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-26 15:01:30 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 15:01:27 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-26 15:01:17 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | -0.087 |  |
| 2025-12-26 15:01:15 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:01:04 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:00:52 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:00:24 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-26 15:00:11 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.043 |  |
| 2025-12-26 15:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:29:25 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-26 14:25:31 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 15:07:08 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-26 15:02:19 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-26 15:05:26 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-26 15:05:08 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-26 15:01:30 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 15:04:53 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 15:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:01:15 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:05:34 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:04:16 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:02:58 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:09:01 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:04:00 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:02:32 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:02:25 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:05:36 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:04:04 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:02:06 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:01:04 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:00:52 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:04:40 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:06:33 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 15:06:10 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-26 15:02:27 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-26 15:01:45 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-26 15:01:27 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-26 15:00:24 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-26 15:08:39 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | -0.018 |  |
| 2025-12-26 15:06:05 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2025-12-26 15:05:28 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2025-12-26 15:03:57 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2025-12-26 15:09:54 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.029 |  |
| 2025-12-26 15:05:15 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2025-12-26 15:03:09 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.040 |  |
| 2025-12-26 15:00:11 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.043 |  |
| 2025-12-26 15:08:04 | Weraganthota (Mahaweli Ganga) | -1.64 | 🟢 Normal | -0.049 |  |
| 2025-12-26 15:03:39 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.060 |  |
| 2025-12-26 15:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.071 |  |
| 2025-12-26 15:01:17 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)