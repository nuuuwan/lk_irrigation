# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_23:17:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,476 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 23:17:20 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.024 |  |
| 2026-05-19 23:09:36 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:07:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:07:35 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:06:52 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-05-19 23:05:33 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:05:32 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-05-19 23:05:25 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-19 23:04:32 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:04:16 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:04:03 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:03:56 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:03:38 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.023 |  |
| 2026-05-19 23:03:16 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:03:11 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:03:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:02:04 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:01:58 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 23:01:33 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:01:33 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-05-19 23:01:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.033 |  |
| 2026-05-19 23:01:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:01:19 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:01:06 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:00:52 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:00:45 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-19 23:00:36 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:00:26 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 23:05:25 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-19 22:14:21 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-19 23:00:45 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-19 23:01:58 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 22:04:30 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 18:04:04 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:01:19 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:00:52 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:04:32 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:07:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:09:36 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:13:22 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:01:06 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:01:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:03:16 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:04:16 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:07:35 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:03:56 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:03:01 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:00:36 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:05:33 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:04:03 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:01:33 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:03:28 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:03:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:00:26 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:02:44 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:01:33 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-05-19 22:08:08 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.018 |  |
| 2026-05-19 23:05:32 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-19 23:06:52 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-05-19 23:03:38 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.023 |  |
| 2026-05-19 23:17:20 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.024 |  |
| 2026-05-19 23:01:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.033 |  |
| 2026-05-19 22:03:32 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.036 |  |
| 2026-05-19 21:18:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)