# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_10:21:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,834 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 10:21:59 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:17:35 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.019 |  |
| 2025-12-21 10:17:21 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.025 |  |
| 2025-12-21 10:16:41 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:09:29 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:08:37 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 10:08:24 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.047 |  |
| 2025-12-21 10:07:46 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.009 |  |
| 2025-12-21 10:07:03 | Weraganthota (Mahaweli Ganga) | -0.54 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2025-12-21 10:06:27 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:06:10 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.196 |  |
| 2025-12-21 10:05:43 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.038 |  |
| 2025-12-21 10:05:41 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:05:21 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:04:59 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.029 |  |
| 2025-12-21 10:04:55 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:04:51 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:04:32 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:04:15 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:04:13 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:04:09 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:03:34 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2025-12-21 10:03:33 | Padiyathalawa (Maduru Oya) | 1.37 | 🟢 Normal | -0.016 |  |
| 2025-12-21 10:03:33 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-21 10:03:28 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:03:16 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2025-12-21 10:03:13 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:03:06 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-21 10:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.77 | 🟢 Normal | -0.031 |  |
| 2025-12-21 10:02:58 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2025-12-21 10:02:42 | Thanthirimale (Malwathu Oya) | 5.15 | 🟡 Alert | -0.020 |  |
| 2025-12-21 10:02:37 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.016 |  |
| 2025-12-21 10:02:31 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-21 10:02:27 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 10:02:11 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:01:55 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-21 10:01:16 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:01:10 | Horowpothana (Yan Oya) | 5.24 | 🟢 Normal | -0.147 |  |
| 2025-12-21 10:01:06 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:59:39 | Manampitiya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 10:02:42 | Thanthirimale (Malwathu Oya) | 5.15 | 🟡 Alert | -0.020 |  |
| 2025-12-21 10:07:03 | Weraganthota (Mahaweli Ganga) | -0.54 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2025-12-21 10:03:33 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-21 10:01:55 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-21 10:02:27 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 10:08:37 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 10:02:11 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:16:41 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:21:59 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:03:28 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:09:29 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:01:06 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:04:51 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:06:27 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:04:32 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:04:55 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:03:13 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:04:15 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:05:21 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:05:41 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:04:09 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 10:07:46 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.009 |  |
| 2025-12-21 10:02:58 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2025-12-21 10:02:31 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-21 10:03:06 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-21 10:03:16 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2025-12-21 10:02:37 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.016 |  |
| 2025-12-21 10:03:33 | Padiyathalawa (Maduru Oya) | 1.37 | 🟢 Normal | -0.016 |  |
| 2025-12-21 10:17:35 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.019 |  |
| 2025-12-21 10:17:21 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.025 |  |
| 2025-12-21 10:04:59 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.029 |  |
| 2025-12-21 10:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.77 | 🟢 Normal | -0.031 |  |
| 2025-12-21 09:59:39 | Manampitiya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.032 |  |
| 2025-12-21 10:05:43 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.038 |  |
| 2025-12-21 10:03:34 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2025-12-21 10:08:24 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.047 |  |
| 2025-12-21 10:01:10 | Horowpothana (Yan Oya) | 5.24 | 🟢 Normal | -0.147 |  |
| 2025-12-21 10:06:10 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)