# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_21:14:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,783 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 21:14:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-12 21:08:58 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-08-12 21:07:44 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:07:22 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:07:16 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 21:05:30 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-12 21:05:11 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:05:03 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:04:59 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:04:57 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.090 |  |
| 2026-08-12 21:04:22 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.060 |  |
| 2026-08-12 21:04:09 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:03:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:03:44 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:03:44 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-08-12 21:03:34 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.080 |  |
| 2026-08-12 21:03:22 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:03:20 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-12 21:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:37 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:35 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:33 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:33 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-12 21:02:29 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-08-12 21:02:21 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:14 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:12 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:01:26 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:01:20 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-12 21:01:17 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:01:16 | Peradeniya (Mahaweli Ganga) | 3.31 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:00:37 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.037 |  |
| 2026-08-12 21:00:31 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-08-12 21:00:11 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:00:09 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 20:04:26 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-08-12 21:01:20 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-12 21:03:20 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-12 21:05:30 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-12 21:02:33 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-12 21:07:16 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 21:14:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-12 21:00:11 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:35 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:03:22 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:03:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:03:44 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:01:17 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:05:42 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:04:09 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:37 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:00:09 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:07:22 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:04:59 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:21 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:05:11 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:12 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:05:03 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:14 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:39 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:01:16 | Peradeniya (Mahaweli Ganga) | 3.31 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:07:44 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:01:26 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:02:33 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 21:08:58 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-08-12 21:00:31 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-08-12 21:03:44 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-08-12 21:02:29 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-08-12 17:00:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.031 |  |
| 2026-08-12 21:00:37 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.037 |  |
| 2026-08-12 21:04:22 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.060 |  |
| 2026-08-12 21:03:34 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.080 |  |
| 2026-08-12 21:04:57 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)