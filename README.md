# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_02:30:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,329 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 02:30:59 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-15 02:28:02 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.014 |  |
| 2026-04-15 02:25:54 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.209 |  |
| 2026-04-15 02:25:30 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:15:04 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.005 |  |
| 2026-04-15 02:14:35 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:13:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 4.065 | 🔺 Rising |
| 2026-04-15 02:12:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 4.065 | 🔺 Rising |
| 2026-04-15 02:11:30 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-15 02:10:33 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-15 02:08:48 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:05:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:05:08 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-15 02:05:08 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:04:35 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-15 02:04:34 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:04:20 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:04:19 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:04:05 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.163 |  |
| 2026-04-15 02:03:35 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.007 |  |
| 2026-04-15 02:03:33 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:03:30 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:03:26 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:03:17 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-15 02:02:59 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:02:28 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.040 |  |
| 2026-04-15 02:02:20 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-15 02:02:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:01:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-15 02:01:46 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-04-15 02:01:36 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.030 |  |
| 2026-04-15 02:01:15 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:53:40 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-15 01:53:07 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-15 01:53:05 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.105 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 02:13:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 4.065 | 🔺 Rising |
| 2026-04-15 02:01:46 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-04-15 02:05:08 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-15 02:11:30 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-15 02:01:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-15 02:10:33 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-15 01:01:08 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 02:30:59 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-15 00:19:42 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:03:26 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:05:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:03:33 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:25:30 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:06:36 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:05:10 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:08:48 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:14:35 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:02:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:05:08 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:00:30 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:03:30 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:01:15 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:02:59 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:04:19 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:04:34 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:15:04 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.005 |  |
| 2026-04-15 02:03:35 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.007 |  |
| 2026-04-15 02:03:17 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-15 02:02:20 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-15 02:28:02 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.014 |  |
| 2026-04-15 00:19:27 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.018 |  |
| 2026-04-15 02:04:35 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-15 02:01:36 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.030 |  |
| 2026-04-15 02:02:28 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.040 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-15 02:04:05 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.163 |  |
| 2026-04-15 02:25:54 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.209 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)