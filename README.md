# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_01:06:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,379 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 01:06:25 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.047 |  |
| 2026-05-29 01:06:08 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.112 |  |
| 2026-05-29 01:05:58 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 01:05:57 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-29 01:05:53 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:05:05 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:04:55 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-29 01:04:40 | Rathnapura (Kalu Ganga) | 5.34 | 🟡 Alert | -0.072 |  |
| 2026-05-29 01:03:39 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:03:39 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:03:30 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-29 01:03:30 | Hanwella (Kelani Ganga) | 3.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-29 01:03:04 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-29 01:02:42 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.023 |  |
| 2026-05-29 01:02:17 | Ellagawa (Kalu Ganga) | 8.51 | 🟢 Normal | -0.010 |  |
| 2026-05-29 01:02:13 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-29 01:02:08 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:02:05 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:01:36 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.031 |  |
| 2026-05-29 01:01:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-29 01:01:09 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-29 01:00:57 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 00:07:29 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.062 | 🔺 Rising |
| 2026-05-29 00:14:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-05-29 00:02:10 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | -0.032 |  |
| 2026-05-29 01:04:40 | Rathnapura (Kalu Ganga) | 5.34 | 🟡 Alert | -0.072 |  |
| 2026-05-29 01:04:55 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-29 00:01:31 | Deraniyagala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-29 00:09:05 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-29 01:03:30 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-29 01:05:57 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-29 01:01:09 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-29 01:03:30 | Hanwella (Kelani Ganga) | 3.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-29 00:00:33 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-29 00:05:44 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-29 01:02:13 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-29 01:05:58 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 00:07:24 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-29 00:05:57 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-29 01:02:05 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:53 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:05:05 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:00:57 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:03:10 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:03:39 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:08:03 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:02:08 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:03:39 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:05:53 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:04:14 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:02:12 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:02:17 | Ellagawa (Kalu Ganga) | 8.51 | 🟢 Normal | -0.010 |  |
| 2026-05-29 01:01:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-29 01:03:04 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-28 18:32:56 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.013 |  |
| 2026-05-29 01:02:42 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.023 |  |
| 2026-05-29 01:01:36 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.031 |  |
| 2026-05-29 01:06:25 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.047 |  |
| 2026-05-29 00:08:02 | Nawalapitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.047 |  |
| 2026-05-29 00:05:44 | Thawalama (Gin Ganga) | 3.35 | 🟢 Normal | -0.083 |  |
| 2026-05-29 01:06:08 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)