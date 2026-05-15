# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_12:16:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,481 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 12:16:37 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-05-15 12:16:04 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:13:57 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:13:05 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.062 |  |
| 2026-05-15 12:09:27 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.117 |  |
| 2026-05-15 12:09:01 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:08:49 | Badalgama (Maha Oya) | 4.44 | 🟢 Normal | -0.056 |  |
| 2026-05-15 12:07:13 | Magura (Kalu Ganga) | 4.65 | 🟡 Alert | -0.028 |  |
| 2026-05-15 12:06:36 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:06:36 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 12:06:31 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 12:05:59 | Galgamuwa (Mee Oya) | 3.75 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-15 12:05:55 | Dunamale (Aththanagalu Oya) | 4.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 12:05:51 | Glencourse (Kelani Ganga) | 12.61 | 🟢 Normal | -0.200 |  |
| 2026-05-15 12:05:48 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-05-15 12:05:32 | Moragaswewa (Deduru Oya) | 3.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 12:05:13 | Rathnapura (Kalu Ganga) | 4.57 | 🟢 Normal | -0.051 |  |
| 2026-05-15 12:05:00 | Giriulla (Maha Oya) | 3.29 | 🟢 Normal | -0.086 |  |
| 2026-05-15 12:04:28 | Hanwella (Kelani Ganga) | 5.85 | 🟢 Normal | -0.098 |  |
| 2026-05-15 12:04:04 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:03:58 | Katharagama (Menik Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:03:58 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:03:39 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 12:03:07 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.056 |  |
| 2026-05-15 12:02:22 | Nagalagam Street (Kelani Ganga) | 1.25 | 🟡 Alert | 0.095 | 🔺 Rising |
| 2026-05-15 12:02:19 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:02:19 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 12:02:16 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.060 |  |
| 2026-05-15 12:01:56 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-15 12:01:54 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:01:41 | Thanthirimale (Malwathu Oya) | 4.10 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-15 12:01:27 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-15 12:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.98 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-05-15 12:01:07 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-05-15 12:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:00:33 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:00:20 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:00:20 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:00:15 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-05-15 12:00:12 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 12:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.98 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-05-15 12:05:55 | Dunamale (Aththanagalu Oya) | 4.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 12:02:22 | Nagalagam Street (Kelani Ganga) | 1.25 | 🟡 Alert | 0.095 | 🔺 Rising |
| 2026-05-15 12:07:13 | Magura (Kalu Ganga) | 4.65 | 🟡 Alert | -0.028 |  |
| 2026-05-15 12:01:41 | Thanthirimale (Malwathu Oya) | 4.10 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-15 12:05:59 | Galgamuwa (Mee Oya) | 3.75 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-15 12:02:19 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 12:05:32 | Moragaswewa (Deduru Oya) | 3.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 12:00:12 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-15 12:06:36 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 12:06:31 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 12:03:39 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 12:00:20 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:01:54 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:06:36 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:03:58 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:00:33 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:16:04 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:04:04 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:09:01 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:03:58 | Katharagama (Menik Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:13:57 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:00:20 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-15 12:16:37 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-05-15 12:01:27 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-15 12:01:56 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-15 12:00:15 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-05-15 12:01:07 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-05-15 12:05:48 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-05-15 12:05:13 | Rathnapura (Kalu Ganga) | 4.57 | 🟢 Normal | -0.051 |  |
| 2026-05-15 12:08:49 | Badalgama (Maha Oya) | 4.44 | 🟢 Normal | -0.056 |  |
| 2026-05-15 12:03:07 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.056 |  |
| 2026-05-15 12:02:16 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.060 |  |
| 2026-05-15 12:13:05 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.062 |  |
| 2026-05-15 12:05:00 | Giriulla (Maha Oya) | 3.29 | 🟢 Normal | -0.086 |  |
| 2026-05-15 12:04:28 | Hanwella (Kelani Ganga) | 5.85 | 🟢 Normal | -0.098 |  |
| 2026-05-15 12:09:27 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.117 |  |
| 2026-05-15 12:05:51 | Glencourse (Kelani Ganga) | 12.61 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)