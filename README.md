# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_20:23:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,924 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 20:23:39 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-23 20:14:43 | Dunamale (Aththanagalu Oya) | 4.80 | 🟠 Minor Flood | -0.042 |  |
| 2026-05-23 20:13:24 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.025 |  |
| 2026-05-23 20:09:32 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.028 |  |
| 2026-05-23 20:07:12 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-23 20:06:44 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:06:42 | Magura (Kalu Ganga) | 3.25 | 🟢 Normal | -0.049 |  |
| 2026-05-23 20:06:10 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-05-23 20:05:33 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.012 |  |
| 2026-05-23 20:05:00 | Nagalagam Street (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:04:58 | Rathnapura (Kalu Ganga) | 5.46 | 🟡 Alert | -0.076 |  |
| 2026-05-23 20:04:15 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:04:10 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.069 |  |
| 2026-05-23 20:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 20:04:07 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:04:05 | Putupaula (Kalu Ganga) | 3.19 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 20:03:51 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.021 |  |
| 2026-05-23 20:03:49 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:03:46 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:03:40 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-23 20:03:31 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-23 20:03:16 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:03:11 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:03:07 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.031 |  |
| 2026-05-23 20:03:03 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:03:02 | Ellagawa (Kalu Ganga) | 10.26 | 🟡 Alert | -0.043 |  |
| 2026-05-23 20:03:00 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:02:35 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.051 |  |
| 2026-05-23 20:02:22 | Hanwella (Kelani Ganga) | 5.85 | 🟢 Normal | -0.100 |  |
| 2026-05-23 20:02:01 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.022 |  |
| 2026-05-23 20:01:53 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.022 |  |
| 2026-05-23 20:01:32 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:01:11 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:00:42 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:00:38 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:00:37 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:00:34 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:00:27 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 20:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 20:14:43 | Dunamale (Aththanagalu Oya) | 4.80 | 🟠 Minor Flood | -0.042 |  |
| 2026-05-23 20:04:05 | Putupaula (Kalu Ganga) | 3.19 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 20:03:02 | Ellagawa (Kalu Ganga) | 10.26 | 🟡 Alert | -0.043 |  |
| 2026-05-23 20:04:58 | Rathnapura (Kalu Ganga) | 5.46 | 🟡 Alert | -0.076 |  |
| 2026-05-23 20:07:12 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-23 20:03:31 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-23 20:23:39 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-23 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 20:03:49 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:01:53 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:03:16 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:01:32 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:04:07 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:04:23 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:03:11 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:01:11 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:05:00 | Nagalagam Street (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:00:42 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:03:00 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:03:46 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:06:44 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:00:27 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:03:03 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-23 20:04:15 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-23 20:03:40 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-23 20:05:33 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.012 |  |
| 2026-05-23 20:06:10 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-05-23 20:03:51 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.021 |  |
| 2026-05-23 20:02:01 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.022 |  |
| 2026-05-23 20:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.022 |  |
| 2026-05-23 20:13:24 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.025 |  |
| 2026-05-23 20:09:32 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.028 |  |
| 2026-05-23 20:03:07 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.031 |  |
| 2026-05-23 20:06:42 | Magura (Kalu Ganga) | 3.25 | 🟢 Normal | -0.049 |  |
| 2026-05-23 20:02:35 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.051 |  |
| 2026-05-23 20:04:10 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.069 |  |
| 2026-05-23 20:02:22 | Hanwella (Kelani Ganga) | 5.85 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)