# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_21:11:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,216 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 21:11:34 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.009 |  |
| 2026-02-23 21:10:19 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.028 |  |
| 2026-02-23 21:09:51 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.028 |  |
| 2026-02-23 21:09:44 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.110 |  |
| 2026-02-23 21:07:56 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.143 |  |
| 2026-02-23 21:06:35 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | -15.882 |  |
| 2026-02-23 21:06:24 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.047 |  |
| 2026-02-23 21:05:27 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -15.882 |  |
| 2026-02-23 21:05:16 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:04:32 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-23 21:04:23 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-02-23 21:04:04 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:03:48 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:03:46 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:03:42 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-02-23 21:03:30 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:03:25 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:03:17 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-23 21:03:16 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:03:15 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-02-23 21:03:11 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-02-23 21:02:57 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:02:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-23 21:02:44 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-02-23 21:02:28 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-02-23 21:02:15 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:02:05 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-02-23 21:01:52 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:01:21 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:01:13 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.103 |  |
| 2026-02-23 21:00:37 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-02-23 21:00:21 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 20:42:05 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -15.882 |  |
| 2026-02-23 20:25:58 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 21:00:37 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-02-23 21:03:42 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-02-23 21:03:17 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-23 21:00:21 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:01:52 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:01:21 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:03:48 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:02:57 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:03:30 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:02:15 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:04:04 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:03:46 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:03:16 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:07:56 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:05:16 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:43 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:03:25 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-23 20:07:38 | Padiyathalawa (Maduru Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-02-23 21:11:34 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.009 |  |
| 2026-02-23 21:02:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-23 21:02:05 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-02-23 21:04:32 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-23 21:03:11 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-02-23 20:11:22 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.015 |  |
| 2026-02-23 20:25:58 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.016 |  |
| 2026-02-23 21:02:28 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-02-23 21:03:15 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-02-23 18:03:52 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.028 |  |
| 2026-02-23 21:10:19 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.028 |  |
| 2026-02-23 21:09:51 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.028 |  |
| 2026-02-23 21:02:44 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-02-23 21:06:24 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.047 |  |
| 2026-02-23 21:04:23 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-02-23 21:01:13 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.103 |  |
| 2026-02-23 21:09:44 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.110 |  |
| 2026-02-23 21:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.143 |  |
| 2026-02-23 21:06:35 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | -15.882 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)