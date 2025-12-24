# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_08:18:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,422 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 08:18:20 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:17:20 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-24 08:14:31 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.256 |  |
| 2025-12-24 08:13:14 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.387 | 🔺 Rising |
| 2025-12-24 08:12:02 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.017 |  |
| 2025-12-24 08:11:31 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.490 | 🔺 Rising |
| 2025-12-24 08:10:57 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.095 |  |
| 2025-12-24 08:09:43 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:09:03 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-24 08:08:32 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | -0.013 |  |
| 2025-12-24 08:07:48 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:06:52 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2025-12-24 08:05:55 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.020 |  |
| 2025-12-24 08:05:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2025-12-24 08:05:40 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:05:05 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.011 |  |
| 2025-12-24 08:04:54 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:04:41 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:04:16 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:04:00 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-24 08:03:50 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.033 |  |
| 2025-12-24 08:03:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.031 |  |
| 2025-12-24 08:03:14 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:55 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:45 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:37 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | -196.615 |  |
| 2025-12-24 08:02:36 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:35 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:25 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:22 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:20 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-24 08:02:09 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2025-12-24 08:02:05 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:01:50 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.111 |  |
| 2025-12-24 08:01:45 | Weraganthota (Mahaweli Ganga) | 1.42 | 🟢 Normal | -196.615 |  |
| 2025-12-24 08:01:27 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2025-12-24 08:01:18 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.089 |  |
| 2025-12-24 08:01:13 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:01:08 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-24 08:00:58 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 08:11:31 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.490 | 🔺 Rising |
| 2025-12-24 08:13:14 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.387 | 🔺 Rising |
| 2025-12-24 08:04:00 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-24 08:09:03 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-24 08:17:20 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-24 08:01:13 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:04:17 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:04:16 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:04:54 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:04:41 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:36 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:05 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:18:20 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:03:14 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:55 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:00:58 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:25 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:22 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:07:48 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:45 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:09:43 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:05:40 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-24 08:02:20 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-24 08:01:08 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-24 08:02:09 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2025-12-24 08:06:52 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2025-12-24 08:01:27 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2025-12-24 08:05:05 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.011 |  |
| 2025-12-24 08:08:32 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | -0.013 |  |
| 2025-12-24 08:12:02 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.017 |  |
| 2025-12-24 08:05:55 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.020 |  |
| 2025-12-24 08:03:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.031 |  |
| 2025-12-24 08:03:50 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.033 |  |
| 2025-12-24 08:05:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2025-12-24 08:01:18 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.089 |  |
| 2025-12-24 08:10:57 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.095 |  |
| 2025-12-24 08:01:50 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.111 |  |
| 2025-12-24 08:14:31 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.256 |  |
| 2025-12-24 08:02:37 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | -196.615 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)