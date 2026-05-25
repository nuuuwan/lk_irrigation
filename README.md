# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_05:24:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,957 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 05:24:24 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.101 |  |
| 2026-05-25 05:21:56 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:18:14 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:18:13 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:16:55 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | -0.107 |  |
| 2026-05-25 05:13:50 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-25 05:12:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | 0.137 | 🔺 Rising |
| 2026-05-25 05:10:45 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.113 |  |
| 2026-05-25 05:09:26 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-25 05:08:24 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-25 05:06:43 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-25 05:05:52 | Hanwella (Kelani Ganga) | 4.98 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-25 05:05:48 | Deraniyagala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.065 |  |
| 2026-05-25 05:05:34 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 05:04:33 | Ellagawa (Kalu Ganga) | 9.20 | 🟢 Normal | -0.029 |  |
| 2026-05-25 05:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.058 |  |
| 2026-05-25 05:04:15 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:04:11 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-05-25 05:04:07 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-05-25 05:03:21 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.070 |  |
| 2026-05-25 05:03:18 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.018 |  |
| 2026-05-25 05:03:08 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 05:02:56 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-05-25 05:02:46 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:02:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:02:27 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | -0.194 |  |
| 2026-05-25 05:02:23 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:02:21 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-05-25 05:02:11 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:02:10 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-25 05:01:55 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:01:04 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:00:43 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.061 |  |
| 2026-05-25 05:00:33 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 05:00:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 05:12:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | 0.137 | 🔺 Rising |
| 2026-05-25 03:08:17 | Putupaula (Kalu Ganga) | 3.22 | 🟡 Alert | -0.010 |  |
| 2026-05-25 05:05:52 | Hanwella (Kelani Ganga) | 4.98 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-25 05:06:43 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-25 05:13:50 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-25 05:08:24 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-25 05:00:33 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 05:03:08 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 05:05:34 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 18:00:57 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:00:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:02:46 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:02:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:50 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:18:14 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:04:15 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:00:13 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:01:04 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:21:56 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:01:55 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:02:23 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 05:09:26 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-25 05:00:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-25 05:02:10 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-25 05:03:18 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.018 |  |
| 2026-05-25 05:04:07 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-05-25 05:02:21 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-05-25 05:04:33 | Ellagawa (Kalu Ganga) | 9.20 | 🟢 Normal | -0.029 |  |
| 2026-05-25 05:04:11 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-05-25 05:02:56 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-05-25 05:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.058 |  |
| 2026-05-25 05:00:43 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.061 |  |
| 2026-05-25 05:05:48 | Deraniyagala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.065 |  |
| 2026-05-25 05:03:21 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.070 |  |
| 2026-05-25 05:24:24 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.101 |  |
| 2026-05-25 05:16:55 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | -0.107 |  |
| 2026-05-25 05:10:45 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.113 |  |
| 2026-05-25 05:02:27 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)