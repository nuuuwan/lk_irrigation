# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_18:10:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,720 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 18:10:32 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.081 |  |
| 2026-01-03 18:08:58 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | 17.419 | 🔺 Rising |
| 2026-01-03 18:08:42 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.012 |  |
| 2026-01-03 18:08:22 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-01-03 18:07:56 | Galgamuwa (Mee Oya) | 2.21 | 🟢 Normal | 17.419 | 🔺 Rising |
| 2026-01-03 18:07:52 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.028 |  |
| 2026-01-03 18:07:20 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.016 |  |
| 2026-01-03 18:07:19 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-01-03 18:05:46 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:05:44 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-01-03 18:04:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.088 |  |
| 2026-01-03 18:04:36 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-01-03 18:04:34 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-01-03 18:04:22 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:04:14 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:03:44 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-03 18:03:39 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-01-03 18:03:37 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-03 18:03:34 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-03 18:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:03:25 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:03:20 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-01-03 18:03:07 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:03:01 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:02:59 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:02:51 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:02:26 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.021 |  |
| 2026-01-03 18:02:19 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-03 18:02:12 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:54 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:42 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-01-03 18:01:13 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:08 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:00:20 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:00:11 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.119 |  |
| 2026-01-03 17:48:13 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.081 |  |
| 2026-01-03 17:17:49 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 18:08:58 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | 17.419 | 🔺 Rising |
| 2026-01-03 18:03:20 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-01-03 18:03:44 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-03 18:01:54 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:00:20 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:13 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:05:46 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:04:14 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:02:19 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:11:58 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:02:12 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:02:51 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:03:01 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:02:59 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:03:07 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:03:25 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:04:22 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:08 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:07:19 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-01-03 18:05:44 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-01-03 18:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-03 18:03:37 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-03 18:03:34 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-03 18:01:42 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-01-03 18:08:42 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.012 |  |
| 2026-01-03 18:07:20 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.016 |  |
| 2026-01-03 18:08:22 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-01-03 18:04:34 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-01-03 18:04:36 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-01-03 18:03:39 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-01-03 18:02:26 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.021 |  |
| 2026-01-03 18:07:52 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.028 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |
| 2026-01-03 18:10:32 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.081 |  |
| 2026-01-03 18:04:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.088 |  |
| 2026-01-03 18:00:11 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)