# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_23:22:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,760 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 23:22:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.10 | 🟡 Alert | 0.015 | 🔺 Rising |
| 2026-06-12 23:11:02 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-12 23:09:00 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | -0.081 |  |
| 2026-06-12 23:07:33 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-12 23:06:52 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-12 23:06:47 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-12 23:06:34 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 23:05:20 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-12 23:04:43 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-12 23:04:28 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.010 |  |
| 2026-06-12 23:04:15 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:04:12 | Glencourse (Kelani Ganga) | 12.26 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-06-12 23:03:50 | Rathnapura (Kalu Ganga) | 6.49 | 🟡 Alert | -0.112 |  |
| 2026-06-12 23:03:22 | Urawa (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.032 |  |
| 2026-06-12 23:03:11 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 23:03:05 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-06-12 23:02:59 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 23:02:57 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.021 |  |
| 2026-06-12 23:02:53 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-06-12 23:02:42 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:02:39 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-12 23:02:27 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-12 23:02:26 | Dunamale (Aththanagalu Oya) | 3.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 23:02:14 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:02:11 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-06-12 23:01:58 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-06-12 23:01:56 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -11.455 |  |
| 2026-06-12 23:01:34 | Nawalapitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -11.455 |  |
| 2026-06-12 23:01:26 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:01:15 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-06-12 23:01:10 | Ellagawa (Kalu Ganga) | 8.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 23:01:04 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 23:00:55 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:00:15 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 23:03:05 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-06-12 23:22:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.10 | 🟡 Alert | 0.015 | 🔺 Rising |
| 2026-06-12 23:03:50 | Rathnapura (Kalu Ganga) | 6.49 | 🟡 Alert | -0.112 |  |
| 2026-06-12 23:04:12 | Glencourse (Kelani Ganga) | 12.26 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-06-12 23:01:58 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-06-12 23:07:33 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-12 23:06:52 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-12 23:04:43 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-12 23:02:27 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-12 23:05:20 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-12 22:06:30 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-12 23:01:04 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 23:02:26 | Dunamale (Aththanagalu Oya) | 3.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 22:03:57 | Thawalama (Gin Ganga) | 3.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 23:06:34 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 23:02:59 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 23:01:10 | Ellagawa (Kalu Ganga) | 8.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 23:03:11 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 23:06:47 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-12 23:02:39 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:00:15 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:02:42 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:02:14 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:00:55 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:01:26 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:04:15 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:02:53 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-06-12 23:11:02 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-12 23:04:28 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.010 |  |
| 2026-06-12 23:01:15 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-06-12 23:02:11 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-06-12 23:02:57 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.021 |  |
| 2026-06-12 23:03:22 | Urawa (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.032 |  |
| 2026-06-12 23:09:00 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | -0.081 |  |
| 2026-06-12 22:02:30 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.150 |  |
| 2026-06-12 23:01:56 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -11.455 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)