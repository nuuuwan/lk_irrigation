# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_03:11:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,265 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 03:11:05 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-02-06 03:10:29 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -2.323 |  |
| 2026-02-06 03:09:58 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -2.323 |  |
| 2026-02-06 03:08:08 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:07:22 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-06 03:06:30 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | -0.085 |  |
| 2026-02-06 03:06:25 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-02-06 03:05:54 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-02-06 03:05:09 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 03:04:56 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 03:04:32 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -144.000 |  |
| 2026-02-06 03:04:31 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -144.000 |  |
| 2026-02-06 03:04:27 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -144.000 |  |
| 2026-02-06 03:04:18 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-02-06 03:03:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:03:33 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.199 |  |
| 2026-02-06 03:03:27 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:03:21 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-06 03:03:04 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:02:53 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:02:31 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-06 03:02:26 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:02:17 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-02-06 03:01:54 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.074 |  |
| 2026-02-06 03:01:28 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:01:26 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-02-06 03:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:59:26 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:57:24 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-06 02:21:16 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.074 |  |
| 2026-02-06 02:15:41 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 23:13:17 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-06 02:57:24 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 03:02:31 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-06 03:04:56 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 03:05:09 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 03:02:26 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:02:53 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 01:05:26 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:03:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:04:22 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:02:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:03:04 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:08:08 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:01:28 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:04:13 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-06 03:03:27 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-06 01:41:55 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.006 |  |
| 2026-02-06 03:11:05 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-02-06 03:03:21 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-06 03:05:54 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-02-06 03:07:22 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:05:46 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-06 03:06:25 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-02-06 03:04:18 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-02-06 03:02:17 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-02-06 03:01:26 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-02-06 02:15:41 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.032 |  |
| 2026-02-05 18:05:45 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.046 |  |
| 2026-02-06 02:03:43 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.049 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 03:01:54 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.074 |  |
| 2026-02-06 03:06:30 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | -0.085 |  |
| 2026-02-06 03:03:33 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.199 |  |
| 2026-02-06 03:10:29 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -2.323 |  |
| 2026-02-06 03:04:32 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)