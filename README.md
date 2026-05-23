# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_01:16:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,093 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 01:16:02 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.008 |  |
| 2026-05-24 01:08:29 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-05-24 01:07:54 | Hanwella (Kelani Ganga) | 5.38 | 🟢 Normal | -0.085 |  |
| 2026-05-24 01:07:15 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:06:34 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:06:04 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:05:41 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:04:29 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.023 |  |
| 2026-05-24 01:04:17 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:04:10 | Putupaula (Kalu Ganga) | 3.25 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-05-24 01:03:50 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:03:30 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-24 01:03:13 | Ellagawa (Kalu Ganga) | 10.17 | 🟡 Alert | -0.031 |  |
| 2026-05-24 01:03:05 | Rathnapura (Kalu Ganga) | 5.07 | 🟢 Normal | -0.071 |  |
| 2026-05-24 01:02:59 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-24 01:02:43 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-05-24 01:02:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:02:12 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-24 01:02:10 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.031 |  |
| 2026-05-24 01:02:05 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-24 01:01:52 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.040 |  |
| 2026-05-24 01:01:46 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:01:31 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-24 01:00:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 01:00:06 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 01:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-23 23:03:45 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | -0.074 |  |
| 2026-05-24 01:04:10 | Putupaula (Kalu Ganga) | 3.25 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-05-24 01:03:13 | Ellagawa (Kalu Ganga) | 10.17 | 🟡 Alert | -0.031 |  |
| 2026-05-24 01:02:12 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-24 01:01:31 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-24 01:00:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 01:00:06 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 00:01:09 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:01:46 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:04:23 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:06:04 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-24 00:05:12 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:07:15 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-24 00:02:36 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:04:17 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:06:34 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:03:50 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 00:09:44 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:05:41 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 00:00:53 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:02:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-24 00:22:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:03:30 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-24 01:16:02 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.008 |  |
| 2026-05-24 01:02:59 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-23 18:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-24 01:02:05 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-24 01:02:43 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-05-24 01:04:29 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.023 |  |
| 2026-05-24 01:08:29 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-05-24 01:02:10 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.031 |  |
| 2026-05-24 01:01:52 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.040 |  |
| 2026-05-24 00:05:10 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.040 |  |
| 2026-05-24 00:02:43 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.061 |  |
| 2026-05-24 01:03:05 | Rathnapura (Kalu Ganga) | 5.07 | 🟢 Normal | -0.071 |  |
| 2026-05-24 01:07:54 | Hanwella (Kelani Ganga) | 5.38 | 🟢 Normal | -0.085 |  |
| 2026-05-24 00:09:24 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.496 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)