# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_23:14:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **214,440 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-23 23:14:48 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-07-23 23:11:32 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:08:52 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:06:36 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:05:53 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-23 23:05:37 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:05:35 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -1.019 |  |
| 2026-07-23 23:04:25 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-07-23 23:03:41 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:03:32 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-23 23:03:31 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:03:25 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.049 |  |
| 2026-07-23 23:03:18 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:03:04 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:02:35 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:02:28 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:02:24 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:01:22 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:01:22 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.093 |  |
| 2026-07-23 23:01:20 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.022 |  |
| 2026-07-23 23:01:08 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:00:45 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-07-23 23:00:31 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-23 23:00:28 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:00:26 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-23 22:52:03 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-23 22:51:34 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-23 22:33:15 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.043 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-23 23:04:25 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-07-23 23:05:53 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-23 23:14:48 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-07-23 23:03:32 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-23 23:00:31 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-23 23:00:26 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:01:22 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:02:24 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-23 22:01:45 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:03:04 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:00:45 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-23 18:04:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-23 22:00:11 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:05:37 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 22:02:30 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:06:36 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:08:52 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-07-23 22:03:41 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-23 22:06:14 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:01:08 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-23 22:00:05 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-23 21:02:38 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:11:32 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:03:18 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:02:28 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:00:28 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-23 22:01:09 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-23 18:01:54 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:02:35 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:03:41 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 21:06:43 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:03:31 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-23 20:53:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-23 23:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-07-23 23:01:20 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.022 |  |
| 2026-07-23 23:03:25 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.049 |  |
| 2026-07-23 23:01:22 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.093 |  |
| 2026-07-23 23:05:35 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -1.019 |  |
| 2026-07-23 18:06:44 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)