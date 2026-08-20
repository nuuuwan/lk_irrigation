# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_21:12:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,921 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 21:12:04 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.035 |  |
| 2026-08-20 21:11:16 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:06:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:05:41 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-20 21:05:32 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 21:05:15 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.069 |  |
| 2026-08-20 21:05:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:04:48 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-20 21:04:45 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-20 21:04:42 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-08-20 21:04:24 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:03:50 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-20 21:03:40 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 21:03:34 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:03:31 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-08-20 21:03:28 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:03:26 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.011 |  |
| 2026-08-20 21:03:21 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:03:12 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:03:03 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:03:03 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-08-20 21:02:59 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:02:42 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.076 |  |
| 2026-08-20 21:02:29 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:02:16 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:02:01 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 21:01:43 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-20 21:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:01:34 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 21:01:17 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:00:42 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:39:18 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.045 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 21:01:43 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-20 21:05:41 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-20 21:02:01 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 21:03:40 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 21:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 21:05:32 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:00:42 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:03:34 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:07:26 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:02:16 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:02:59 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:04:45 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:18:04 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:11:16 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:15:05 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:06:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:03:28 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:02:29 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:03:03 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:05:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:03:21 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:02:19 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:03:12 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:01:34 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:01:17 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-20 21:04:45 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-20 21:03:03 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-08-20 21:03:50 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-20 21:04:48 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-20 21:03:31 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-08-20 20:01:41 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-08-20 21:03:26 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.011 |  |
| 2026-08-20 21:04:42 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-08-20 21:12:04 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.035 |  |
| 2026-08-20 21:05:15 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.069 |  |
| 2026-08-20 20:14:17 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.071 |  |
| 2026-08-20 21:02:42 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)