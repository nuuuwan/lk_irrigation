# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_00:08:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,200 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 00:08:23 | Manampitiya (Mahaweli Ganga) | 2.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-14 00:07:41 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-14 00:06:09 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:05:56 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.064 |  |
| 2025-12-14 00:05:22 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:04:54 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.039 |  |
| 2025-12-14 00:04:45 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-14 00:04:40 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-14 00:04:17 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-14 00:04:11 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:04:07 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:03:42 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:03:28 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:03:14 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:03:13 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:03:07 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:02:51 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:02:39 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.021 |  |
| 2025-12-14 00:02:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2025-12-14 00:02:38 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2025-12-14 00:02:27 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:02:13 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:02:11 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-14 00:02:10 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:01:38 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:01:29 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | -0.020 |  |
| 2025-12-14 00:01:27 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 00:01:24 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:01:18 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:01:11 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.022 |  |
| 2025-12-14 00:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:00:19 | Horowpothana (Yan Oya) | 5.28 | 🟢 Normal | -0.061 |  |
| 2025-12-13 23:35:09 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-13 23:23:15 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:12:48 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.039 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 00:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2025-12-14 00:07:41 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-14 00:02:11 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-14 00:04:17 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-14 00:04:40 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-14 00:04:45 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-13 23:12:48 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-14 00:08:23 | Manampitiya (Mahaweli Ganga) | 2.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 23:07:36 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-14 00:01:27 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 00:02:51 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:01:18 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:03:14 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:03:28 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:02:13 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:03:13 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:03:07 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:04:07 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:03:42 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:02:54 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:04:11 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:01:24 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:06:09 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:02:27 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:02:38 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:01:38 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:05:22 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:02:10 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-14 00:01:29 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | -0.020 |  |
| 2025-12-14 00:02:39 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.021 |  |
| 2025-12-14 00:01:11 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.022 |  |
| 2025-12-14 00:02:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2025-12-14 00:04:54 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.039 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-14 00:00:19 | Horowpothana (Yan Oya) | 5.28 | 🟢 Normal | -0.061 |  |
| 2025-12-14 00:05:56 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)