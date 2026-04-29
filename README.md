# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_15:29:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,312 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 15:29:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:12:43 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:10:10 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:09:10 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:07:47 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.047 |  |
| 2026-04-29 15:06:42 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:06:34 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:06:29 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-04-29 15:05:33 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:05:14 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 15:05:09 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.033 |  |
| 2026-04-29 15:04:59 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-29 15:04:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.124 |  |
| 2026-04-29 15:04:11 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-29 15:04:06 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 15:04:04 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-04-29 15:03:48 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.029 |  |
| 2026-04-29 15:03:46 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-04-29 15:03:39 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:03:29 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-29 15:03:22 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-04-29 15:03:16 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:03:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-04-29 15:02:54 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.101 |  |
| 2026-04-29 15:02:50 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.052 |  |
| 2026-04-29 15:02:48 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:02:47 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:02:28 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:02:27 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-04-29 15:02:27 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:02:26 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:02:23 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-29 15:01:52 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:01:47 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-04-29 15:01:11 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:00:32 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 14:58:10 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 6.923 | 🔺 Rising |
| 2026-04-29 14:57:44 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 6.923 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 14:58:10 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 6.923 | 🔺 Rising |
| 2026-04-29 15:03:29 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-29 15:02:23 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-29 15:04:11 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-29 15:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 15:04:06 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 15:05:14 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 15:02:26 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:02:10 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:29:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:01:52 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:03:39 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:05:33 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:02:47 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:06:42 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:01:11 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:12:43 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:10:10 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 15:06:29 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-04-29 15:03:16 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:02:28 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:02:48 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:00:32 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:03:46 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:09:10 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:02:27 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-04-29 15:03:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-04-29 15:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-04-29 15:04:59 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-29 15:01:47 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-04-29 15:03:22 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-04-29 15:02:27 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-04-29 15:04:04 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-04-29 15:03:48 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.029 |  |
| 2026-04-29 15:05:09 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.033 |  |
| 2026-04-29 15:07:47 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.047 |  |
| 2026-04-29 15:02:50 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.052 |  |
| 2026-04-29 15:02:54 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.101 |  |
| 2026-04-29 15:04:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)