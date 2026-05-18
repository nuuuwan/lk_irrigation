# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_23:20:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,591 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 23:20:37 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.016 |  |
| 2026-05-18 23:16:43 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-05-18 23:12:50 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.044 |  |
| 2026-05-18 23:12:47 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:10:18 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-05-18 23:07:29 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:06:15 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.019 |  |
| 2026-05-18 23:05:55 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-05-18 23:05:29 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:05:17 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:05:07 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-05-18 23:05:01 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-05-18 23:04:59 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.113 |  |
| 2026-05-18 23:04:40 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.009 |  |
| 2026-05-18 23:04:16 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 23:04:06 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.038 |  |
| 2026-05-18 23:03:30 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:03:07 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-05-18 23:03:06 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:02:58 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 23:02:33 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:02:31 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-05-18 23:02:31 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.016 |  |
| 2026-05-18 23:02:15 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:01:49 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.174 |  |
| 2026-05-18 23:01:36 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:01:22 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:01:22 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:01:07 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 23:00:27 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-18 23:00:25 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 23:00:15 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 21:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.000 |  |
| 2026-05-18 23:02:58 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 23:04:16 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 23:01:07 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 23:00:25 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:00:15 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:01:45 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:05:29 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:07:29 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:01:36 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:03:30 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:01:22 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:02:33 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:12:47 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:05:17 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:03:06 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:03:32 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:01:22 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:02:15 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 23:16:43 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-05-18 23:04:40 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.009 |  |
| 2026-05-18 23:03:07 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-05-18 23:05:55 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-05-18 23:05:07 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-05-18 23:00:27 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-18 23:20:37 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.016 |  |
| 2026-05-18 23:02:31 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.016 |  |
| 2026-05-18 23:10:18 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-05-18 22:03:44 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2026-05-18 23:06:15 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.019 |  |
| 2026-05-18 23:05:01 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-05-18 23:02:31 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-05-18 18:01:53 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.033 |  |
| 2026-05-18 23:04:06 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.038 |  |
| 2026-05-18 23:12:50 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.044 |  |
| 2026-05-18 18:01:24 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | -0.082 |  |
| 2026-05-18 23:04:59 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.113 |  |
| 2026-05-18 23:01:49 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.174 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)