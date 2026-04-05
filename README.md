# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_07:11:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,616 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 07:11:30 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.018 |  |
| 2026-04-05 07:11:21 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-05 07:10:12 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-04-05 07:09:32 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-04-05 07:07:56 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:06:48 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-05 07:06:43 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.117 |  |
| 2026-04-05 07:06:39 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-05 07:05:41 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.009 |  |
| 2026-04-05 07:05:30 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-05 07:05:28 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:05:25 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.031 |  |
| 2026-04-05 07:04:40 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-05 07:04:35 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-05 07:04:27 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 07:04:22 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.022 |  |
| 2026-04-05 07:03:44 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.068 |  |
| 2026-04-05 07:03:36 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 07:03:16 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:03:04 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.030 |  |
| 2026-04-05 07:02:51 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.024 |  |
| 2026-04-05 07:02:40 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-05 07:02:14 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-04-05 07:02:12 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.120 |  |
| 2026-04-05 07:02:09 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-04-05 07:01:46 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-05 07:01:43 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:01:41 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-04-05 07:01:33 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 07:01:17 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:00:42 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:00:34 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.054 |  |
| 2026-04-05 07:00:31 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-04-05 07:00:25 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-05 06:38:56 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 0.728 | 🔺 Rising |
| 2026-04-05 07:00:31 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-04-05 07:02:14 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-04-05 07:04:40 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-05 07:01:46 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-05 07:04:35 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-05 07:02:40 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-05 06:01:36 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-05 07:03:36 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 07:01:33 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 07:04:27 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 07:11:21 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-05 07:07:56 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:01:17 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:00:42 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:03:16 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:01:43 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:05:28 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:01:53 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:02:46 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:00:25 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:09:32 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-04-05 07:05:41 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.009 |  |
| 2026-04-05 07:10:12 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-04-05 07:06:48 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-05 07:06:39 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-05 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-05 07:05:30 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-05 07:11:30 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.018 |  |
| 2026-04-05 07:02:09 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-04-05 07:04:22 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.022 |  |
| 2026-04-05 07:02:51 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.024 |  |
| 2026-04-05 07:03:04 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.030 |  |
| 2026-04-05 07:05:25 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.031 |  |
| 2026-04-05 07:01:41 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-04-05 07:00:34 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.054 |  |
| 2026-04-05 07:03:44 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.068 |  |
| 2026-04-05 07:06:43 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.117 |  |
| 2026-04-05 07:02:12 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)