# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_13:04:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,171 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 13:04:27 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:04:16 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:04:13 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:04:13 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:04:05 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.050 |  |
| 2025-12-28 13:03:57 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:03:56 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.038 |  |
| 2025-12-28 13:03:38 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2025-12-28 13:03:24 | Nagalagam Street (Kelani Ganga) | 0.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-28 13:03:23 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:03:15 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:02:22 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:02:18 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.011 |  |
| 2025-12-28 13:02:16 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-28 13:02:13 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:01:47 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.100 |  |
| 2025-12-28 13:01:44 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-28 13:01:43 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.072 |  |
| 2025-12-28 13:01:35 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-28 13:01:30 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-28 13:01:11 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:00:53 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:00:43 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:00:12 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:15:36 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:08:30 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:07:26 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-28 12:07:23 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:06:18 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 12:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-28 13:03:24 | Nagalagam Street (Kelani Ganga) | 0.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-28 13:01:30 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-28 12:02:17 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-28 13:04:13 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:01:35 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:04:13 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:00:53 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:02:13 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:08:30 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:01:43 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:03:57 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:04:49 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:15:36 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:02:22 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:03:15 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:05:43 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:04:27 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:04:28 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:00:43 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:01:11 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:01:10 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:03:23 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:04:16 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:00:12 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:05:05 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2025-12-28 13:01:44 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-28 13:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:03:43 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-28 13:02:16 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:01:19 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:01:44 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.011 |  |
| 2025-12-28 13:02:18 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.011 |  |
| 2025-12-28 12:01:27 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.011 |  |
| 2025-12-28 13:03:38 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2025-12-28 13:03:56 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.038 |  |
| 2025-12-28 13:04:05 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.050 |  |
| 2025-12-28 13:01:43 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.072 |  |
| 2025-12-28 13:01:47 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)