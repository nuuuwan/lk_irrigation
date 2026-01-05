# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_18:25:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,524 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 18:25:56 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.004 |  |
| 2026-01-05 18:14:07 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:11:41 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:11:38 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-01-05 18:10:16 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:08:37 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:06:53 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.019 |  |
| 2026-01-05 18:06:06 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:05:16 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.059 |  |
| 2026-01-05 18:04:36 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-05 18:04:23 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-05 18:03:45 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-01-05 18:03:41 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.077 |  |
| 2026-01-05 18:03:16 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-05 18:03:15 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-01-05 18:03:09 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:02:26 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-01-05 18:02:17 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 1.421 | 🔺 Rising |
| 2026-01-05 18:02:16 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.063 |  |
| 2026-01-05 18:02:16 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:02:09 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:02:07 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:02:02 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:02:02 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-05 18:01:58 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:01:54 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:01:50 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 18:02:17 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 1.421 | 🔺 Rising |
| 2026-01-05 18:01:10 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.407 | 🔺 Rising |
| 2026-01-05 18:03:15 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-05 18:02:02 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-05 18:04:23 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-05 18:01:13 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-05 18:03:16 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-05 18:02:26 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 18:01:50 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 18:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 18:02:07 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:01:35 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:04:36 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:11:41 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:02:16 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:01:54 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:03:09 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:02:02 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:01:58 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:08:37 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:06:06 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:01:19 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:14:07 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:01:17 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:02:09 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:25:56 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.004 |  |
| 2026-01-05 18:01:27 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.005 |  |
| 2026-01-05 18:11:38 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-01-05 18:00:15 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-05 18:03:45 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-01-05 18:06:53 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.019 |  |
| 2026-01-05 18:00:18 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-01-05 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-01-05 18:05:16 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.059 |  |
| 2026-01-05 18:02:16 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.063 |  |
| 2026-01-05 18:03:41 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)