# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_19:11:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 19:11:53 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.009 |  |
| 2026-05-26 19:09:46 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.063 |  |
| 2026-05-26 19:08:56 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:08:19 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:08:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:08:03 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:07:21 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-05-26 19:07:05 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-05-26 19:06:16 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:06:11 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 19:06:01 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.011 |  |
| 2026-05-26 19:06:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.050 |  |
| 2026-05-26 19:05:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:04:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:04:06 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-26 19:03:52 | Hanwella (Kelani Ganga) | 4.68 | 🟢 Normal | -0.049 |  |
| 2026-05-26 19:03:40 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.030 |  |
| 2026-05-26 19:03:16 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | -0.032 |  |
| 2026-05-26 19:03:11 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:03:04 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:03:00 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-26 19:02:57 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:02:46 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:02:31 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-26 19:02:27 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.033 |  |
| 2026-05-26 19:02:26 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.021 |  |
| 2026-05-26 19:02:25 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.020 |  |
| 2026-05-26 19:02:04 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 19:01:46 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-26 19:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-05-26 19:01:38 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.539 |  |
| 2026-05-26 19:01:29 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:01:00 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 18:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | 0.000 |  |
| 2026-05-26 19:02:04 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 19:06:11 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 19:03:11 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:01:29 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:02:57 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:08:56 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:02:46 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:06:16 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:08:19 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:08:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:05:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:04:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:08:03 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:11:53 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.009 |  |
| 2026-05-26 19:04:06 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-26 19:07:21 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-05-26 19:03:00 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-26 19:02:31 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-26 19:01:46 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:00:10 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:02:59 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-26 19:01:00 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.011 |  |
| 2026-05-26 19:06:01 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.011 |  |
| 2026-05-26 19:07:05 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-05-26 19:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-26 19:02:25 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.020 |  |
| 2026-05-26 19:02:26 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.021 |  |
| 2026-05-26 19:03:40 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.030 |  |
| 2026-05-26 19:03:16 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | -0.032 |  |
| 2026-05-26 19:02:27 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.033 |  |
| 2026-05-26 19:03:52 | Hanwella (Kelani Ganga) | 4.68 | 🟢 Normal | -0.049 |  |
| 2026-05-26 19:06:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.050 |  |
| 2026-05-26 19:09:46 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.063 |  |
| 2026-05-26 19:01:38 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.539 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)