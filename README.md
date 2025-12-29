# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_19:30:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,302 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 19:30:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.027 |  |
| 2025-12-29 19:28:33 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-29 19:19:34 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:10:29 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 19:08:53 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:08:22 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.005 |  |
| 2025-12-29 19:08:13 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.009 |  |
| 2025-12-29 19:08:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:08:00 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-29 19:07:18 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:07:15 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:07:13 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-29 19:07:03 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:06:16 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:05:39 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:05:30 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:05:00 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.029 |  |
| 2025-12-29 19:04:59 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:04:27 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2025-12-29 19:04:16 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-29 19:03:41 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2025-12-29 19:03:30 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:03:12 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:02:56 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.039 |  |
| 2025-12-29 19:02:52 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 19:02:50 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-29 19:02:45 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-29 19:02:20 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:02:17 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:01:54 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 19:01:42 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:01:41 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:01:30 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:01:17 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:01:06 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:00:15 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 19:03:41 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2025-12-29 19:02:50 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-29 19:07:13 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-29 19:08:00 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-29 19:04:16 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-29 19:28:33 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-29 19:01:54 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 19:02:52 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 19:10:29 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 19:08:22 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.005 |  |
| 2025-12-29 19:00:15 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:19:34 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:03:30 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:01:41 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:03:12 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:01:06 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:07:53 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:02:17 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:01:42 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:08:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:02:20 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:06:16 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:01:30 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:07:15 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:04:59 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:07:18 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:08:53 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:05:30 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:05:39 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:07:03 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:01:17 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 19:08:13 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.009 |  |
| 2025-12-29 18:06:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-29 19:02:45 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-29 19:04:27 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2025-12-29 19:30:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.027 |  |
| 2025-12-29 19:05:00 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.029 |  |
| 2025-12-29 19:02:56 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)