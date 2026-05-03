# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_08:13:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,595 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 08:13:40 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.033 |  |
| 2026-05-03 08:13:12 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-03 08:11:56 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-05-03 08:09:12 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:08:04 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:07:54 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.057 |  |
| 2026-05-03 08:07:10 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:06:58 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:06:43 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:06:41 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.140 |  |
| 2026-05-03 08:06:41 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | -0.019 |  |
| 2026-05-03 08:05:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-03 08:05:09 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:04:55 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-05-03 08:04:23 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.154 |  |
| 2026-05-03 08:04:22 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.05 | 🟢 Normal | -0.043 |  |
| 2026-05-03 08:04:15 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:04:07 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-03 08:03:46 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:03:36 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-05-03 08:03:32 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:03:16 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-03 08:03:16 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:02:59 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:02:41 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:02:23 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:02:15 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:02:07 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:02:05 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-05-03 08:01:57 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.518 | 🔺 Rising |
| 2026-05-03 08:01:47 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:01:38 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:01:25 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-03 08:01:21 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-03 08:01:16 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-03 08:01:13 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.038 |  |
| 2026-05-03 08:00:48 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | -0.022 |  |
| 2026-05-03 08:00:19 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 08:01:57 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.518 | 🔺 Rising |
| 2026-05-03 08:01:16 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-03 08:01:25 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-03 08:01:21 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-03 08:13:12 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-03 08:03:16 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-03 08:05:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-03 08:01:47 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:01:38 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:02:41 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:02:15 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:04:22 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:03:46 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:06:43 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:06:58 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:03:16 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:03:32 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:07:10 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:02:07 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:05:09 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:02:59 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:08:04 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:09:12 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:02:23 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:04:15 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-03 08:04:55 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-05-03 08:04:07 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-03 08:02:05 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-05-03 08:11:56 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-05-03 08:06:41 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | -0.019 |  |
| 2026-05-03 08:00:19 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.020 |  |
| 2026-05-03 08:00:48 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | -0.022 |  |
| 2026-05-03 08:03:36 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-05-03 08:13:40 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.033 |  |
| 2026-05-03 08:01:13 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.038 |  |
| 2026-05-03 08:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.05 | 🟢 Normal | -0.043 |  |
| 2026-05-03 08:07:54 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.057 |  |
| 2026-05-03 08:06:41 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.140 |  |
| 2026-05-03 08:04:23 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)