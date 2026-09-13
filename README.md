# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_03:22:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,286 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 03:22:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:16:32 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.062 |  |
| 2026-09-14 03:15:31 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-14 03:13:06 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | -0.101 |  |
| 2026-09-14 03:12:26 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:08:16 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:06:58 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-09-14 03:06:09 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:05:44 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:05:29 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:05:23 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.040 |  |
| 2026-09-14 03:05:04 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:04:52 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:04:49 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:04:45 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.037 |  |
| 2026-09-14 03:04:33 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:04:24 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.038 |  |
| 2026-09-14 03:04:19 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:04:09 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-09-14 03:03:32 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:03:19 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:03:03 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-09-14 03:02:57 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.042 |  |
| 2026-09-14 03:02:48 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-14 03:02:16 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:02:12 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:02:07 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.040 |  |
| 2026-09-14 03:02:02 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:01:13 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.003 |  |
| 2026-09-14 03:01:11 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:01:02 | Nakkala (Kumbukkan Oya) | 0.20 | 🟢 Normal | -0.299 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 03:15:31 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-14 03:02:48 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-14 01:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 02:02:26 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 03:01:13 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.003 |  |
| 2026-09-14 03:08:16 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:39 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:05:29 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:05:04 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:02:12 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:02:16 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:02:02 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:13:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:39:08 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:03:32 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:12:26 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:04:17 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:01:11 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:22:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:05:44 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:04:33 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:04:19 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:03:19 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:04:49 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:06:09 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-14 03:06:58 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-09-14 03:04:09 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-09-14 03:03:03 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-09-14 03:04:45 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.037 |  |
| 2026-09-14 03:04:24 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.038 |  |
| 2026-09-14 03:05:23 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.040 |  |
| 2026-09-14 03:02:07 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.040 |  |
| 2026-09-14 03:02:57 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.042 |  |
| 2026-09-14 02:05:55 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | -0.044 |  |
| 2026-09-14 03:16:32 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.062 |  |
| 2026-09-14 03:13:06 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | -0.101 |  |
| 2026-09-14 03:01:02 | Nakkala (Kumbukkan Oya) | 0.20 | 🟢 Normal | -0.299 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)