# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_01:24:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,281 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 01:24:09 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.069 |  |
| 2026-05-30 01:22:27 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.016 |  |
| 2026-05-30 01:19:02 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:15:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:11:24 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.027 |  |
| 2026-05-30 01:07:13 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.028 |  |
| 2026-05-30 01:06:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-05-30 01:06:12 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.038 |  |
| 2026-05-30 01:06:03 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:05:59 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:05:29 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:05:29 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:05:03 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-30 01:04:41 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-05-30 01:04:15 | Baddegama (Gin Ganga) | 3.20 | 🟢 Normal | -0.021 |  |
| 2026-05-30 01:04:05 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-30 01:03:40 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:03:35 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-30 01:03:10 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-05-30 01:03:05 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-30 01:02:58 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.050 |  |
| 2026-05-30 01:02:48 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:02:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:02:36 | Ellagawa (Kalu Ganga) | 8.35 | 🟢 Normal | -0.020 |  |
| 2026-05-30 01:02:13 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:02:11 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.040 |  |
| 2026-05-30 01:02:09 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.050 |  |
| 2026-05-30 01:02:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:01:47 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-05-30 01:01:32 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:01:10 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:00:54 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 01:00:46 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 01:06:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-05-30 01:05:03 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-30 01:00:54 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 00:05:00 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:01:32 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:01:10 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:02:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:15:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:04:21 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:02:48 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:02:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:03:40 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:05:59 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:19:02 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:00:46 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:05:29 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:05:29 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:01:26 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:01:20 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:06:03 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:03:35 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:05:25 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:03:20 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-05-30 01:04:05 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-30 01:03:05 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-30 01:22:27 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.016 |  |
| 2026-05-30 01:04:41 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-05-30 01:03:10 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-05-30 01:02:36 | Ellagawa (Kalu Ganga) | 8.35 | 🟢 Normal | -0.020 |  |
| 2026-05-30 01:01:47 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-05-30 01:04:15 | Baddegama (Gin Ganga) | 3.20 | 🟢 Normal | -0.021 |  |
| 2026-05-30 01:11:24 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.027 |  |
| 2026-05-30 01:07:13 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.028 |  |
| 2026-05-29 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.034 |  |
| 2026-05-30 01:06:12 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.038 |  |
| 2026-05-30 01:02:11 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.040 |  |
| 2026-05-30 01:02:09 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.050 |  |
| 2026-05-30 01:02:58 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.050 |  |
| 2026-05-30 01:24:09 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)