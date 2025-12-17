# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_11:15:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,320 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 11:15:28 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:10:23 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-17 11:06:44 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-17 11:06:42 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 11:06:39 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:06:22 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:05:56 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-17 11:05:32 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:05:14 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 11:04:30 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.011 |  |
| 2025-12-17 11:04:15 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:04:14 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 11:04:09 | Yaka Wewa (Ma Oya) | 1.24 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-17 11:04:08 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:03:55 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-17 11:03:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-17 11:03:47 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2025-12-17 11:03:30 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 11:03:28 | Weraganthota (Mahaweli Ganga) | -1.28 | 🟢 Normal | -0.102 |  |
| 2025-12-17 11:03:24 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:03:14 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2025-12-17 11:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:03:04 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:03:00 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:02:40 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 11:02:37 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2025-12-17 11:02:18 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:02:16 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:02:12 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-17 11:02:01 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 11:01:46 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 11:01:31 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 11:01:21 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-17 11:01:17 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:00:56 | Horowpothana (Yan Oya) | 5.82 | 🟢 Normal | -0.040 |  |
| 2025-12-17 11:00:56 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:00:46 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 11:03:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-17 11:02:12 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-17 11:05:56 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-17 11:04:09 | Yaka Wewa (Ma Oya) | 1.24 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-17 11:06:44 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-17 11:02:01 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 11:06:42 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 11:01:31 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 11:01:46 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 11:03:30 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 11:02:40 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 11:05:14 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 11:01:17 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:15:28 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:06:22 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:02:16 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:06:39 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:05:32 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:02:56 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:02:37 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:03:04 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:04:08 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:04:15 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:03:00 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:02:18 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:03:24 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:00:56 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 11:00:46 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-17 11:04:14 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 11:03:55 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-17 11:01:21 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-17 11:10:23 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-17 11:03:47 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2025-12-17 11:04:30 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.011 |  |
| 2025-12-17 11:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2025-12-17 11:03:14 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2025-12-17 11:00:56 | Horowpothana (Yan Oya) | 5.82 | 🟢 Normal | -0.040 |  |
| 2025-12-17 11:03:28 | Weraganthota (Mahaweli Ganga) | -1.28 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)