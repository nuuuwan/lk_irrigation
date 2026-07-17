# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18_05:01:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **209,237 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-18 05:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.037 |  |
| 2026-07-18 05:00:46 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.005 |  |
| 2026-07-18 04:42:50 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:29:50 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.027 |  |
| 2026-07-18 04:23:23 | Moraketiya (Walawe Ganga) | 0.46 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-18 04:17:58 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:17:10 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:14:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.061 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-18 04:09:41 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-18 04:03:07 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-07-18 04:14:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-18 04:04:41 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-07-18 04:03:08 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-18 03:08:26 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-18 03:07:17 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-18 04:23:23 | Moraketiya (Walawe Ganga) | 0.46 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-18 04:02:19 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:10:54 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:03:14 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:02:23 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:06:05 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:17:10 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 18:06:03 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:03:21 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:06:11 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:04:17 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:03:46 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:03:15 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-18 00:00:24 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:03:43 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:02:54 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:17:58 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:03:08 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:05:10 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:01:36 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-17 18:03:48 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:07:39 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:02:58 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:04:23 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-18 04:42:50 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 05:00:46 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.005 |  |
| 2026-07-18 04:02:54 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-07-18 04:02:26 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.025 |  |
| 2026-07-18 04:29:50 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.027 |  |
| 2026-07-17 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.030 |  |
| 2026-07-18 05:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.037 |  |
| 2026-07-18 04:00:54 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)