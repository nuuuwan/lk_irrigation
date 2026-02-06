# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_05:27:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,337 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 05:27:14 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:16:44 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-06 05:15:07 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-02-06 05:12:17 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.009 |  |
| 2026-02-06 05:11:18 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.012 |  |
| 2026-02-06 05:07:53 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 05:06:56 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.043 |  |
| 2026-02-06 05:06:13 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:05:09 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:04:54 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-02-06 05:04:18 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-06 05:03:32 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:03:25 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.068 |  |
| 2026-02-06 05:03:23 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:03:20 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.368 | 🔺 Rising |
| 2026-02-06 05:03:15 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:03:07 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 05:02:50 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:02:30 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-02-06 05:02:29 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-06 05:02:25 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:02:14 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.136 |  |
| 2026-02-06 05:01:51 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.012 |  |
| 2026-02-06 05:01:36 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-06 05:01:26 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 05:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:00:57 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.707 | 🔺 Rising |
| 2026-02-06 05:00:42 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-06 04:51:37 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.707 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 05:00:57 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.707 | 🔺 Rising |
| 2026-02-06 05:03:20 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.368 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 05:02:29 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-06 05:01:36 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-06 05:07:53 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 05:01:26 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 05:03:07 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 05:16:44 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-06 05:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:03:23 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:02:25 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:06:13 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:02:50 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:00:42 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:03:15 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:27:14 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:05:09 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:04:13 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:03:32 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-06 04:04:11 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-06 05:12:17 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.009 |  |
| 2026-02-06 05:15:07 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-02-06 05:04:18 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-06 04:03:21 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-02-06 05:02:30 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:05:46 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-06 05:11:18 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.012 |  |
| 2026-02-06 05:01:51 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.012 |  |
| 2026-02-06 05:04:54 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-02-06 05:06:56 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.043 |  |
| 2026-02-05 18:05:45 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.046 |  |
| 2026-02-06 05:03:25 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.068 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 03:06:30 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | -0.085 |  |
| 2026-02-06 05:02:14 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.136 |  |
| 2026-02-06 03:10:29 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -2.323 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)