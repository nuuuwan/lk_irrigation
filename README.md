# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_03:40:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,479 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 03:40:32 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:16:00 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-14 03:14:34 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-14 03:14:33 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-14 03:13:52 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.045 |  |
| 2026-04-14 03:11:50 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:09:33 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-14 03:07:41 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -72.000 |  |
| 2026-04-14 03:07:40 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -72.000 |  |
| 2026-04-14 03:07:39 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -72.000 |  |
| 2026-04-14 03:07:32 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-14 03:07:28 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.019 |  |
| 2026-04-14 03:06:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:06:12 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:06:06 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-04-14 03:05:23 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | -216.000 |  |
| 2026-04-14 03:05:22 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -216.000 |  |
| 2026-04-14 03:04:54 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:04:51 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-04-14 03:04:37 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:04:02 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.132 |  |
| 2026-04-14 03:03:46 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.113 |  |
| 2026-04-14 03:03:40 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-14 03:03:24 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:03:17 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | -0.094 |  |
| 2026-04-14 03:02:47 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-04-14 03:02:43 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 03:02:20 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:02:11 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-04-14 03:01:49 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:01:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-04-14 03:01:37 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-14 03:01:26 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.020 |  |
| 2026-04-14 03:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.021 |  |
| 2026-04-14 03:01:04 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:00:45 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.131 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 03:14:34 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-14 03:02:47 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-04-14 03:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-04-14 01:33:09 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-14 03:16:00 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-14 03:01:37 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-14 03:02:43 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 03:09:33 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-14 02:01:46 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 18:01:02 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 03:06:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:04:54 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:02:20 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:01:19 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:04:37 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:06:12 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:11:50 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:03:24 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:01:04 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:40:32 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:02:11 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:07:32 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-14 02:02:43 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-13 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |
| 2026-04-14 03:03:40 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-14 03:07:28 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.019 |  |
| 2026-04-14 03:06:06 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-04-14 03:01:26 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.020 |  |
| 2026-04-14 03:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.021 |  |
| 2026-04-14 03:01:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-04-14 03:04:51 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-04-14 03:13:52 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.045 |  |
| 2026-04-14 03:03:17 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | -0.094 |  |
| 2026-04-14 03:03:46 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.113 |  |
| 2026-04-14 03:00:45 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.131 |  |
| 2026-04-14 03:04:02 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.132 |  |
| 2026-04-14 03:07:41 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -72.000 |  |
| 2026-04-14 03:05:23 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | -216.000 |  |
| 2026-04-14 01:14:21 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -684.000 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)