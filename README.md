# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_06:32:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,235 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 06:32:50 | Galgamuwa (Mee Oya) | 3.30 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-15 06:15:32 | Thawalama (Gin Ganga) | 2.73 | 🟢 Normal | -0.059 |  |
| 2026-05-15 06:12:51 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:12:30 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:09:12 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-05-15 06:08:32 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.032 |  |
| 2026-05-15 06:08:31 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 06:07:22 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-15 06:07:15 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.037 |  |
| 2026-05-15 06:06:57 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:05:43 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:05:43 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:04:54 | Katharagama (Menik Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:04:31 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-05-15 06:04:28 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:04:14 | Glencourse (Kelani Ganga) | 13.77 | 🟢 Normal | -0.148 |  |
| 2026-05-15 06:04:10 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:04:10 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-15 06:03:47 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:03:38 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.097 |  |
| 2026-05-15 06:03:27 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.022 |  |
| 2026-05-15 06:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | 0.078 | 🔺 Rising |
| 2026-05-15 06:03:20 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-15 06:03:19 | Badalgama (Maha Oya) | 4.73 | 🟢 Normal | -0.030 |  |
| 2026-05-15 06:02:55 | Giriulla (Maha Oya) | 3.73 | 🟢 Normal | -0.050 |  |
| 2026-05-15 06:02:08 | Hanwella (Kelani Ganga) | 6.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-15 06:01:58 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:01:51 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | 0.000 |  |
| 2026-05-15 06:01:49 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.380 |  |
| 2026-05-15 06:01:45 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-15 06:01:44 | Moragaswewa (Deduru Oya) | 3.60 | 🟢 Normal | 0.802 | 🔺 Rising |
| 2026-05-15 06:01:44 | Dunamale (Aththanagalu Oya) | 4.70 | 🟠 Minor Flood | 0.057 | 🔺 Rising |
| 2026-05-15 06:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.093 |  |
| 2026-05-15 06:01:34 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-05-15 06:01:29 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.092 |  |
| 2026-05-15 06:01:24 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 06:00:50 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-15 06:00:36 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-15 06:00:30 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.766 | 🔺 Rising |
| 2026-05-15 06:00:20 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 06:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | 0.078 | 🔺 Rising |
| 2026-05-15 06:01:44 | Dunamale (Aththanagalu Oya) | 4.70 | 🟠 Minor Flood | 0.057 | 🔺 Rising |
| 2026-05-15 06:01:51 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | 0.000 |  |
| 2026-05-15 06:01:44 | Moragaswewa (Deduru Oya) | 3.60 | 🟢 Normal | 0.802 | 🔺 Rising |
| 2026-05-15 06:00:30 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.766 | 🔺 Rising |
| 2026-05-15 06:09:12 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-05-15 06:32:50 | Galgamuwa (Mee Oya) | 3.30 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-15 06:02:08 | Hanwella (Kelani Ganga) | 6.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-15 06:08:31 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 06:07:22 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-15 06:04:10 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-15 06:01:24 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 06:00:36 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-15 06:04:10 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:06:57 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:04:28 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:05:43 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:03:47 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:01:58 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:04:54 | Katharagama (Menik Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:12:51 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:05:43 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 06:01:45 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-15 06:03:20 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-15 06:00:50 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-15 06:04:31 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-05-15 06:03:27 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.022 |  |
| 2026-05-15 06:03:19 | Badalgama (Maha Oya) | 4.73 | 🟢 Normal | -0.030 |  |
| 2026-05-15 06:08:32 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.032 |  |
| 2026-05-15 06:07:15 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.037 |  |
| 2026-05-15 06:01:34 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-05-15 06:02:55 | Giriulla (Maha Oya) | 3.73 | 🟢 Normal | -0.050 |  |
| 2026-05-15 06:15:32 | Thawalama (Gin Ganga) | 2.73 | 🟢 Normal | -0.059 |  |
| 2026-05-15 06:01:29 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.092 |  |
| 2026-05-15 06:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.093 |  |
| 2026-05-15 06:03:38 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.097 |  |
| 2026-05-15 06:04:14 | Glencourse (Kelani Ganga) | 13.77 | 🟢 Normal | -0.148 |  |
| 2026-05-15 06:01:49 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.380 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)