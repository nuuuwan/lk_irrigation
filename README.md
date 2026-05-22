# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_17:26:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,927 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 17:26:43 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:22:57 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:13:23 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.065 |  |
| 2026-05-22 17:10:19 | Ellagawa (Kalu Ganga) | 9.35 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-22 17:08:51 | Rathnapura (Kalu Ganga) | 7.58 | 🟠 Minor Flood | -0.064 |  |
| 2026-05-22 17:08:28 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.032 |  |
| 2026-05-22 17:08:02 | Nagalagam Street (Kelani Ganga) | 1.46 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-05-22 17:06:30 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:05:50 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-22 17:05:43 | Badalgama (Maha Oya) | 3.87 | 🟢 Normal | -0.047 |  |
| 2026-05-22 17:05:33 | Dunamale (Aththanagalu Oya) | 5.10 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-05-22 17:04:46 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.353 |  |
| 2026-05-22 17:04:42 | Glencourse (Kelani Ganga) | 15.25 | 🟡 Alert | -0.104 |  |
| 2026-05-22 17:04:34 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:04:02 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-22 17:03:53 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-05-22 17:03:43 | Deraniyagala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.059 |  |
| 2026-05-22 17:03:41 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-22 17:03:36 | Hanwella (Kelani Ganga) | 8.14 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-22 17:03:32 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 17:03:20 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-22 17:02:45 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:02:42 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:02:35 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.79 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-05-22 17:02:04 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-22 17:01:59 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.079 |  |
| 2026-05-22 17:01:54 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | -0.005 |  |
| 2026-05-22 17:01:53 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-05-22 17:01:47 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:01:31 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-22 17:01:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:01:11 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-22 17:01:10 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.079 |  |
| 2026-05-22 17:01:05 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:00:58 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-22 17:00:19 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 17:05:33 | Dunamale (Aththanagalu Oya) | 5.10 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-05-22 17:03:36 | Hanwella (Kelani Ganga) | 8.14 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-22 17:08:51 | Rathnapura (Kalu Ganga) | 7.58 | 🟠 Minor Flood | -0.064 |  |
| 2026-05-22 17:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.79 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-05-22 17:08:02 | Nagalagam Street (Kelani Ganga) | 1.46 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-05-22 17:08:28 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.032 |  |
| 2026-05-22 17:04:42 | Glencourse (Kelani Ganga) | 15.25 | 🟡 Alert | -0.104 |  |
| 2026-05-22 17:05:50 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-22 17:04:02 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-22 17:00:58 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-22 17:01:11 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-22 17:00:19 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-22 17:10:19 | Ellagawa (Kalu Ganga) | 9.35 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-22 17:03:41 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-22 17:03:32 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 17:06:30 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:01:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:01:05 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:03:07 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:01:47 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:02:45 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:22:57 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:04:34 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:02:42 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:38:34 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:26:43 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:02:35 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 17:01:54 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | -0.005 |  |
| 2026-05-22 17:03:20 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-22 17:01:53 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-05-22 17:02:04 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-22 17:01:31 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-22 17:03:53 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-05-22 17:05:43 | Badalgama (Maha Oya) | 3.87 | 🟢 Normal | -0.047 |  |
| 2026-05-22 17:03:43 | Deraniyagala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.059 |  |
| 2026-05-22 17:13:23 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.065 |  |
| 2026-05-22 17:01:59 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.079 |  |
| 2026-05-22 17:01:10 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.079 |  |
| 2026-05-22 17:04:46 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.353 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)