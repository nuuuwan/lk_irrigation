# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_16:16:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,953 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 16:16:19 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.025 |  |
| 2026-05-29 16:14:04 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:12:47 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:10:50 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.009 |  |
| 2026-05-29 16:10:26 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:09:52 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-29 16:07:39 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-29 16:06:46 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.038 |  |
| 2026-05-29 16:06:26 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:06:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:05:47 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:05:45 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-05-29 16:03:40 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:03:32 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 16:03:20 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-29 16:03:19 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | -0.129 |  |
| 2026-05-29 16:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-29 16:03:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.104 |  |
| 2026-05-29 16:03:04 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:03:03 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-05-29 16:03:00 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:02:58 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:02:50 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-29 16:02:45 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-29 16:02:44 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-05-29 16:02:40 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.042 |  |
| 2026-05-29 16:02:40 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.064 |  |
| 2026-05-29 16:02:30 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:02:30 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-29 16:02:07 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.036 |  |
| 2026-05-29 16:01:55 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-05-29 16:01:49 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-29 16:01:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:01:36 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.031 |  |
| 2026-05-29 16:01:36 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-29 16:01:22 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:00:44 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:00:18 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-29 15:13:04 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | -0.035 |  |
| 2026-05-29 16:01:49 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-29 16:07:39 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-29 16:09:52 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-29 16:00:18 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 16:03:32 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 16:03:20 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-29 16:05:47 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:12:47 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:01:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:03:04 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:06:26 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:02:30 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:03:40 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:14:04 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:03:00 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:06:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:00:44 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:10:26 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:01:22 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:02:30 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-29 16:10:50 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.009 |  |
| 2026-05-29 16:01:36 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-29 16:01:55 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-05-29 16:02:50 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-29 16:02:45 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-29 16:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-29 16:03:03 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-05-29 16:16:19 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.025 |  |
| 2026-05-29 16:05:45 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-05-29 16:02:44 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-05-29 16:01:36 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.031 |  |
| 2026-05-29 16:02:07 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.036 |  |
| 2026-05-29 16:06:46 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.038 |  |
| 2026-05-29 16:02:40 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.042 |  |
| 2026-05-29 16:02:40 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.064 |  |
| 2026-05-29 16:03:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.104 |  |
| 2026-05-29 16:03:19 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)