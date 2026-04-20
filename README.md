# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_00:08:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,604 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 00:08:12 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-21 00:06:11 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.035 |  |
| 2026-04-21 00:06:10 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-21 00:05:55 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-04-21 00:05:50 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.128 |  |
| 2026-04-21 00:05:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-21 00:04:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-04-21 00:04:19 | Thanamalwila (Kirindi Oya) | 4.60 | 🟡 Alert | -0.095 |  |
| 2026-04-21 00:04:16 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.150 |  |
| 2026-04-21 00:04:08 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.249 |  |
| 2026-04-21 00:04:07 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-21 00:03:36 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-21 00:03:31 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-21 00:03:23 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 00:02:55 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-21 00:02:36 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 00:02:34 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-21 00:02:29 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-04-21 00:02:21 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-21 00:02:19 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.056 |  |
| 2026-04-21 00:02:17 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.062 |  |
| 2026-04-21 00:02:11 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-21 00:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-21 00:02:00 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 00:01:31 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-04-21 00:01:30 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 00:01:29 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-21 00:01:24 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-21 00:01:16 | Kuda Oya (Kirindi Oya) | 4.85 | 🟢 Normal | -0.050 |  |
| 2026-04-21 00:01:15 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 00:00:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.060 |  |
| 2026-04-20 23:33:11 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.077 |  |
| 2026-04-20 23:30:11 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-20 23:20:41 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | -0.249 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 00:04:19 | Thanamalwila (Kirindi Oya) | 4.60 | 🟡 Alert | -0.095 |  |
| 2026-04-21 00:05:55 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-04-21 00:04:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-21 00:02:11 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-21 00:02:55 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-21 00:03:31 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-20 23:09:46 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-21 00:05:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-21 00:04:07 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-21 00:08:12 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-21 00:02:34 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-21 00:06:10 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-20 23:08:07 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-21 00:02:36 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 00:03:23 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 00:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-21 00:01:29 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-21 00:01:30 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 00:01:24 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-21 00:02:00 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:02:37 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-21 00:03:36 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-21 00:01:15 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 00:02:21 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-21 00:01:31 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-04-21 00:06:11 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.035 |  |
| 2026-04-21 00:01:16 | Kuda Oya (Kirindi Oya) | 4.85 | 🟢 Normal | -0.050 |  |
| 2026-04-21 00:02:29 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-04-20 23:02:34 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.050 |  |
| 2026-04-21 00:02:19 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.056 |  |
| 2026-04-21 00:00:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.060 |  |
| 2026-04-21 00:02:17 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.062 |  |
| 2026-04-20 23:33:11 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.077 |  |
| 2026-04-21 00:05:50 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.128 |  |
| 2026-04-21 00:04:16 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.150 |  |
| 2026-04-21 00:04:08 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.249 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)