# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_05:04:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,164 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2025-12-16 05:01:00 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.012 |  |
| 2025-12-16 05:00:42 | Peradeniya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -1.576 |  |
| 2025-12-16 04:35:52 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 04:35:05 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.007 |  |
| 2025-12-16 04:33:35 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-16 04:14:49 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.012 |  |
| 2025-12-16 04:14:20 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.012 |  |
| 2025-12-16 04:12:16 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.012 |  |
| 2025-12-16 04:11:32 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-16 04:10:46 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.012 |  |
| 2025-12-16 04:08:19 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.029 |  |
| 2025-12-16 04:08:14 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2025-12-16 04:07:33 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.018 |  |
| 2025-12-16 04:06:31 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 04:06:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-16 04:06:04 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.111 |  |
| 2025-12-16 04:05:54 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 05:03:58 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 189.474 | 🔺 Rising |
| 2025-12-16 03:17:47 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2025-12-16 05:03:15 | Yaka Wewa (Ma Oya) | 1.14 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-16 05:01:25 | Horowpothana (Yan Oya) | 3.36 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-16 05:04:01 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-16 05:02:14 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-16 05:04:31 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 04:06:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-16 05:02:14 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 04:03:36 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:01:03 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:02:37 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-16 04:05:15 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 04:01:53 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 05:02:23 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 04:11:32 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-16 04:35:52 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:08:35 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-16 04:35:05 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.007 |  |
| 2025-12-16 04:05:54 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2025-12-15 23:05:44 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-16 05:02:28 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.011 |  |
| 2025-12-16 05:01:00 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.012 |  |
| 2025-12-16 05:03:11 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.012 |  |
| 2025-12-16 04:07:33 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.018 |  |
| 2025-12-15 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-16 05:01:20 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.020 |  |
| 2025-12-16 03:33:08 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2025-12-16 05:03:09 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-16 05:02:00 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | -0.025 |  |
| 2025-12-16 04:08:19 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.029 |  |
| 2025-12-16 03:00:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.050 |  |
| 2025-12-15 18:00:44 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2025-12-16 04:00:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.064 |  |
| 2025-12-16 04:06:04 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.111 |  |
| 2025-12-15 18:01:57 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.193 |  |
| 2025-12-16 05:00:42 | Peradeniya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -1.576 |  |
| 2025-12-16 04:04:26 | Panadugama (Nilwala Ganga) | 0.85 | 🟢 Normal | -78.980 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)