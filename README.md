# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_07:20:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,985 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 07:20:53 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-29 07:19:56 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.016 |  |
| 2026-04-29 07:19:39 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.045 |  |
| 2026-04-29 07:16:23 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:16:02 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:12:16 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.042 |  |
| 2026-04-29 07:11:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.069 |  |
| 2026-04-29 07:08:37 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.036 |  |
| 2026-04-29 07:08:05 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 07:07:23 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.027 |  |
| 2026-04-29 07:06:52 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:06:47 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-04-29 07:06:46 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 07:06:00 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:04:47 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-29 07:04:23 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 07:04:09 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:03:31 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | -0.005 |  |
| 2026-04-29 07:03:26 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.039 |  |
| 2026-04-29 07:03:22 | Glencourse (Kelani Ganga) | 9.07 | 🟢 Normal | -0.030 |  |
| 2026-04-29 07:03:02 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.139 |  |
| 2026-04-29 07:02:40 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-29 07:02:29 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.129 |  |
| 2026-04-29 07:02:29 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:02:28 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:02:21 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-04-29 07:02:19 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:02:09 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:01:49 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-29 07:01:25 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.071 |  |
| 2026-04-29 07:01:20 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:01:07 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 07:01:05 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-29 07:00:54 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-29 07:00:43 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-04-29 07:00:15 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:33:19 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 07:02:21 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-04-29 07:00:54 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-29 07:01:07 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 07:04:23 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 07:08:05 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 07:06:46 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 07:20:53 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-29 07:02:19 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:16:02 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:01:49 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:16:23 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:02:28 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:04:09 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:02:29 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:04:10 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:06:00 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:00:15 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:02:09 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:01:20 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:06:52 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:03:31 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | -0.005 |  |
| 2026-04-29 07:06:47 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-04-29 07:04:47 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-29 07:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-29 07:01:05 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-29 07:02:40 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-29 05:00:56 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-29 07:19:56 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.016 |  |
| 2026-04-29 07:00:43 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-04-29 07:07:23 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.027 |  |
| 2026-04-29 07:03:22 | Glencourse (Kelani Ganga) | 9.07 | 🟢 Normal | -0.030 |  |
| 2026-04-29 07:08:37 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.036 |  |
| 2026-04-29 07:03:26 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.039 |  |
| 2026-04-29 07:12:16 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.042 |  |
| 2026-04-29 07:19:39 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.045 |  |
| 2026-04-29 07:11:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.069 |  |
| 2026-04-29 07:01:25 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.071 |  |
| 2026-04-29 07:02:29 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.129 |  |
| 2026-04-29 07:03:02 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)