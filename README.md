# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_10:27:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,652 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 10:27:08 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:18:09 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:15:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-05-22 10:10:40 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-22 10:10:06 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-05-22 10:08:22 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-22 10:08:09 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:07:49 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-05-22 10:07:38 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-22 10:07:23 | Badalgama (Maha Oya) | 4.24 | 🟢 Normal | -0.037 |  |
| 2026-05-22 10:06:43 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-22 10:06:39 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-22 10:06:37 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-22 10:06:16 | Glencourse (Kelani Ganga) | 15.24 | 🟡 Alert | 0.119 | 🔺 Rising |
| 2026-05-22 10:06:00 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-22 10:05:44 | Ellagawa (Kalu Ganga) | 8.76 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-05-22 10:05:30 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:05:22 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-22 10:05:10 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:05:04 | Thawalama (Gin Ganga) | 3.85 | 🟢 Normal | -0.049 |  |
| 2026-05-22 10:04:27 | Hanwella (Kelani Ganga) | 7.55 | 🟡 Alert | 0.290 | 🔺 Rising |
| 2026-05-22 10:03:55 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-22 10:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-22 10:03:31 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-05-22 10:03:27 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-05-22 10:03:14 | Deraniyagala (Kelani Ganga) | 3.39 | 🟢 Normal | 0.692 | 🔺 Rising |
| 2026-05-22 10:03:10 | Dunamale (Aththanagalu Oya) | 4.82 | 🟠 Minor Flood | 0.086 | 🔺 Rising |
| 2026-05-22 10:02:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:02:36 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.95 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-05-22 10:01:47 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:01:28 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-05-22 10:01:28 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-05-22 10:01:24 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.010 |  |
| 2026-05-22 10:01:20 | Rathnapura (Kalu Ganga) | 7.80 | 🟠 Minor Flood | 0.150 | 🔺 Rising |
| 2026-05-22 10:01:05 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:00:50 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-05-22 10:00:37 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:00:13 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 10:01:20 | Rathnapura (Kalu Ganga) | 7.80 | 🟠 Minor Flood | 0.150 | 🔺 Rising |
| 2026-05-22 10:03:10 | Dunamale (Aththanagalu Oya) | 4.82 | 🟠 Minor Flood | 0.086 | 🔺 Rising |
| 2026-05-22 10:04:27 | Hanwella (Kelani Ganga) | 7.55 | 🟡 Alert | 0.290 | 🔺 Rising |
| 2026-05-22 10:06:16 | Glencourse (Kelani Ganga) | 15.24 | 🟡 Alert | 0.119 | 🔺 Rising |
| 2026-05-22 10:03:14 | Deraniyagala (Kelani Ganga) | 3.39 | 🟢 Normal | 0.692 | 🔺 Rising |
| 2026-05-22 10:03:27 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-05-22 10:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.95 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-05-22 10:10:06 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-05-22 10:05:44 | Ellagawa (Kalu Ganga) | 8.76 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-05-22 10:06:39 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-22 10:03:31 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-05-22 10:06:37 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-22 10:06:00 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-22 10:03:55 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-22 10:10:40 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-22 09:05:16 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-22 10:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-22 10:08:22 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-22 10:07:38 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-22 10:06:43 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-22 10:05:22 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-22 10:01:05 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:00:37 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:18:09 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:27:08 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:01:47 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:08:09 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:05:30 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:05:10 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:02:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:02:36 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-22 10:15:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-05-22 10:01:24 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.010 |  |
| 2026-05-22 10:01:28 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-05-22 10:07:49 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-05-22 10:00:50 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-05-22 10:01:28 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-05-22 10:07:23 | Badalgama (Maha Oya) | 4.24 | 🟢 Normal | -0.037 |  |
| 2026-05-22 10:05:04 | Thawalama (Gin Ganga) | 3.85 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)