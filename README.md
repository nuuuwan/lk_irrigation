# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_00:27:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,625 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 00:27:44 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:24:59 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -72.000 |  |
| 2026-05-19 00:24:58 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -72.000 |  |
| 2026-05-19 00:14:04 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-05-19 00:10:00 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:09:08 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.028 |  |
| 2026-05-19 00:08:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-19 00:07:26 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:07:20 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:06:27 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | -0.028 |  |
| 2026-05-19 00:05:50 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.005 |  |
| 2026-05-19 00:05:42 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 00:05:08 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-19 00:05:05 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.023 |  |
| 2026-05-19 00:04:33 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:03:58 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 00:03:56 | Ellagawa (Kalu Ganga) | 5.71 | 🟢 Normal | -0.042 |  |
| 2026-05-19 00:03:52 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:03:34 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-05-19 00:03:30 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-05-19 00:03:23 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:03:12 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:02:58 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:02:57 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 00:02:46 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:02:32 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:02:18 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:02:15 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.094 |  |
| 2026-05-19 00:02:04 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:01:58 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:01:34 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-19 00:01:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:00:27 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 21:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.000 |  |
| 2026-05-19 00:08:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-19 00:05:08 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-19 00:02:57 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 00:03:58 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 00:05:42 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 00:01:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:00:27 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:03:52 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:27:44 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:02:46 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:10:00 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:07:26 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:02:04 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:01:58 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:02:32 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:02:33 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:03:23 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:07:20 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:02:18 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:36:58 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:04:33 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:02:58 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:05:50 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.005 |  |
| 2026-05-19 00:14:04 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-05-19 00:01:34 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-18 23:05:07 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-05-19 00:03:30 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-05-19 00:03:34 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-05-18 23:20:37 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.016 |  |
| 2026-05-19 00:05:05 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.023 |  |
| 2026-05-19 00:09:08 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.028 |  |
| 2026-05-19 00:06:27 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | -0.028 |  |
| 2026-05-18 18:01:53 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.033 |  |
| 2026-05-19 00:03:56 | Ellagawa (Kalu Ganga) | 5.71 | 🟢 Normal | -0.042 |  |
| 2026-05-18 18:01:24 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | -0.082 |  |
| 2026-05-19 00:02:15 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.094 |  |
| 2026-05-19 00:24:59 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)