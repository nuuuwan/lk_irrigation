# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_12:03:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,708 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 12:03:03 | Deraniyagala (Kelani Ganga) | 2.76 | 🟢 Normal | -0.329 |  |
| 2026-05-22 12:02:48 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:02:47 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-22 12:02:20 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | -0.064 |  |
| 2026-05-22 12:02:17 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:02:11 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.019 |  |
| 2026-05-22 12:02:00 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:01:57 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-05-22 12:01:35 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:01:29 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-22 12:01:06 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:00:58 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:00:38 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:00:38 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:00:34 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.017 |  |
| 2026-05-22 11:25:48 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.017 |  |
| 2026-05-22 11:23:12 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 11:13:20 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.027 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 11:02:19 | Dunamale (Aththanagalu Oya) | 4.88 | 🟠 Minor Flood | 0.061 | 🔺 Rising |
| 2026-05-22 11:05:47 | Rathnapura (Kalu Ganga) | 7.84 | 🟠 Minor Flood | 0.037 | 🔺 Rising |
| 2026-05-22 11:04:16 | Hanwella (Kelani Ganga) | 7.78 | 🟡 Alert | 0.231 | 🔺 Rising |
| 2026-05-22 11:05:12 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | 0.211 | 🔺 Rising |
| 2026-05-22 11:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.185 | 🔺 Rising |
| 2026-05-22 11:02:10 | Glencourse (Kelani Ganga) | 15.34 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-05-22 11:05:07 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-05-22 11:05:28 | Ellagawa (Kalu Ganga) | 8.89 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-05-22 11:10:23 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-22 11:05:18 | Putupaula (Kalu Ganga) | 1.86 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-22 11:07:42 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-22 12:02:47 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-22 12:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-22 11:03:42 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-22 11:13:20 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-22 11:04:08 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-22 12:01:29 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:00:38 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:02:48 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:01:35 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:00:38 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 11:01:28 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-22 11:05:16 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 11:05:03 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:00:58 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:02:00 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-22 11:01:14 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:01:06 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-22 11:05:52 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.005 |  |
| 2026-05-22 11:04:50 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-05-22 11:08:26 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-22 12:00:34 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.017 |  |
| 2026-05-22 12:02:11 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.019 |  |
| 2026-05-22 12:01:57 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-05-22 11:05:06 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-05-22 12:02:20 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | -0.064 |  |
| 2026-05-22 11:06:23 | Thawalama (Gin Ganga) | 3.78 | 🟢 Normal | -0.068 |  |
| 2026-05-22 11:08:34 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.154 |  |
| 2026-05-22 12:03:03 | Deraniyagala (Kelani Ganga) | 2.76 | 🟢 Normal | -0.329 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)