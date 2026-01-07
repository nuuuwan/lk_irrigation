# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_08:30:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,906 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 08:30:30 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-07 08:15:20 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:14:04 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:13:07 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:13:07 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.036 |  |
| 2026-01-07 08:11:38 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:11:16 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.571 |  |
| 2026-01-07 08:10:13 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.571 |  |
| 2026-01-07 08:08:50 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:08:24 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-01-07 08:08:04 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:08:01 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-07 08:07:25 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-01-07 08:07:17 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:06:56 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | -0.012 |  |
| 2026-01-07 08:06:20 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.028 |  |
| 2026-01-07 08:06:05 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-01-07 08:05:43 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:05:03 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.098 |  |
| 2026-01-07 08:04:58 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-07 08:04:25 | Manampitiya (Mahaweli Ganga) | 3.10 | 🟡 Alert | -0.095 |  |
| 2026-01-07 08:04:15 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:03:38 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-07 08:03:34 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-07 08:03:20 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.032 |  |
| 2026-01-07 08:03:14 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.010 |  |
| 2026-01-07 08:03:05 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-07 08:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:02:44 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.013 |  |
| 2026-01-07 08:02:41 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:02:28 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.060 |  |
| 2026-01-07 08:01:43 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:01:19 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:01:12 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-07 08:00:55 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 08:00:44 | Weraganthota (Mahaweli Ganga) | -0.99 | 🟢 Normal | -0.207 |  |
| 2026-01-07 08:00:29 | Siyambalanduwa (Heda Oya) | 1.91 | 🟢 Normal | -0.040 |  |
| 2026-01-07 08:00:24 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.097 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 08:04:25 | Manampitiya (Mahaweli Ganga) | 3.10 | 🟡 Alert | -0.095 |  |
| 2026-01-07 08:07:25 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-01-07 08:03:38 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-07 08:03:34 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-07 08:08:01 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-07 08:30:30 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-07 08:00:55 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 08:01:19 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:01:43 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:13:07 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:14:04 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:15:20 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:02:28 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:11:38 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:04:15 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:08:04 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:07:17 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:08:50 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:02:41 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:05:43 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:08:24 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-01-07 08:04:58 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-07 08:03:05 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-07 08:03:14 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.010 |  |
| 2026-01-07 08:01:12 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-07 08:06:56 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | -0.012 |  |
| 2026-01-07 08:02:44 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.013 |  |
| 2026-01-07 08:06:05 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-01-07 08:06:20 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.028 |  |
| 2026-01-07 08:03:20 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.032 |  |
| 2026-01-07 08:13:07 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.036 |  |
| 2026-01-07 08:00:29 | Siyambalanduwa (Heda Oya) | 1.91 | 🟢 Normal | -0.040 |  |
| 2026-01-07 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.060 |  |
| 2026-01-07 08:00:24 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.097 |  |
| 2026-01-07 08:05:03 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.098 |  |
| 2026-01-07 07:03:08 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.130 |  |
| 2026-01-07 08:00:44 | Weraganthota (Mahaweli Ganga) | -0.99 | 🟢 Normal | -0.207 |  |
| 2026-01-07 08:11:16 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.571 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)