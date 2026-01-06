# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_13:39:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,212 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 13:39:23 | Manampitiya (Mahaweli Ganga) | 3.54 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-01-06 13:21:37 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.036 |  |
| 2026-01-06 13:20:36 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-06 13:18:06 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-01-06 13:17:52 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.035 |  |
| 2026-01-06 13:16:42 | Padiyathalawa (Maduru Oya) | 2.90 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-01-06 13:12:44 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-01-06 13:12:25 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:09:26 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-06 13:09:05 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-01-06 13:08:47 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:08:34 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.038 |  |
| 2026-01-06 13:08:30 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:06:01 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-01-06 13:05:47 | Nakkala (Kumbukkan Oya) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-01-06 13:05:37 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-06 13:05:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:05:05 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.019 |  |
| 2026-01-06 13:04:35 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-06 13:03:53 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.039 |  |
| 2026-01-06 13:03:48 | Siyambalanduwa (Heda Oya) | 5.40 | 🟡 Alert | 0.087 | 🔺 Rising |
| 2026-01-06 13:03:24 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-06 13:03:17 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-01-06 13:03:15 | Weraganthota (Mahaweli Ganga) | -0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-06 13:03:13 | Thaldena (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-06 13:03:12 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 13:03:10 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:02:49 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.070 |  |
| 2026-01-06 13:02:25 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-06 13:02:22 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 13:02:15 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-01-06 13:01:28 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-06 13:01:18 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:01:11 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:00:35 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 13:00:29 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.010 |  |
| 2026-01-06 13:00:22 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 13:03:48 | Siyambalanduwa (Heda Oya) | 5.40 | 🟡 Alert | 0.087 | 🔺 Rising |
| 2026-01-06 13:39:23 | Manampitiya (Mahaweli Ganga) | 3.54 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-01-06 13:16:42 | Padiyathalawa (Maduru Oya) | 2.90 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-01-06 13:04:35 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-06 13:02:25 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-06 13:01:28 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-06 13:03:24 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-06 13:05:37 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-06 13:20:36 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-06 13:00:35 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 13:03:12 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 13:02:22 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 13:00:22 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 13:09:26 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-06 12:02:55 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:01:18 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:12:25 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:01:11 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:08:30 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:03:10 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:02:49 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:08:47 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:05:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 13:18:06 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-01-06 13:09:05 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-01-06 13:12:44 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-01-06 13:05:47 | Nakkala (Kumbukkan Oya) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-01-06 13:00:29 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.010 |  |
| 2026-01-06 13:03:13 | Thaldena (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-06 13:03:15 | Weraganthota (Mahaweli Ganga) | -0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-06 13:05:05 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.019 |  |
| 2026-01-06 13:06:01 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-01-06 13:03:17 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-01-06 13:17:52 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.035 |  |
| 2026-01-06 13:21:37 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.036 |  |
| 2026-01-06 13:08:34 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.038 |  |
| 2026-01-06 13:03:53 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.039 |  |
| 2026-01-06 13:02:15 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-01-06 13:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)