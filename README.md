# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_05:02:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,007 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 05:02:33 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-28 05:02:30 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 05:02:23 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.061 |  |
| 2026-04-28 05:02:15 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 05:02:10 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.050 |  |
| 2026-04-28 05:02:09 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-04-28 05:02:01 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-28 05:01:46 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.040 |  |
| 2026-04-28 05:01:08 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-04-28 05:01:04 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-28 05:00:57 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-28 05:00:55 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-28 05:00:10 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.047 |  |
| 2026-04-28 04:57:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-28 04:34:50 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.047 |  |
| 2026-04-28 04:26:16 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-28 04:15:31 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.037 |  |
| 2026-04-28 04:13:47 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.050 |  |
| 2026-04-28 04:12:52 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-28 04:09:42 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 04:02:58 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.417 | 🔺 Rising |
| 2026-04-28 04:01:41 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-28 05:02:33 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-28 05:00:55 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-28 04:02:52 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-28 04:05:42 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-28 04:57:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-28 04:05:46 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-28 03:01:20 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 04:26:16 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 04:06:33 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-28 05:02:30 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:01:46 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 05:02:15 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:36 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 05:01:04 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-28 04:08:14 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-28 05:00:57 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-28 04:03:44 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.005 |  |
| 2026-04-28 05:02:09 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-04-28 04:05:02 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-28 05:02:01 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-28 04:07:58 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.013 |  |
| 2026-04-28 05:01:08 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-04-28 04:03:23 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-04-28 04:09:42 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.027 |  |
| 2026-04-28 04:15:31 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.037 |  |
| 2026-04-28 05:01:46 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.040 |  |
| 2026-04-28 04:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.040 |  |
| 2026-04-28 03:14:14 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.042 |  |
| 2026-04-28 05:00:10 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.047 |  |
| 2026-04-28 05:02:10 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.050 |  |
| 2026-04-28 04:06:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.061 |  |
| 2026-04-28 05:02:23 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.061 |  |
| 2026-04-28 04:07:16 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.167 |  |
| 2026-04-28 03:18:19 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -6.207 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)