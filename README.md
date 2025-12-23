# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_07:19:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,497 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 07:19:17 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.008 |  |
| 2025-12-23 07:17:48 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:15:53 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.008 |  |
| 2025-12-23 07:10:55 | Galgamuwa (Mee Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:10:53 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:09:46 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:09:27 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:07:07 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:06:41 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-23 07:06:19 | Horowpothana (Yan Oya) | 2.91 | 🟢 Normal | -0.064 |  |
| 2025-12-23 07:06:11 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.010 |  |
| 2025-12-23 07:06:10 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-23 07:05:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.070 |  |
| 2025-12-23 07:05:28 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 07:05:01 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:42 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.075 |  |
| 2025-12-23 07:04:40 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2025-12-23 07:04:38 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:34 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:32 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -0.046 |  |
| 2025-12-23 07:04:13 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:08 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:01 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:03:30 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.084 |  |
| 2025-12-23 07:03:23 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | -0.021 |  |
| 2025-12-23 07:02:57 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.968 | 🔺 Rising |
| 2025-12-23 07:02:46 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.068 |  |
| 2025-12-23 07:02:39 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:02:34 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:02:30 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:02:15 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2025-12-23 07:02:07 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:01:40 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-23 07:01:02 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | -0.064 |  |
| 2025-12-23 07:01:01 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:33:25 | Galgamuwa (Mee Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 07:02:57 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.968 | 🔺 Rising |
| 2025-12-23 06:02:25 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2025-12-23 07:06:41 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-23 07:06:10 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-23 07:01:40 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 07:05:28 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 07:02:07 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:01:01 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:02:34 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:09:27 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:10:55 | Galgamuwa (Mee Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:38 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:10:53 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:08 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:01 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:32 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:00:04 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:13 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:05:01 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:02:39 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:09:46 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:07:07 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:17:48 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:02:30 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:04:34 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-23 07:15:53 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.008 |  |
| 2025-12-23 07:19:17 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.008 |  |
| 2025-12-23 07:06:11 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.010 |  |
| 2025-12-23 07:04:40 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2025-12-23 07:02:15 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2025-12-23 07:03:23 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | -0.021 |  |
| 2025-12-23 07:04:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -0.046 |  |
| 2025-12-23 07:01:02 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | -0.064 |  |
| 2025-12-23 07:06:19 | Horowpothana (Yan Oya) | 2.91 | 🟢 Normal | -0.064 |  |
| 2025-12-23 07:02:46 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.068 |  |
| 2025-12-23 07:05:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.070 |  |
| 2025-12-23 07:04:42 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.075 |  |
| 2025-12-23 07:03:30 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)