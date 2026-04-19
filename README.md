# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_01:39:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,740 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 01:39:31 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:18:45 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:18:43 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.018 |  |
| 2026-04-20 01:17:34 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-04-20 01:15:57 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:08:30 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:07:41 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:06:07 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:04:34 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.023 |  |
| 2026-04-20 01:04:28 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 1.065 | 🔺 Rising |
| 2026-04-20 01:04:24 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-04-20 01:04:14 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-20 01:04:10 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-20 01:03:50 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.050 |  |
| 2026-04-20 01:03:44 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-20 01:03:22 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-20 01:03:12 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:03:10 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:02:46 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.071 |  |
| 2026-04-20 01:02:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-04-20 01:02:33 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:02:20 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.066 |  |
| 2026-04-20 01:01:47 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:01:39 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:01:17 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-04-20 01:01:08 | Panadugama (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.955 |  |
| 2026-04-20 01:00:56 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:00:32 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 01:04:28 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 1.065 | 🔺 Rising |
| 2026-04-20 01:04:24 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-04-20 01:03:44 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-19 18:00:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-20 01:04:10 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-20 00:01:13 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:00:56 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:03:10 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:01:39 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:39:31 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:03:12 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:18:45 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-20 00:02:57 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 00:01:15 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:07:41 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-20 00:02:42 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:15:57 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:01:47 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 00:20:52 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-20 00:03:52 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:06:07 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:02:33 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-20 01:17:34 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-04-20 01:03:22 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-20 01:04:14 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-20 01:00:32 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-19 21:20:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.017 |  |
| 2026-04-20 01:18:43 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.018 |  |
| 2026-04-20 01:01:17 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-04-20 01:04:34 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.023 |  |
| 2026-04-20 01:02:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-04-20 00:28:21 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-04-20 01:03:50 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.050 |  |
| 2026-04-20 01:02:20 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.066 |  |
| 2026-04-19 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.068 |  |
| 2026-04-20 01:02:46 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.071 |  |
| 2026-04-20 00:04:43 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.110 |  |
| 2026-04-20 01:01:08 | Panadugama (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.955 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)