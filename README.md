# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_07:18:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,017 measurements** from **39** stations.
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
| 2026-08-14 07:18:26 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:13:01 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.008 |  |
| 2026-08-14 07:11:58 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-14 07:11:52 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.008 |  |
| 2026-08-14 07:11:46 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-14 07:11:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:11:11 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.043 |  |
| 2026-08-14 07:10:02 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:08:38 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:06:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-14 07:06:15 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:05:09 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-08-14 07:05:08 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:04:56 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.039 |  |
| 2026-08-14 07:04:41 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.047 |  |
| 2026-08-14 07:04:29 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-14 07:04:02 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:03:39 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:03:19 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:03:10 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-08-14 07:02:51 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:02:48 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:02:45 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:02:42 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 07:02:37 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-14 07:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | -0.097 |  |
| 2026-08-14 07:02:26 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:02:17 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:02:10 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.084 |  |
| 2026-08-14 07:02:08 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.118 |  |
| 2026-08-14 07:01:38 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:01:23 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:01:16 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:00:44 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 07:11:58 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-14 07:04:29 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-14 07:02:42 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 07:11:46 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-14 07:06:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-14 06:05:02 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:11:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:06:15 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:00:44 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:01:23 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:41 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:03:39 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:03:10 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:02:26 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:03:19 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:05:08 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:02:45 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:02:48 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:04:02 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:02:51 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:08:38 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:02:17 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:46 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:01:38 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:10:02 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:18:26 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:01:16 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-14 07:13:01 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.008 |  |
| 2026-08-14 07:11:52 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.008 |  |
| 2026-08-14 07:05:09 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-08-14 07:02:37 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-14 07:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-08-14 06:06:39 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-08-14 07:04:56 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.039 |  |
| 2026-08-14 07:11:11 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.043 |  |
| 2026-08-14 07:04:41 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.047 |  |
| 2026-08-14 07:02:10 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.084 |  |
| 2026-08-14 07:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | -0.097 |  |
| 2026-08-14 07:02:08 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)