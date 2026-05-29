# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_19:27:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,069 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 19:27:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-29 19:21:31 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.030 |  |
| 2026-05-29 19:18:33 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.033 |  |
| 2026-05-29 19:16:22 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:10:51 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:10:46 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-05-29 19:10:14 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-29 19:08:21 | Rathnapura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.104 |  |
| 2026-05-29 19:08:17 | Magura (Kalu Ganga) | 4.02 | 🟡 Alert | -0.060 |  |
| 2026-05-29 19:07:30 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:06:11 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-05-29 19:05:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-05-29 19:05:30 | Ellagawa (Kalu Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-05-29 19:05:02 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-29 19:04:58 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-05-29 19:04:39 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-29 19:03:40 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-05-29 19:03:37 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:03:27 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:03:20 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-29 19:03:16 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:02:52 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:02:40 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-05-29 19:02:39 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | -0.022 |  |
| 2026-05-29 19:02:35 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:02:34 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.072 |  |
| 2026-05-29 19:02:32 | Hanwella (Kelani Ganga) | 3.55 | 🟢 Normal | -0.051 |  |
| 2026-05-29 19:02:32 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:02:32 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 19:27:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-29 19:08:17 | Magura (Kalu Ganga) | 4.02 | 🟡 Alert | -0.060 |  |
| 2026-05-29 19:10:46 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-05-29 19:05:02 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-29 19:10:14 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-29 19:03:16 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:00:31 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:00:43 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:07:30 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:00:34 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:04:21 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:02:32 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:02:52 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:01:41 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:03:27 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:16:22 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:03:37 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:02:32 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:00:56 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:01:26 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:10:51 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:02:35 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-29 19:04:39 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-29 19:03:40 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-05-29 19:03:20 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-29 19:02:40 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-05-29 19:05:30 | Ellagawa (Kalu Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-05-29 19:02:23 | Baddegama (Gin Ganga) | 3.31 | 🟢 Normal | -0.020 |  |
| 2026-05-29 19:02:39 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | -0.022 |  |
| 2026-05-29 19:06:11 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-05-29 19:21:31 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.030 |  |
| 2026-05-29 19:05:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-05-29 19:18:33 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.033 |  |
| 2026-05-29 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.034 |  |
| 2026-05-29 19:04:58 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-05-29 19:02:32 | Hanwella (Kelani Ganga) | 3.55 | 🟢 Normal | -0.051 |  |
| 2026-05-29 19:02:25 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.066 |  |
| 2026-05-29 19:02:34 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.072 |  |
| 2026-05-29 19:08:21 | Rathnapura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)