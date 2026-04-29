# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_09:26:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,069 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 09:26:33 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-29 09:23:43 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:15:12 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:12:42 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.033 |  |
| 2026-04-29 09:09:25 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-04-29 09:09:12 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-29 09:08:25 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.048 |  |
| 2026-04-29 09:07:33 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:06:26 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:06:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-29 09:06:06 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-04-29 09:05:49 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.040 |  |
| 2026-04-29 09:04:32 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-04-29 09:04:09 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:03:43 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-29 09:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-04-29 09:03:40 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 09:03:28 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.055 |  |
| 2026-04-29 09:03:27 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:03:25 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 09:03:21 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:03:11 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-29 09:03:10 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-29 09:03:09 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.249 |  |
| 2026-04-29 09:03:00 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:02:59 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-29 09:02:58 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:02:54 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:02:29 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.878 |  |
| 2026-04-29 09:02:24 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-04-29 09:02:15 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:02:14 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-04-29 09:02:13 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:01:57 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 09:01:48 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.878 |  |
| 2026-04-29 09:01:29 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-04-29 09:01:25 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | -0.032 |  |
| 2026-04-29 09:01:16 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.010 |  |
| 2026-04-29 09:01:10 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:01:08 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-04-29 09:00:47 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 09:06:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-29 09:03:11 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-29 09:09:12 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-29 09:02:59 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-29 09:26:33 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-29 09:03:10 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-29 09:03:40 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 09:03:25 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 09:01:57 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 09:02:15 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:02:54 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:01:10 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:07:33 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:03:27 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:23:43 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:02:58 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:03:21 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:03:00 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:06:26 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:00:47 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:15:12 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-29 09:09:25 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-04-29 09:03:43 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-29 09:01:29 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-04-29 09:01:16 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.010 |  |
| 2026-04-29 09:01:08 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-04-29 09:04:32 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-04-29 09:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-04-29 09:02:14 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-04-29 09:02:24 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-04-29 09:06:06 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-04-29 09:01:25 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | -0.032 |  |
| 2026-04-29 09:12:42 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.033 |  |
| 2026-04-29 09:05:49 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.040 |  |
| 2026-04-29 09:08:25 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.048 |  |
| 2026-04-29 09:03:28 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.055 |  |
| 2026-04-29 09:03:09 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.249 |  |
| 2026-04-29 09:02:29 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.878 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)