# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_07:17:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,214 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 07:17:06 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-27 07:12:45 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.027 |  |
| 2026-04-27 07:08:07 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:07:51 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.195 |  |
| 2026-04-27 07:07:49 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.018 |  |
| 2026-04-27 07:05:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:05:36 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:05:24 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-04-27 07:04:51 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-27 07:04:34 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-27 07:04:24 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:04:21 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:04:21 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.047 |  |
| 2026-04-27 07:04:08 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:04:05 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:04:04 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-27 07:03:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-04-27 07:03:28 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.010 |  |
| 2026-04-27 07:03:28 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.039 |  |
| 2026-04-27 07:03:11 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-04-27 07:03:09 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:02:29 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-27 07:02:17 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.016 |  |
| 2026-04-27 07:02:14 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:02:08 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 07:01:54 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-27 07:01:54 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.151 |  |
| 2026-04-27 07:01:23 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-27 07:01:17 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.015 |  |
| 2026-04-27 07:01:10 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-27 07:01:00 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.107 |  |
| 2026-04-27 07:00:44 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:00:42 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:32:39 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 07:03:11 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-04-27 07:02:29 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-27 06:01:55 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-27 07:04:04 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-27 07:04:51 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-27 07:01:10 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-27 07:04:34 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-27 07:17:06 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-27 07:01:23 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-27 06:19:39 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-27 06:01:22 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 07:02:08 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 07:00:42 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:00:44 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:05:36 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:05:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:04:24 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:08:07 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:04:08 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:02:14 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:03:09 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:04:05 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 07:03:28 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.010 |  |
| 2026-04-27 07:01:54 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-27 07:01:17 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.015 |  |
| 2026-04-27 07:02:17 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.016 |  |
| 2026-04-27 07:07:49 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.018 |  |
| 2026-04-27 07:03:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-04-27 07:12:45 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.027 |  |
| 2026-04-27 06:00:54 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-04-27 07:05:24 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-04-27 07:03:28 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.039 |  |
| 2026-04-27 07:04:21 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.047 |  |
| 2026-04-27 07:01:00 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.107 |  |
| 2026-04-27 07:01:54 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.151 |  |
| 2026-04-27 07:07:51 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.195 |  |
| 2026-04-27 04:06:46 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)