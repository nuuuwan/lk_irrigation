# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_03:05:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,220 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 03:05:31 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | -0.056 |  |
| 2026-05-31 03:04:15 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.019 |  |
| 2026-05-31 03:04:00 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-05-31 03:03:50 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.025 |  |
| 2026-05-31 03:03:46 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:03:38 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.020 |  |
| 2026-05-31 03:03:34 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:03:17 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:03:02 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.052 |  |
| 2026-05-31 03:03:01 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:02:40 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:02:33 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:02:29 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.054 |  |
| 2026-05-31 03:01:30 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:01:23 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-31 03:01:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-31 03:00:58 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 02:39:28 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.025 |  |
| 2026-05-31 02:33:32 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-31 02:33:02 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-31 02:31:27 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-05-31 02:24:01 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.007 |  |
| 2026-05-31 02:18:51 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-31 02:17:54 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 02:17:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | -0.054 |  |
| 2026-05-31 02:17:07 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.062 |  |
| 2026-05-31 02:16:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 03:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.054 |  |
| 2026-05-31 02:02:50 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-31 03:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-31 03:00:58 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 03:01:23 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-31 03:03:01 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:00:56 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:01:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:01:30 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-31 02:16:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:03:34 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:02:33 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:02:40 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:09:18 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:03:17 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 02:17:54 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:03:46 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-31 02:05:24 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 02:03:51 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-31 01:02:44 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:02:29 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 02:24:01 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.007 |  |
| 2026-05-31 02:05:13 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-05-31 02:01:12 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-05-31 03:04:15 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.019 |  |
| 2026-05-31 02:02:22 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-05-31 03:03:38 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.020 |  |
| 2026-05-31 02:31:27 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-05-31 03:04:00 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-05-31 03:03:50 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.025 |  |
| 2026-05-31 02:14:22 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | -0.026 |  |
| 2026-05-31 02:06:19 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.029 |  |
| 2026-05-31 02:05:09 | Putupaula (Kalu Ganga) | 2.28 | 🟢 Normal | -0.035 |  |
| 2026-05-31 02:02:44 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.049 |  |
| 2026-05-31 03:03:02 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.052 |  |
| 2026-05-31 03:05:31 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | -0.056 |  |
| 2026-05-31 02:17:07 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)