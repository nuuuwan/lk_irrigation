# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_19:14:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,837 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 19:14:23 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:10:56 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-14 19:08:30 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:08:22 | Rathnapura (Kalu Ganga) | 4.92 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-14 19:08:08 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.028 |  |
| 2026-05-14 19:07:40 | Nawalapitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-14 19:06:46 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-14 19:06:34 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:06:30 | Glencourse (Kelani Ganga) | 13.16 | 🟢 Normal | 0.501 | 🔺 Rising |
| 2026-05-14 19:06:03 | Katharagama (Menik Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:06:00 | Yaka Wewa (Ma Oya) | 1.13 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-05-14 19:05:40 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:05:35 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-05-14 19:05:35 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:05:07 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-14 19:05:07 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:04:31 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:04:16 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-14 19:04:01 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.142 |  |
| 2026-05-14 19:03:56 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-05-14 19:03:41 | Dunamale (Aththanagalu Oya) | 3.85 | 🟡 Alert | 0.246 | 🔺 Rising |
| 2026-05-14 19:03:18 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:03:14 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-14 19:03:01 | Magura (Kalu Ganga) | 5.00 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-05-14 19:02:40 | Hanwella (Kelani Ganga) | 3.69 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-05-14 19:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-05-14 19:02:27 | Giriulla (Maha Oya) | 3.42 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-05-14 19:02:13 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.019 |  |
| 2026-05-14 19:01:41 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-14 19:01:17 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:01:17 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-05-14 19:01:12 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.150 |  |
| 2026-05-14 19:01:12 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-14 19:01:11 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:01:08 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 19:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-05-14 19:03:41 | Dunamale (Aththanagalu Oya) | 3.85 | 🟡 Alert | 0.246 | 🔺 Rising |
| 2026-05-14 19:03:01 | Magura (Kalu Ganga) | 5.00 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-05-14 19:06:30 | Glencourse (Kelani Ganga) | 13.16 | 🟢 Normal | 0.501 | 🔺 Rising |
| 2026-05-14 19:02:40 | Hanwella (Kelani Ganga) | 3.69 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-05-14 16:04:04 | Deraniyagala (Kelani Ganga) | 3.81 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-05-14 19:05:35 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-05-14 19:02:27 | Giriulla (Maha Oya) | 3.42 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-05-14 19:06:00 | Yaka Wewa (Ma Oya) | 1.13 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-05-14 19:01:17 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-05-14 19:06:46 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-14 19:08:22 | Rathnapura (Kalu Ganga) | 4.92 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-14 19:04:16 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-14 19:01:41 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-14 19:07:40 | Nawalapitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-14 19:10:56 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-14 19:05:07 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-14 19:06:34 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:05:35 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:14:23 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:05:40 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:03:18 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:04:31 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:01:11 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:06:03 | Katharagama (Menik Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:01:17 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:08:30 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:05:07 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 19:03:56 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-05-14 19:01:12 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-14 19:03:14 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-14 19:02:13 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.019 |  |
| 2026-05-14 19:01:08 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.023 |  |
| 2026-05-14 19:08:08 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.028 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-14 19:04:01 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.142 |  |
| 2026-05-14 19:01:12 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)