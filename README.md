# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_09:09:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,612 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 09:09:54 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:09:44 | Magura (Kalu Ganga) | 3.94 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-05-22 09:09:29 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-22 09:07:58 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-22 09:07:43 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-22 09:07:22 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.131 | 🔺 Rising |
| 2026-05-22 09:06:52 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-22 09:06:35 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-22 09:05:48 | Glencourse (Kelani Ganga) | 15.12 | 🟡 Alert | 0.223 | 🔺 Rising |
| 2026-05-22 09:05:30 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:05:25 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-05-22 09:05:17 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-05-22 09:05:16 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-22 09:05:03 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:04:54 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:04:53 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.528 | 🔺 Rising |
| 2026-05-22 09:04:52 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:04:31 | Hanwella (Kelani Ganga) | 7.26 | 🟡 Alert | 0.428 | 🔺 Rising |
| 2026-05-22 09:04:24 | Thawalama (Gin Ganga) | 3.90 | 🟢 Normal | 0.584 | 🔺 Rising |
| 2026-05-22 09:04:15 | Deraniyagala (Kelani Ganga) | 2.71 | 🟢 Normal | -0.315 |  |
| 2026-05-22 09:04:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-22 09:03:15 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.029 |  |
| 2026-05-22 09:02:55 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-22 09:02:54 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:02:54 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-22 09:02:53 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:02:31 | Badalgama (Maha Oya) | 4.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-22 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.75 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-05-22 09:02:06 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-22 09:01:45 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-05-22 09:01:42 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 09:01:34 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:01:28 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-22 09:01:25 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:00:57 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:00:21 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-05-22 09:00:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 08:11:29 | Rathnapura (Kalu Ganga) | 7.63 | 🟠 Minor Flood | 0.183 | 🔺 Rising |
| 2026-05-22 09:07:22 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.131 | 🔺 Rising |
| 2026-05-22 09:04:31 | Hanwella (Kelani Ganga) | 7.26 | 🟡 Alert | 0.428 | 🔺 Rising |
| 2026-05-22 09:05:48 | Glencourse (Kelani Ganga) | 15.12 | 🟡 Alert | 0.223 | 🔺 Rising |
| 2026-05-22 09:04:24 | Thawalama (Gin Ganga) | 3.90 | 🟢 Normal | 0.584 | 🔺 Rising |
| 2026-05-22 09:04:53 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.528 | 🔺 Rising |
| 2026-05-22 09:09:44 | Magura (Kalu Ganga) | 3.94 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-05-22 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.75 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-05-22 09:05:17 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-05-22 09:06:35 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-22 09:07:43 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-22 09:09:29 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-22 09:01:28 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-22 09:04:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-22 09:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-22 09:02:55 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-22 09:05:16 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-22 09:06:52 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-22 09:02:31 | Badalgama (Maha Oya) | 4.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-22 09:07:58 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-22 09:02:54 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-22 09:01:42 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 09:01:25 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:01:34 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:05:03 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:05:30 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:09:54 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:02:54 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:04:54 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:02:06 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:00:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:02:53 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:04:52 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:00:57 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 09:05:25 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-05-22 09:00:21 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-05-22 09:01:45 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-05-22 09:03:15 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.029 |  |
| 2026-05-22 09:04:15 | Deraniyagala (Kelani Ganga) | 2.71 | 🟢 Normal | -0.315 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)