# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_02:04:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,405 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 02:04:50 | Rathnapura (Kalu Ganga) | 5.20 | 🟡 Alert | -0.140 |  |
| 2026-05-29 02:04:24 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-29 02:03:53 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 02:03:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:03:25 | Hanwella (Kelani Ganga) | 3.84 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-29 02:03:10 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:03:05 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:02:55 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-05-29 02:02:40 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-29 02:02:16 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-29 02:02:14 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:01:44 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:01:39 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:01:26 | Deraniyagala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.204 |  |
| 2026-05-29 02:01:22 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:01:18 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:01:17 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.010 |  |
| 2026-05-29 01:40:52 | Deraniyagala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.204 |  |
| 2026-05-29 01:38:23 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.204 |  |
| 2026-05-29 01:23:21 | Panadugama (Nilwala Ganga) | 5.08 | 🟡 Alert | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 01:23:21 | Panadugama (Nilwala Ganga) | 5.08 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-05-29 00:14:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-05-29 01:06:44 | Magura (Kalu Ganga) | 4.89 | 🟡 Alert | -0.028 |  |
| 2026-05-29 02:04:50 | Rathnapura (Kalu Ganga) | 5.20 | 🟡 Alert | -0.140 |  |
| 2026-05-29 01:07:36 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-29 02:02:16 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-29 01:04:55 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-29 02:03:25 | Hanwella (Kelani Ganga) | 3.84 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-29 02:04:24 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-29 01:05:57 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-29 02:02:40 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-29 00:05:44 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-29 01:05:58 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 00:05:57 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-29 02:03:53 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 02:01:39 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:03:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:01:22 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:53 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:01:44 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:03:10 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:03:05 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:03:10 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:08:03 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:02:14 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:03:39 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:05:53 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:08:55 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:02:12 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-29 01:11:09 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:01:17 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.010 |  |
| 2026-05-28 18:32:56 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.013 |  |
| 2026-05-29 02:02:55 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-05-29 01:01:36 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.031 |  |
| 2026-05-29 01:06:25 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.047 |  |
| 2026-05-29 01:06:41 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | -0.049 |  |
| 2026-05-29 01:06:08 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.112 |  |
| 2026-05-29 01:10:42 | Nawalapitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.153 |  |
| 2026-05-29 02:01:26 | Deraniyagala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)