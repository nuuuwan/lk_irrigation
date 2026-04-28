# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_02:38:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,803 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 02:38:25 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:38:18 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:29:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.088 |  |
| 2026-04-29 02:19:40 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:15:23 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-29 02:14:38 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.008 |  |
| 2026-04-29 02:14:08 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.025 |  |
| 2026-04-29 02:10:15 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-04-29 02:10:00 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-29 02:08:44 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.093 |  |
| 2026-04-29 02:08:08 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:06:52 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.028 |  |
| 2026-04-29 02:06:50 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.050 |  |
| 2026-04-29 02:03:51 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:03:42 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:03:20 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-04-29 02:03:16 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-29 02:03:13 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.058 |  |
| 2026-04-29 02:02:42 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:02:40 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:02:10 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-29 02:02:09 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:02:09 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-29 02:02:04 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:02:00 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:01:54 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.138 |  |
| 2026-04-29 02:01:38 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:01:38 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-29 02:01:29 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:00:20 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:00:20 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.120 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 02:02:10 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-29 02:01:38 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-28 21:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-29 02:10:00 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-29 01:01:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 18:04:58 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 02:15:23 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 02:03:16 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-29 02:02:42 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-29 01:27:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:02:04 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-29 00:08:33 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:38:25 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:00:20 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:02:09 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:01:29 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:01:38 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:38:18 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:03:51 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:08:08 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:02:00 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-29 02:14:38 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.008 |  |
| 2026-04-29 02:10:15 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-04-29 01:06:16 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-29 00:03:00 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-29 02:03:20 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-04-29 00:01:51 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-28 23:26:48 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.014 |  |
| 2026-04-29 02:14:08 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.025 |  |
| 2026-04-29 02:06:52 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.028 |  |
| 2026-04-29 02:06:50 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.050 |  |
| 2026-04-29 02:03:13 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.058 |  |
| 2026-04-29 02:29:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.088 |  |
| 2026-04-29 02:08:44 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.093 |  |
| 2026-04-29 02:00:20 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.120 |  |
| 2026-04-29 02:01:54 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.138 |  |
| 2026-04-29 01:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.268 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)