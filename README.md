# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_17:23:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,993 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 17:23:02 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | -0.073 |  |
| 2026-05-29 17:21:32 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:20:35 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:18:00 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:13:13 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-29 17:11:37 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-29 17:11:04 | Hanwella (Kelani Ganga) | 3.65 | 🟢 Normal | -0.055 |  |
| 2026-05-29 17:09:41 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.018 |  |
| 2026-05-29 17:08:32 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.036 |  |
| 2026-05-29 17:08:32 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-05-29 17:07:23 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-29 17:06:57 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:06:45 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-05-29 17:06:35 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2026-05-29 17:06:21 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.065 |  |
| 2026-05-29 17:05:52 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-29 17:05:18 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:04:53 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:04:47 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:04:33 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:03:43 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.012 |  |
| 2026-05-29 17:03:37 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-05-29 17:03:36 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:03:31 | Rathnapura (Kalu Ganga) | 4.06 | 🟢 Normal | -0.090 |  |
| 2026-05-29 17:03:11 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:02:59 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:02:29 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 17:02:23 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-29 17:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-29 17:02:22 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-05-29 17:02:18 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:02:01 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:01:58 | Baddegama (Gin Ganga) | 3.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 17:01:21 | Ellagawa (Kalu Ganga) | 8.52 | 🟢 Normal | -0.020 |  |
| 2026-05-29 17:01:02 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:00:54 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:00:48 | Putupaula (Kalu Ganga) | 2.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 17:00:08 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 17:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-29 17:23:02 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | -0.073 |  |
| 2026-05-29 17:13:13 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-29 17:05:52 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-29 17:02:29 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 17:00:48 | Putupaula (Kalu Ganga) | 2.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 17:01:58 | Baddegama (Gin Ganga) | 3.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 16:00:18 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 17:03:11 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:00:54 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:05:18 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:18:00 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:04:47 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:02:01 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:02:18 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:00:08 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:06:57 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:02:59 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:04:53 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:20:35 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:04:33 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:21:32 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:03:36 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-29 17:11:37 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-29 17:07:23 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-29 17:06:45 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-05-29 17:02:23 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-29 17:03:43 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.012 |  |
| 2026-05-29 17:09:41 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.018 |  |
| 2026-05-29 17:08:32 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-05-29 17:03:37 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-05-29 17:02:22 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-05-29 17:01:21 | Ellagawa (Kalu Ganga) | 8.52 | 🟢 Normal | -0.020 |  |
| 2026-05-29 17:08:32 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.036 |  |
| 2026-05-29 17:11:04 | Hanwella (Kelani Ganga) | 3.65 | 🟢 Normal | -0.055 |  |
| 2026-05-29 17:06:35 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2026-05-29 17:06:21 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.065 |  |
| 2026-05-29 17:03:31 | Rathnapura (Kalu Ganga) | 4.06 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)