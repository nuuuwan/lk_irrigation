# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_23:21:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 23:21:16 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:17:09 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:14:23 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:10:14 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:10:13 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-07-05 23:09:29 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:08:32 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:08:21 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 23:07:35 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-07-05 23:07:16 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:06:51 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:06:22 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:05:02 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-07-05 23:04:50 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:04:45 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-07-05 23:04:15 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.074 |  |
| 2026-07-05 23:04:04 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:03:45 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:03:42 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-07-05 23:03:16 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:03:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:02:44 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:02:17 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 23:02:14 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-07-05 23:02:12 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | -0.050 |  |
| 2026-07-05 23:01:59 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-07-05 23:01:53 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:01:42 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:01:37 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.022 |  |
| 2026-07-05 23:01:28 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.040 |  |
| 2026-07-05 23:01:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:01:15 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-05 23:00:50 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:00:18 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 23:01:15 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-05 23:02:17 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 23:08:21 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 23:04:50 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:00:18 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:01:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:00:50 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:02:43 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:07:04 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:41 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:10:14 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:06:22 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:14:23 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:03:16 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:03:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:04:04 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:09:29 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:03:45 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:07:16 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:17:09 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:01:42 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:08:32 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:06:51 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:21:16 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:01:53 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:10:13 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-07-05 23:03:42 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-05 23:05:02 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-07-05 23:07:35 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-07-05 23:01:59 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-07-05 23:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-07-05 23:02:14 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-07-05 23:01:37 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.022 |  |
| 2026-07-05 23:01:28 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.040 |  |
| 2026-07-05 23:02:12 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | -0.050 |  |
| 2026-07-05 23:04:15 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.074 |  |
| 2026-07-05 22:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.373 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)