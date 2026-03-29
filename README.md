# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_22:23:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,925 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 22:23:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:17:41 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-29 22:15:32 | Ellagawa (Kalu Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:15:18 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.009 |  |
| 2026-03-29 22:12:26 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:09:11 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:08:36 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.060 |  |
| 2026-03-29 22:08:20 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-03-29 22:08:12 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:07:40 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:06:49 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:06:17 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:05:55 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-29 22:04:51 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-03-29 22:04:46 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:04:43 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-29 22:04:33 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 22:04:03 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:03:25 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:02:55 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:02:40 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.042 |  |
| 2026-03-29 22:02:37 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:02:37 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-03-29 22:02:32 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-29 22:02:25 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:02:21 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:02:13 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:01:57 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:01:56 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.021 |  |
| 2026-03-29 22:01:35 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-29 22:01:33 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 22:01:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-29 22:01:10 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:01:02 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-03-29 22:00:42 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:00:12 | Magura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-29 21:59:51 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 22:02:37 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-03-29 22:01:02 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-03-29 22:05:55 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-29 22:01:35 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-29 22:02:32 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-29 22:01:33 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 22:04:33 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 22:17:41 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-29 21:26:18 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-29 22:00:42 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:01:57 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:02:21 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:07:40 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:06:49 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:02:13 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:04:46 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:03:02 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:00:12 | Magura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:06:17 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:15:32 | Ellagawa (Kalu Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:09:11 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:03:25 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:02:55 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:23:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:02:25 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:08:12 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:01:38 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:12:26 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:04:03 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:15:18 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.009 |  |
| 2026-03-29 22:08:20 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-03-29 22:04:43 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-29 22:04:51 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-03-29 22:01:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-29 22:01:56 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.021 |  |
| 2026-03-29 21:59:51 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-03-29 22:02:40 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.042 |  |
| 2026-03-29 22:08:36 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.060 |  |
| 2026-03-29 18:00:53 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)