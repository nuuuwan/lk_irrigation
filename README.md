# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_02:05:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,663 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 02:05:12 | Moragaswewa (Deduru Oya) | 2.46 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-05-09 02:04:40 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-09 02:04:21 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.100 |  |
| 2026-05-09 02:04:07 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 02:03:02 | Glencourse (Kelani Ganga) | 10.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-09 02:02:34 | Moraketiya (Walawe Ganga) | 2.34 | 🟢 Normal | -0.173 |  |
| 2026-05-09 02:02:17 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-09 02:02:13 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.109 |  |
| 2026-05-09 02:02:09 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.197 |  |
| 2026-05-09 02:01:31 | Kuda Oya (Kirindi Oya) | 6.20 | 🟢 Normal | -0.489 |  |
| 2026-05-09 02:01:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-09 02:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 02:01:08 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 02:01:07 | Thaldena (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.073 |  |
| 2026-05-09 02:00:45 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-09 01:41:51 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-09 01:30:17 | Norwood (Kelani Ganga) | 0.28 | 🟢 Normal | -0.729 |  |
| 2026-05-09 01:17:35 | Wellawaya (Kirindi Oya) | 2.95 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 01:05:43 | Thanamalwila (Kirindi Oya) | 6.51 | 🔴 Major Flood | 0.210 | 🔺 Rising |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-09 01:02:20 | Rathnapura (Kalu Ganga) | 3.38 | 🟢 Normal | 0.371 | 🔺 Rising |
| 2026-05-09 00:12:12 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-05-09 02:05:12 | Moragaswewa (Deduru Oya) | 2.46 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-05-09 01:07:03 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-05-09 02:01:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-08 23:34:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-09 02:03:02 | Glencourse (Kelani Ganga) | 10.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-09 02:04:07 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 02:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 02:04:40 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-09 02:01:08 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 01:02:13 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 01:03:42 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 23:01:55 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-09 00:03:06 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-09 01:07:23 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:00:45 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-09 01:41:51 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-09 01:01:09 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-09 01:04:03 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-09 02:02:17 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-09 00:08:05 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | -0.019 |  |
| 2026-05-09 00:01:45 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-05-09 01:01:04 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.023 |  |
| 2026-05-09 00:10:38 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.036 |  |
| 2026-05-09 01:17:35 | Wellawaya (Kirindi Oya) | 2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-09 01:04:39 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.041 |  |
| 2026-05-09 02:01:07 | Thaldena (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.073 |  |
| 2026-05-09 02:04:21 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.100 |  |
| 2026-05-09 01:09:08 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.104 |  |
| 2026-05-09 02:02:13 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.109 |  |
| 2026-05-09 02:02:34 | Moraketiya (Walawe Ganga) | 2.34 | 🟢 Normal | -0.173 |  |
| 2026-05-09 02:02:09 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.197 |  |
| 2026-05-09 02:01:31 | Kuda Oya (Kirindi Oya) | 6.20 | 🟢 Normal | -0.489 |  |
| 2026-05-09 01:30:17 | Norwood (Kelani Ganga) | 0.28 | 🟢 Normal | -0.729 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)