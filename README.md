# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_02:15:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,929 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 02:15:58 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:15:30 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-28 02:11:22 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:06:36 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:06:01 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-28 02:05:46 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-28 02:05:45 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-28 02:05:32 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.059 |  |
| 2026-04-28 02:05:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:05:19 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-04-28 02:05:16 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:05:04 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-04-28 02:04:50 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-28 02:04:26 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:04:08 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 02:03:49 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-28 02:03:26 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 02:03:03 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 02:02:43 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.247 |  |
| 2026-04-28 02:02:34 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:02:20 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-28 02:02:19 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:02:16 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.041 |  |
| 2026-04-28 02:02:11 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-04-28 02:02:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.063 |  |
| 2026-04-28 02:02:01 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.055 |  |
| 2026-04-28 02:01:38 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:01:10 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.094 |  |
| 2026-04-28 02:01:09 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-28 02:00:50 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 01:57:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 3.857 | 🔺 Rising |
| 2026-04-28 01:56:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 3.857 | 🔺 Rising |
| 2026-04-28 01:33:43 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 01:57:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 3.857 | 🔺 Rising |
| 2026-04-28 02:02:11 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-04-28 02:05:45 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-28 02:01:09 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-28 02:06:01 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-28 02:03:49 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-28 02:04:08 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 02:15:30 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-28 02:00:50 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 02:03:26 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 02:03:03 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:05:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:02:45 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:04:26 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:11:22 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:01:38 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:05:16 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:02:19 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:15:58 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:02:34 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:06:19 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-28 02:05:04 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-04-28 01:07:26 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-28 02:05:46 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-28 02:04:50 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-28 02:02:20 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-28 02:05:19 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-04-28 02:02:16 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.041 |  |
| 2026-04-28 02:02:01 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.055 |  |
| 2026-04-28 02:05:32 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.059 |  |
| 2026-04-28 02:02:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.063 |  |
| 2026-04-28 01:17:25 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.065 |  |
| 2026-04-28 01:03:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.075 |  |
| 2026-04-28 02:01:10 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.094 |  |
| 2026-04-28 02:02:43 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.247 |  |
| 2026-04-28 01:12:41 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)