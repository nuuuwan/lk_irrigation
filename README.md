# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_05:32:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,421 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 05:32:50 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:31:12 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:14:02 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-23 05:13:48 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.026 |  |
| 2025-12-23 05:11:53 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.016 |  |
| 2025-12-23 05:08:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.044 |  |
| 2025-12-23 05:07:24 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:04:27 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 05:04:20 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-23 05:04:13 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.065 |  |
| 2025-12-23 05:03:53 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:03:42 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.030 |  |
| 2025-12-23 05:03:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2025-12-23 05:03:06 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-23 05:03:05 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:03:03 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-23 05:03:01 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | -0.089 |  |
| 2025-12-23 05:02:58 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:02:48 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 05:02:46 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:02:43 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 05:02:37 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 2.323 | 🔺 Rising |
| 2025-12-23 05:02:06 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 2.323 | 🔺 Rising |
| 2025-12-23 05:01:44 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.071 |  |
| 2025-12-23 05:01:41 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:01:38 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2025-12-23 05:01:30 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.010 |  |
| 2025-12-23 05:01:23 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:01:23 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 05:01:19 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.032 |  |
| 2025-12-23 05:00:58 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:00:55 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:00:38 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:00:30 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-23 05:00:11 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.062 |  |
| 2025-12-23 04:43:22 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.030 |  |
| 2025-12-23 04:42:48 | Horowpothana (Yan Oya) | 3.04 | 🟢 Normal | -0.089 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 05:02:37 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 2.323 | 🔺 Rising |
| 2025-12-23 05:03:06 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-23 05:03:03 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-23 05:02:48 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 05:14:02 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-23 05:00:30 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-23 05:04:27 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 05:01:23 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 05:02:43 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 05:00:38 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:01:23 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:02:46 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:07:24 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:03:53 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:08:26 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:32:50 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:01:40 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:00:55 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:02:58 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:01:41 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:54 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:31:12 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:01:30 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.010 |  |
| 2025-12-23 05:01:38 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2025-12-23 05:03:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2025-12-23 05:04:20 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-23 05:11:53 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.016 |  |
| 2025-12-23 05:13:48 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.026 |  |
| 2025-12-23 05:03:42 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.030 |  |
| 2025-12-23 05:01:19 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.032 |  |
| 2025-12-23 05:08:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.044 |  |
| 2025-12-23 05:00:11 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.062 |  |
| 2025-12-23 05:04:13 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.065 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-23 05:01:44 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.071 |  |
| 2025-12-23 05:03:01 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | -0.089 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)