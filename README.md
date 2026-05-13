# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_23:10:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,081 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 23:10:22 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.116 |  |
| 2026-05-13 23:10:15 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.097 |  |
| 2026-05-13 23:09:30 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-05-13 23:09:28 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-13 23:08:47 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.028 |  |
| 2026-05-13 23:08:26 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.056 |  |
| 2026-05-13 23:07:30 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-13 23:06:51 | Moraketiya (Walawe Ganga) | 1.92 | 🟢 Normal | -0.046 |  |
| 2026-05-13 23:06:39 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:06:05 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:05:43 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 23:05:35 | Rathnapura (Kalu Ganga) | 5.62 | 🟡 Alert | -0.131 |  |
| 2026-05-13 23:05:33 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.028 |  |
| 2026-05-13 23:05:28 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-05-13 23:04:55 | Moragaswewa (Deduru Oya) | 2.70 | 🟢 Normal | -0.076 |  |
| 2026-05-13 23:04:38 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-13 23:04:01 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.137 |  |
| 2026-05-13 23:03:50 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.050 |  |
| 2026-05-13 23:03:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-13 23:03:43 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:03:34 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.018 |  |
| 2026-05-13 23:03:00 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.250 |  |
| 2026-05-13 23:02:32 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-05-13 23:02:29 | Magura (Kalu Ganga) | 5.11 | 🟡 Alert | -0.030 |  |
| 2026-05-13 23:02:20 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.050 |  |
| 2026-05-13 23:02:10 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.031 |  |
| 2026-05-13 23:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-05-13 23:01:50 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-13 23:01:36 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:01:25 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:01:01 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.032 |  |
| 2026-05-13 23:00:35 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:00:00 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 20:09:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.86 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-05-13 23:02:32 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-05-13 23:02:29 | Magura (Kalu Ganga) | 5.11 | 🟡 Alert | -0.030 |  |
| 2026-05-13 23:10:15 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.097 |  |
| 2026-05-13 23:05:35 | Rathnapura (Kalu Ganga) | 5.62 | 🟡 Alert | -0.131 |  |
| 2026-05-13 23:03:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-13 23:09:28 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-13 23:04:38 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-13 23:05:43 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 23:07:30 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 23:06:05 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:01:44 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:01:25 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:00:35 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:06:39 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:19:38 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:00:00 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:01:36 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:03:43 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:09:30 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-05-13 23:01:50 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-13 23:03:34 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.018 |  |
| 2026-05-13 23:05:28 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-05-13 23:08:47 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.028 |  |
| 2026-05-13 23:05:33 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.028 |  |
| 2026-05-13 23:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-05-13 23:02:10 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.031 |  |
| 2026-05-13 23:01:01 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.032 |  |
| 2026-05-13 23:06:51 | Moraketiya (Walawe Ganga) | 1.92 | 🟢 Normal | -0.046 |  |
| 2026-05-13 23:03:50 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.050 |  |
| 2026-05-13 23:02:20 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.050 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-13 23:08:26 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.056 |  |
| 2026-05-13 23:04:55 | Moragaswewa (Deduru Oya) | 2.70 | 🟢 Normal | -0.076 |  |
| 2026-05-13 23:10:22 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.116 |  |
| 2026-05-13 23:04:01 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.137 |  |
| 2026-05-13 23:03:00 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.250 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)