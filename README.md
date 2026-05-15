# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_23:15:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,898 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 23:15:04 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:12:36 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-15 23:11:20 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | -108.000 |  |
| 2026-05-15 23:11:19 | Baddegama (Gin Ganga) | 3.21 | 🟢 Normal | -108.000 |  |
| 2026-05-15 23:09:15 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:07:13 | Badalgama (Maha Oya) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-05-15 23:07:09 | Rathnapura (Kalu Ganga) | 4.07 | 🟢 Normal | -0.033 |  |
| 2026-05-15 23:06:45 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | -0.095 |  |
| 2026-05-15 23:06:27 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-15 23:06:14 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:06:07 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:05:53 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | -0.023 |  |
| 2026-05-15 23:05:50 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:05:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.04 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 23:05:04 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-15 23:04:23 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 23:03:27 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-15 23:03:13 | Giriulla (Maha Oya) | 2.82 | 🟢 Normal | -0.020 |  |
| 2026-05-15 23:02:57 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:02:37 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.040 |  |
| 2026-05-15 23:02:27 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-15 23:02:21 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:02:13 | Moragaswewa (Deduru Oya) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:02:07 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-15 23:02:04 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.042 |  |
| 2026-05-15 23:02:03 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.012 |  |
| 2026-05-15 23:02:02 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | -0.010 |  |
| 2026-05-15 23:01:59 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.081 |  |
| 2026-05-15 23:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.019 |  |
| 2026-05-15 23:01:47 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:01:45 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:01:34 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | -0.031 |  |
| 2026-05-15 23:01:32 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-05-15 23:01:13 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 23:05:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.04 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 22:02:20 | Dunamale (Aththanagalu Oya) | 4.62 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-15 23:01:34 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | -0.031 |  |
| 2026-05-15 23:06:27 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-15 22:03:56 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-15 23:02:07 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 23:04:23 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 23:12:36 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-15 22:16:01 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:01:47 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:02:13 | Moragaswewa (Deduru Oya) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:15:04 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:02:57 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:07:48 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:15:04 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:02:21 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:09:15 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:06:14 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:06:07 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-15 23:03:27 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-15 23:07:13 | Badalgama (Maha Oya) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-05-15 23:02:02 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | -0.010 |  |
| 2026-05-15 23:02:27 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-15 23:05:04 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-15 23:02:03 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.012 |  |
| 2026-05-15 23:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.019 |  |
| 2026-05-15 23:01:32 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-05-15 23:03:13 | Giriulla (Maha Oya) | 2.82 | 🟢 Normal | -0.020 |  |
| 2026-05-15 23:05:53 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | -0.023 |  |
| 2026-05-15 23:01:13 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | -0.027 |  |
| 2026-05-15 23:07:09 | Rathnapura (Kalu Ganga) | 4.07 | 🟢 Normal | -0.033 |  |
| 2026-05-15 23:02:37 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.040 |  |
| 2026-05-15 23:02:04 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.042 |  |
| 2026-05-15 23:01:59 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.081 |  |
| 2026-05-15 23:06:45 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | -0.095 |  |
| 2026-05-15 23:11:20 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)