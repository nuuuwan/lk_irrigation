# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_05:14:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,185 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 05:14:07 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.036 |  |
| 2025-12-16 05:12:35 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | 1.858 | 🔺 Rising |
| 2025-12-16 05:12:10 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.027 |  |
| 2025-12-16 05:11:45 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:11:33 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.049 |  |
| 2025-12-16 05:11:24 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:11:02 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.005 |  |
| 2025-12-16 05:11:00 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:10:49 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -36.000 |  |
| 2025-12-16 05:10:48 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -36.000 |  |
| 2025-12-16 05:10:47 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -36.000 |  |
| 2025-12-16 05:10:45 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -36.000 |  |
| 2025-12-16 05:10:44 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -36.000 |  |
| 2025-12-16 05:10:42 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -36.000 |  |
| 2025-12-16 05:07:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:05:48 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:05:40 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:05:36 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:05:11 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:04:56 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:04:55 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 22.055 | 🔺 Rising |
| 2025-12-16 05:04:31 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 05:04:01 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-16 05:03:58 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 189.474 | 🔺 Rising |
| 2025-12-16 05:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:03:39 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 189.474 | 🔺 Rising |
| 2025-12-16 05:03:15 | Yaka Wewa (Ma Oya) | 1.14 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-16 05:03:11 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.012 |  |
| 2025-12-16 05:03:09 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-16 05:02:37 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:02:28 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.011 |  |
| 2025-12-16 05:02:23 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:02:14 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:02:14 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-16 05:02:00 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | -0.025 |  |
| 2025-12-16 05:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:01:25 | Horowpothana (Yan Oya) | 3.36 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-16 05:01:20 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.020 |  |
| 2025-12-16 05:01:03 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:01:00 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:00:42 | Peradeniya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 22.055 | 🔺 Rising |
| 2025-12-16 04:35:52 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 04:35:05 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.049 |  |
| 2025-12-16 04:33:35 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.059 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 05:03:58 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 189.474 | 🔺 Rising |
| 2025-12-16 05:04:55 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 22.055 | 🔺 Rising |
| 2025-12-16 05:12:35 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | 1.858 | 🔺 Rising |
| 2025-12-16 03:17:47 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2025-12-16 05:03:15 | Yaka Wewa (Ma Oya) | 1.14 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-16 05:01:25 | Horowpothana (Yan Oya) | 3.36 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-16 05:04:01 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-16 05:02:14 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-16 05:04:31 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 05:02:14 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 04:03:36 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:01:03 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:05:48 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:02:37 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:07:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:11:24 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:11:45 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:04:56 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:02:23 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:05:11 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:05:36 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:05:40 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:11:02 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.005 |  |
| 2025-12-16 04:05:54 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2025-12-16 05:02:28 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.011 |  |
| 2025-12-16 05:03:11 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.012 |  |
| 2025-12-16 04:07:33 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.018 |  |
| 2025-12-15 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-16 05:01:20 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.020 |  |
| 2025-12-16 05:03:09 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-16 05:02:00 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | -0.025 |  |
| 2025-12-16 05:12:10 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.027 |  |
| 2025-12-16 05:14:07 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.036 |  |
| 2025-12-16 05:11:33 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.049 |  |
| 2025-12-16 03:00:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.050 |  |
| 2025-12-15 18:00:44 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2025-12-15 18:01:57 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.193 |  |
| 2025-12-16 05:10:49 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)