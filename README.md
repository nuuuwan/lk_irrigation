# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_08:43:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,214 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 08:43:18 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:25:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.016 |  |
| 2025-12-26 08:21:49 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.040 |  |
| 2025-12-26 08:19:24 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:13:10 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:12:17 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.009 |  |
| 2025-12-26 08:11:54 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-26 08:10:32 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-26 08:09:26 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.067 |  |
| 2025-12-26 08:08:58 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.032 |  |
| 2025-12-26 08:08:30 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2025-12-26 08:08:13 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2025-12-26 08:08:13 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:07:15 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-26 08:06:50 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:06:27 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:06:18 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2025-12-26 08:05:41 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:05:41 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:04:58 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2025-12-26 08:04:54 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-26 08:04:42 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:04:11 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-26 08:03:41 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.021 |  |
| 2025-12-26 08:03:40 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:03:35 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 08:03:25 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 08:02:58 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:02:51 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:02:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.124 |  |
| 2025-12-26 08:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-26 08:02:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.010 |  |
| 2025-12-26 08:01:59 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:01:20 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.032 |  |
| 2025-12-26 08:01:15 | Thanthirimale (Malwathu Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-26 08:01:13 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2025-12-26 08:01:08 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 08:01:07 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 08:10:32 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-26 08:04:54 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-26 08:04:11 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-26 08:07:15 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-26 08:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-26 08:01:08 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 08:03:35 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 08:03:25 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 08:08:13 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:43:18 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:02:58 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:02:51 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:19:24 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:05:41 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:13:10 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:04:42 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:01:59 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:05:41 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:03:40 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:06:50 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:02:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:06:27 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:12:17 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.009 |  |
| 2025-12-26 08:08:13 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2025-12-26 08:11:54 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-26 08:08:30 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2025-12-26 08:01:13 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2025-12-26 08:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.010 |  |
| 2025-12-26 08:01:15 | Thanthirimale (Malwathu Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-26 08:01:07 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.011 |  |
| 2025-12-26 08:25:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.016 |  |
| 2025-12-26 08:06:18 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2025-12-26 08:03:41 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.021 |  |
| 2025-12-26 08:04:58 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2025-12-26 08:08:58 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.032 |  |
| 2025-12-26 08:01:20 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.032 |  |
| 2025-12-26 08:21:49 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.040 |  |
| 2025-12-26 08:09:26 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.067 |  |
| 2025-12-26 08:02:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)