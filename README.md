# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_07:16:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,418 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 07:16:37 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.016 |  |
| 2026-05-23 07:09:00 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:07:57 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-05-23 07:07:51 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | -0.029 |  |
| 2026-05-23 07:07:17 | Glencourse (Kelani Ganga) | 12.43 | 🟢 Normal | -0.112 |  |
| 2026-05-23 07:05:58 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-23 07:05:48 | Magura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.038 |  |
| 2026-05-23 07:05:38 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-05-23 07:05:23 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.052 |  |
| 2026-05-23 07:05:22 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.109 |  |
| 2026-05-23 07:04:57 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-05-23 07:04:50 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-05-23 07:04:50 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:04:13 | Nagalagam Street (Kelani Ganga) | 1.42 | 🟡 Alert | -0.016 |  |
| 2026-05-23 07:04:06 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:03:09 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 07:03:09 | Hanwella (Kelani Ganga) | 7.15 | 🟡 Alert | -0.133 |  |
| 2026-05-23 07:03:05 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.022 |  |
| 2026-05-23 07:02:57 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-23 07:02:53 | Ellagawa (Kalu Ganga) | 10.05 | 🟡 Alert | 0.083 | 🔺 Rising |
| 2026-05-23 07:02:48 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.057 |  |
| 2026-05-23 07:02:48 | Rathnapura (Kalu Ganga) | 6.37 | 🟡 Alert | -0.063 |  |
| 2026-05-23 07:02:41 | Dunamale (Aththanagalu Oya) | 5.16 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 07:02:31 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 07:02:30 | Deraniyagala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.151 |  |
| 2026-05-23 07:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.49 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-05-23 07:02:15 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.085 |  |
| 2026-05-23 07:02:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-23 07:01:49 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:01:29 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.021 |  |
| 2026-05-23 07:01:18 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:01:05 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:01:04 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:00:58 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:00:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:00:42 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.002 |  |
| 2026-05-23 07:00:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 07:02:41 | Dunamale (Aththanagalu Oya) | 5.16 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 07:02:53 | Ellagawa (Kalu Ganga) | 10.05 | 🟡 Alert | 0.083 | 🔺 Rising |
| 2026-05-23 07:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.49 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-05-23 07:04:13 | Nagalagam Street (Kelani Ganga) | 1.42 | 🟡 Alert | -0.016 |  |
| 2026-05-23 07:02:48 | Rathnapura (Kalu Ganga) | 6.37 | 🟡 Alert | -0.063 |  |
| 2026-05-23 07:03:09 | Hanwella (Kelani Ganga) | 7.15 | 🟡 Alert | -0.133 |  |
| 2026-05-23 07:05:58 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-23 07:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-23 07:03:09 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 07:02:31 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 07:01:04 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:00:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:09:00 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:04:06 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:04:50 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:01:18 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:00:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:01:49 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:01:05 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:00:58 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 07:00:42 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.002 |  |
| 2026-05-23 07:07:57 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-05-23 07:04:57 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-05-23 07:02:57 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-23 07:16:37 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.016 |  |
| 2026-05-23 07:02:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-23 07:05:38 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-05-23 07:01:29 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.021 |  |
| 2026-05-23 07:03:05 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.022 |  |
| 2026-05-23 07:07:51 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | -0.029 |  |
| 2026-05-23 07:04:50 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-05-23 07:05:48 | Magura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.038 |  |
| 2026-05-23 07:05:23 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.052 |  |
| 2026-05-23 07:02:48 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.057 |  |
| 2026-05-23 07:02:15 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.085 |  |
| 2026-05-23 07:05:22 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.109 |  |
| 2026-05-23 07:07:17 | Glencourse (Kelani Ganga) | 12.43 | 🟢 Normal | -0.112 |  |
| 2026-05-23 07:02:30 | Deraniyagala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)