# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_14:22:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,808 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 14:22:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:10:27 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-22 14:10:00 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-05-22 14:09:57 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.017 |  |
| 2026-05-22 14:09:13 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-22 14:08:40 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-05-22 14:07:36 | Rathnapura (Kalu Ganga) | 7.78 | 🟠 Minor Flood | -0.073 |  |
| 2026-05-22 14:06:55 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-22 14:06:45 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 14:06:39 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-22 14:06:29 | Nagalagam Street (Kelani Ganga) | 1.28 | 🟡 Alert | 0.120 | 🔺 Rising |
| 2026-05-22 14:06:21 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-05-22 14:06:09 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-22 14:06:00 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:05:57 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-22 14:05:46 | Dunamale (Aththanagalu Oya) | 5.02 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-22 14:05:45 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:04:54 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:04:48 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-22 14:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-05-22 14:04:09 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | -0.096 |  |
| 2026-05-22 14:03:50 | Glencourse (Kelani Ganga) | 15.47 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-22 14:03:37 | Badalgama (Maha Oya) | 4.03 | 🟢 Normal | -0.053 |  |
| 2026-05-22 14:03:02 | Ellagawa (Kalu Ganga) | 9.15 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-22 14:03:01 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:02:51 | Hanwella (Kelani Ganga) | 8.09 | 🟠 Minor Flood | 0.061 | 🔺 Rising |
| 2026-05-22 14:02:50 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:02:46 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.234 |  |
| 2026-05-22 14:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.52 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-05-22 14:02:08 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-22 14:02:06 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-05-22 14:01:53 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-22 14:01:44 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:01:32 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-05-22 14:01:23 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:01:18 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:00:54 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-22 13:49:54 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 14:02:51 | Hanwella (Kelani Ganga) | 8.09 | 🟠 Minor Flood | 0.061 | 🔺 Rising |
| 2026-05-22 14:05:46 | Dunamale (Aththanagalu Oya) | 5.02 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-22 14:07:36 | Rathnapura (Kalu Ganga) | 7.78 | 🟠 Minor Flood | -0.073 |  |
| 2026-05-22 14:06:29 | Nagalagam Street (Kelani Ganga) | 1.28 | 🟡 Alert | 0.120 | 🔺 Rising |
| 2026-05-22 14:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.52 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-05-22 13:10:20 | Magura (Kalu Ganga) | 4.37 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-05-22 14:03:50 | Glencourse (Kelani Ganga) | 15.47 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-22 14:08:40 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-05-22 14:06:09 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-22 14:04:48 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-22 14:03:02 | Ellagawa (Kalu Ganga) | 9.15 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-22 14:05:57 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-22 14:09:13 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-22 14:06:55 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-22 14:00:54 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-22 14:06:45 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 14:06:39 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-22 14:04:54 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:01:18 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:02:08 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:22:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:01:23 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:01:44 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:05:45 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:02:50 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:03:01 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:06:00 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-22 14:10:27 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-22 14:02:08 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-22 14:01:32 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-05-22 14:01:53 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-22 14:06:21 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-05-22 14:02:06 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-05-22 14:09:57 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.017 |  |
| 2026-05-22 14:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-05-22 14:10:00 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-05-22 14:03:37 | Badalgama (Maha Oya) | 4.03 | 🟢 Normal | -0.053 |  |
| 2026-05-22 14:04:09 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | -0.096 |  |
| 2026-05-22 14:02:46 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)