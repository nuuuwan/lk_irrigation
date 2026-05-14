# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_02:35:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 02:35:31 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-15 02:28:20 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:20:02 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:17:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | 0.016 | 🔺 Rising |
| 2026-05-15 02:10:07 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-15 02:09:30 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | -0.009 |  |
| 2026-05-15 02:09:24 | Glencourse (Kelani Ganga) | 14.19 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:09:22 | Glencourse (Kelani Ganga) | 14.19 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:09:21 | Glencourse (Kelani Ganga) | 14.19 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:08:46 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | -0.062 |  |
| 2026-05-15 02:08:25 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-15 02:05:31 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-15 02:05:31 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.020 |  |
| 2026-05-15 02:05:23 | Moragaswewa (Deduru Oya) | 1.86 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-15 02:05:20 | Badalgama (Maha Oya) | 4.66 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-15 02:04:05 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -72.000 |  |
| 2026-05-15 02:04:04 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -72.000 |  |
| 2026-05-15 02:04:03 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -72.000 |  |
| 2026-05-15 02:03:59 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:03:49 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.039 |  |
| 2026-05-15 02:03:37 | Hanwella (Kelani Ganga) | 5.98 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-05-15 02:03:16 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 02:03:15 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | -0.010 |  |
| 2026-05-15 02:03:01 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.005 |  |
| 2026-05-15 02:02:46 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 02:02:28 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:02:20 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:02:07 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:02:03 | Giriulla (Maha Oya) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:01:45 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 02:01:45 | Dunamale (Aththanagalu Oya) | 4.57 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-05-15 02:01:38 | Thawalama (Gin Ganga) | 2.72 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-05-15 02:01:27 | Deraniyagala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.179 |  |
| 2026-05-15 02:01:11 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-15 02:01:00 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:00:22 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:55:55 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 02:01:45 | Dunamale (Aththanagalu Oya) | 4.57 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-05-15 02:17:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | 0.016 | 🔺 Rising |
| 2026-05-15 01:06:57 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.022 |  |
| 2026-05-15 02:03:37 | Hanwella (Kelani Ganga) | 5.98 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-05-15 02:01:38 | Thawalama (Gin Ganga) | 2.72 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-05-15 02:05:23 | Moragaswewa (Deduru Oya) | 1.86 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-15 02:01:11 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-15 02:05:20 | Badalgama (Maha Oya) | 4.66 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-15 02:05:31 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-15 00:02:19 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-15 02:03:16 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 02:10:07 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-15 00:22:27 | Horowpothana (Yan Oya) | 2.83 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-15 02:08:25 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-15 02:01:45 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 02:35:31 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-15 02:02:46 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:00:22 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:02:03 | Giriulla (Maha Oya) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:02:28 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:09:24 | Glencourse (Kelani Ganga) | 14.19 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:03:59 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:28:20 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:02:07 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:01:00 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:20:02 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:02:20 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:03:01 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.005 |  |
| 2026-05-15 02:09:30 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | -0.009 |  |
| 2026-05-15 02:03:15 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | -0.010 |  |
| 2026-05-15 01:05:53 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.011 |  |
| 2026-05-15 02:05:31 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.020 |  |
| 2026-05-15 02:03:49 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.039 |  |
| 2026-05-15 02:08:46 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | -0.062 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-15 02:01:27 | Deraniyagala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.179 |  |
| 2026-05-15 02:04:05 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)