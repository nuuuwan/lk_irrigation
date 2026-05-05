# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_17:26:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,705 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 17:26:19 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-05-05 17:11:21 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:09:13 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:09:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-05 17:09:07 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:08:50 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-05-05 17:08:09 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-05 17:07:51 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-05-05 17:06:56 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:05:41 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-05 17:05:35 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-05-05 17:05:23 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -0.047 |  |
| 2026-05-05 17:05:17 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:05:02 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.028 |  |
| 2026-05-05 17:04:41 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:04:34 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:04:28 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-05 17:04:11 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-05 17:04:11 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:03:37 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:03:30 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:03:25 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:03:20 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.054 |  |
| 2026-05-05 17:03:09 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.070 |  |
| 2026-05-05 17:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-05 17:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-05-05 17:02:18 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 17:02:17 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.071 |  |
| 2026-05-05 17:02:03 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-05 17:01:47 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:01:42 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.040 |  |
| 2026-05-05 17:01:34 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-05 17:01:28 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:01:18 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:00:43 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-05 17:00:41 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-05 17:00:28 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:00:25 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 17:01:34 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-05 17:09:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-05 17:05:41 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-05 17:00:43 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-05 17:00:41 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-05 17:02:18 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 17:08:09 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-05 17:04:41 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:01:28 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:04:11 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:01:47 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:03:25 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:03:37 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:00:28 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:05:17 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:09:07 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:09:13 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:03:30 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:11:21 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:01:18 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:06:56 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:04:34 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:07:51 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-05-05 17:05:35 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-05-05 17:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-05 17:04:11 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-05 17:02:03 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-05 17:00:25 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-05-05 17:04:28 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-05 17:08:50 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-05-05 16:02:00 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-05-05 17:26:19 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-05-05 17:05:02 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.028 |  |
| 2026-05-05 17:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-05-05 17:01:42 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.040 |  |
| 2026-05-05 17:05:23 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -0.047 |  |
| 2026-05-05 17:03:20 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.054 |  |
| 2026-05-05 17:03:09 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.070 |  |
| 2026-05-05 17:02:17 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)