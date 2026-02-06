# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_01:46:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,105 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 01:46:50 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:31:43 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.871 | 🔺 Rising |
| 2026-02-07 01:26:26 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-07 01:20:58 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-07 01:16:12 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 6.146 | 🔺 Rising |
| 2026-02-07 01:15:31 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 6.146 | 🔺 Rising |
| 2026-02-07 01:15:03 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-07 01:10:26 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:09:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-07 01:08:53 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-02-07 01:06:36 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:05:46 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-07 01:05:04 | Panadugama (Nilwala Ganga) | 0.00 | 🟢 Normal | -2.222 |  |
| 2026-02-07 01:04:45 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 01:04:43 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-07 01:04:39 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-07 01:04:24 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-02-07 01:03:50 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:03:37 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.051 |  |
| 2026-02-07 01:02:46 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:02:33 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:02:23 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:02:22 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-02-07 01:02:17 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.096 |  |
| 2026-02-07 01:02:17 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:01:51 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-02-07 01:01:47 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 01:16:12 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 6.146 | 🔺 Rising |
| 2026-02-07 01:31:43 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.871 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-07 01:05:46 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-07 00:01:07 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-07 01:04:43 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-07 00:01:15 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-07 01:20:58 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-07 01:09:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-07 01:26:26 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-07 01:04:45 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 01:01:47 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:46:50 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:02:46 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-07 00:05:09 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:03:50 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:57 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:06:36 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 00:11:45 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:02:23 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:02:33 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:02:17 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:10:26 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-07 00:08:21 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-02-07 01:15:03 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-07 00:03:05 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-07 01:04:39 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-07 00:01:55 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-07 01:08:53 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-02-07 01:02:22 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-02-07 01:01:51 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-07 01:04:24 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-02-07 01:03:37 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.051 |  |
| 2026-02-07 01:02:17 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.096 |  |
| 2026-02-07 01:05:04 | Panadugama (Nilwala Ganga) | 0.00 | 🟢 Normal | -2.222 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)