# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_00:32:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,402 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 00:32:14 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-23 00:22:27 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.039 |  |
| 2026-04-23 00:19:04 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-23 00:12:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:12:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:10:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:07:57 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.039 |  |
| 2026-04-23 00:07:49 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-23 00:06:30 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:06:30 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -1.714 |  |
| 2026-04-23 00:06:09 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -1.714 |  |
| 2026-04-23 00:04:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-23 00:04:23 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.107 |  |
| 2026-04-23 00:04:05 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:03:59 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-04-23 00:03:45 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-23 00:03:37 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-04-23 00:03:37 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.048 |  |
| 2026-04-23 00:03:36 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.015 |  |
| 2026-04-23 00:03:35 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:03:19 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-23 00:02:55 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:02:50 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:02:26 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:02:16 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-23 00:02:13 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.039 |  |
| 2026-04-23 00:02:12 | Thanamalwila (Kirindi Oya) | 3.12 | 🟢 Normal | -0.428 |  |
| 2026-04-23 00:02:10 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:02:02 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.070 |  |
| 2026-04-23 00:01:58 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.099 |  |
| 2026-04-23 00:01:48 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:01:10 | Kuda Oya (Kirindi Oya) | 2.50 | 🟢 Normal | -0.211 |  |
| 2026-04-23 00:00:41 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-23 00:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.287 |  |
| 2026-04-22 23:59:53 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-22 23:51:49 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.039 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 23:18:07 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-04-23 00:03:37 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-04-23 00:00:41 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-23 00:02:16 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-22 23:59:53 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-23 00:03:45 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-23 00:03:19 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-23 00:19:04 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-23 00:04:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 23:05:44 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 00:32:14 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-23 00:07:49 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-23 00:03:35 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:02:50 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:02:26 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:06:30 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:02:10 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:01:48 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:04:05 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:12:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:52 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 23:05:49 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.012 |  |
| 2026-04-23 00:03:36 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.015 |  |
| 2026-04-23 00:03:59 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-04-22 22:00:50 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-04-23 00:07:57 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.039 |  |
| 2026-04-23 00:22:27 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.039 |  |
| 2026-04-23 00:02:13 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.039 |  |
| 2026-04-23 00:03:37 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.048 |  |
| 2026-04-23 00:02:02 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.070 |  |
| 2026-04-23 00:01:58 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.099 |  |
| 2026-04-23 00:04:23 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.107 |  |
| 2026-04-22 23:02:25 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.168 |  |
| 2026-04-23 00:01:10 | Kuda Oya (Kirindi Oya) | 2.50 | 🟢 Normal | -0.211 |  |
| 2026-04-23 00:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.287 |  |
| 2026-04-23 00:02:12 | Thanamalwila (Kirindi Oya) | 3.12 | 🟢 Normal | -0.428 |  |
| 2026-04-23 00:06:30 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -1.714 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)