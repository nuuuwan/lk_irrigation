# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_11:06:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,258 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 11:06:23 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-28 11:06:23 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-04-28 11:06:09 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-04-28 11:04:41 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.088 |  |
| 2026-04-28 11:04:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 11:04:20 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-04-28 11:03:51 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.049 |  |
| 2026-04-28 11:03:47 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.105 |  |
| 2026-04-28 11:03:42 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:03:38 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.030 |  |
| 2026-04-28 11:03:25 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.050 |  |
| 2026-04-28 11:02:54 | Thanthirimale (Malwathu Oya) | 2.07 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-28 11:02:48 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.012 |  |
| 2026-04-28 11:02:40 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-28 11:02:29 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-04-28 11:02:23 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:02:19 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-28 11:02:11 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-28 11:02:01 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:02:01 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:01:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-04-28 11:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 11:01:35 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:01:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:01:27 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-04-28 11:01:10 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-28 11:00:49 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-28 11:00:40 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -36.000 |  |
| 2026-04-28 11:00:39 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -36.000 |  |
| 2026-04-28 11:00:36 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:00:22 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -36.000 |  |
| 2026-04-28 11:00:01 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-28 10:28:04 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-28 10:18:27 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 11:01:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-04-28 11:02:29 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-04-28 11:02:40 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-28 11:06:23 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-28 11:02:54 | Thanthirimale (Malwathu Oya) | 2.07 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-28 11:00:49 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-28 11:02:19 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-28 11:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 11:04:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 10:28:04 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-28 11:01:35 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:01:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:00:36 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-28 10:01:43 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:02:01 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:02:01 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:03:42 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:00:01 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:02:23 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-28 10:02:11 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 10:08:46 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-28 10:08:17 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-04-28 11:04:20 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-04-28 11:02:11 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-28 11:01:10 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-28 11:06:23 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-04-28 11:06:09 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-04-28 11:01:27 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-04-28 11:02:48 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.012 |  |
| 2026-04-28 10:02:41 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.023 |  |
| 2026-04-28 11:03:38 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.030 |  |
| 2026-04-28 11:03:51 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.049 |  |
| 2026-04-28 11:03:25 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.050 |  |
| 2026-04-28 10:04:06 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.081 |  |
| 2026-04-28 10:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.084 |  |
| 2026-04-28 11:04:41 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.088 |  |
| 2026-04-28 10:11:43 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.099 |  |
| 2026-04-28 11:03:47 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.105 |  |
| 2026-04-28 11:00:40 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)