# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_02:02:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,423 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 02:02:59 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-14 02:02:55 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 02:02:53 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-14 02:02:45 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-14 02:02:43 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-14 02:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-04-14 02:02:33 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-14 02:02:23 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-14 02:01:51 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-14 02:01:46 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 02:01:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-04-14 02:01:23 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -108.000 |  |
| 2026-04-14 02:01:22 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -108.000 |  |
| 2026-04-14 02:01:13 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 02:01:09 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.092 |  |
| 2026-04-14 02:00:48 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 02:00:14 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-14 01:59:46 | Katharagama (Menik Ganga) | 0.80 | 🟢 Normal | 1.103 | 🔺 Rising |
| 2026-04-14 01:46:31 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:37:30 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.007 |  |
| 2026-04-14 01:33:09 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-14 01:21:42 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 1.103 | 🔺 Rising |
| 2026-04-14 01:19:42 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.071 |  |
| 2026-04-14 01:19:40 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-04-14 01:16:35 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:14:21 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -684.000 |  |
| 2026-04-14 01:14:20 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -684.000 |  |
| 2026-04-14 01:14:19 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -684.000 |  |
| 2026-04-14 01:14:17 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -684.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 01:59:46 | Katharagama (Menik Ganga) | 0.80 | 🟢 Normal | 1.103 | 🔺 Rising |
| 2026-04-14 01:06:47 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.878 | 🔺 Rising |
| 2026-04-14 02:02:53 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-14 01:33:09 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-14 02:00:14 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-14 02:01:51 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-14 00:10:00 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-14 01:08:24 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-14 02:02:23 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-14 02:01:46 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 18:01:02 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 02:02:33 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:46:31 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:02:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 02:00:48 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:01:19 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-14 02:01:13 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 02:02:59 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:09:05 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 02:02:55 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:01:59 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:26:34 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.004 |  |
| 2026-04-14 01:37:30 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.007 |  |
| 2026-04-14 02:02:45 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-14 02:02:43 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-13 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |
| 2026-04-14 01:04:12 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-14 01:03:11 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-04-14 02:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-04-13 21:01:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.029 |  |
| 2026-04-14 02:01:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-04-14 00:04:28 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2026-04-14 01:01:11 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.033 |  |
| 2026-04-14 01:19:40 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-04-14 01:19:42 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.071 |  |
| 2026-04-14 01:02:40 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.078 |  |
| 2026-04-14 02:01:09 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.092 |  |
| 2026-04-14 02:01:23 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -108.000 |  |
| 2026-04-14 01:14:21 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -684.000 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)