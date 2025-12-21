# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_14:22:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,992 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 14:22:58 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2025-12-21 14:21:17 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:17:52 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:13:54 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -2.400 |  |
| 2025-12-21 14:13:39 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | -2.400 |  |
| 2025-12-21 14:12:32 | Thanthirimale (Malwathu Oya) | 5.08 | 🟡 Alert | -0.017 |  |
| 2025-12-21 14:09:59 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:08:49 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:08:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.120 |  |
| 2025-12-21 14:08:05 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:08:05 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:07:40 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.073 |  |
| 2025-12-21 14:07:28 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.027 |  |
| 2025-12-21 14:06:59 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:06:38 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.018 |  |
| 2025-12-21 14:05:58 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:05:54 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:05:03 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-21 14:04:44 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 14:04:31 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:04:21 | Weraganthota (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.229 |  |
| 2025-12-21 14:04:13 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:04:08 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-21 14:03:48 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2025-12-21 14:03:40 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2025-12-21 14:03:25 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.062 |  |
| 2025-12-21 14:03:14 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.023 |  |
| 2025-12-21 14:02:59 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2025-12-21 14:02:58 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-21 14:02:56 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:02:40 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.011 |  |
| 2025-12-21 14:02:28 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-21 14:02:06 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:01:48 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-21 14:01:46 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:01:30 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:01:19 | Horowpothana (Yan Oya) | 4.87 | 🟢 Normal | -0.050 |  |
| 2025-12-21 14:01:10 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:01:00 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-21 14:00:53 | Manampitiya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 14:12:32 | Thanthirimale (Malwathu Oya) | 5.08 | 🟡 Alert | -0.017 |  |
| 2025-12-21 14:03:40 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2025-12-21 14:02:59 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2025-12-21 14:01:48 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-21 14:05:03 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-21 14:02:28 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-21 14:04:44 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 14:01:30 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:08:05 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:06:42 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:02:06 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:21:17 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:04:13 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:04:31 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:09:59 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:01:46 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:08:49 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:01:10 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:08:05 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:05:54 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:17:52 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:02:56 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:06:59 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 14:04:08 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-21 14:01:00 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-21 14:02:58 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-21 14:02:40 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.011 |  |
| 2025-12-21 14:06:38 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.018 |  |
| 2025-12-21 14:22:58 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2025-12-21 14:00:53 | Manampitiya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.020 |  |
| 2025-12-21 14:03:48 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2025-12-21 14:03:14 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.023 |  |
| 2025-12-21 14:07:28 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.027 |  |
| 2025-12-21 14:01:19 | Horowpothana (Yan Oya) | 4.87 | 🟢 Normal | -0.050 |  |
| 2025-12-21 14:03:25 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.062 |  |
| 2025-12-21 14:07:40 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.073 |  |
| 2025-12-21 14:08:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.120 |  |
| 2025-12-21 14:04:21 | Weraganthota (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.229 |  |
| 2025-12-21 14:13:54 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -2.400 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)