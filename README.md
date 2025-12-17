# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_12:08:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,356 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 12:08:58 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:08:50 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.095 |  |
| 2025-12-17 12:06:41 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:06:17 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:04:42 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:04:30 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-17 12:04:20 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:04:20 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:04:10 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 12:04:05 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-17 12:04:05 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 12:04:04 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:04:03 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:03:55 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:03:47 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:03:28 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:03:20 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-17 12:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:03:08 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:02:57 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.011 |  |
| 2025-12-17 12:02:48 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-17 12:02:35 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:02:25 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-17 12:02:15 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:02:08 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:02:06 | Yaka Wewa (Ma Oya) | 1.30 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-17 12:02:04 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:01:53 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:01:44 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 12:01:42 | Thanthirimale (Malwathu Oya) | 3.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 12:01:34 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:01:24 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:01:15 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:00:34 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 12:00:25 | Horowpothana (Yan Oya) | 5.79 | 🟢 Normal | -0.030 |  |
| 2025-12-17 12:00:09 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:15:28 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 11:02:12 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-17 12:02:06 | Yaka Wewa (Ma Oya) | 1.30 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-17 12:02:48 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-17 12:04:30 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-17 12:01:42 | Thanthirimale (Malwathu Oya) | 3.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 12:04:05 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-17 11:06:44 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-17 12:04:05 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 12:04:10 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 12:01:44 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 12:02:25 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-17 12:00:34 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 12:01:53 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:01:15 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:04:04 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:04:42 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:02:04 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:02:35 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:00:09 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:04:20 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:06:41 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:08:58 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:03:47 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:02:08 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:01:24 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:01:34 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:06:17 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:03:55 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:03:28 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:03:08 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:02:15 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:04:20 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2025-12-17 12:02:57 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.011 |  |
| 2025-12-17 12:03:20 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-17 12:00:25 | Horowpothana (Yan Oya) | 5.79 | 🟢 Normal | -0.030 |  |
| 2025-12-17 12:08:50 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.095 |  |
| 2025-12-17 11:03:28 | Weraganthota (Mahaweli Ganga) | -1.28 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)