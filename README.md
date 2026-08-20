# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_20:18:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,888 measurements** from **39** stations.
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
| 2026-08-20 20:18:04 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:17:10 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:16:46 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:14:17 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.071 |  |
| 2026-08-20 20:13:04 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.038 |  |
| 2026-08-20 20:10:21 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:07:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-20 20:07:30 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:07:27 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:07:26 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:06:52 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-20 20:05:55 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 16.035 | 🔺 Rising |
| 2026-08-20 20:05:44 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-08-20 20:05:00 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:04:43 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:04:15 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:03:47 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:03:31 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:03:13 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 20:03:12 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.051 |  |
| 2026-08-20 20:03:06 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-20 20:02:46 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 20:02:42 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:02:24 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:02:23 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:02:11 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:02:06 | Badalgama (Maha Oya) | 0.86 | 🟢 Normal | 16.035 | 🔺 Rising |
| 2026-08-20 20:02:02 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:01:44 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:01:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:01:42 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-08-20 20:01:41 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-08-20 20:01:04 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:00:11 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:59:10 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 20:05:55 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 16.035 | 🔺 Rising |
| 2026-08-20 20:01:42 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-08-20 20:03:06 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-20 19:03:03 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-20 20:03:13 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 20:07:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-20 20:02:46 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:00:11 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:02:11 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:01:44 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:07:26 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:01:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:07:27 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:02:23 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:04:45 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:18:04 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:04:15 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:15:05 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:59:10 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:10:21 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:04:43 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:05:00 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:02:24 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:02:42 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:03:47 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:02:02 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:03:31 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:02:19 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:07:30 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:16:46 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:01:04 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-20 20:06:52 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-20 20:01:41 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-08-20 20:05:44 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-08-20 19:02:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.033 |  |
| 2026-08-20 20:13:04 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.038 |  |
| 2026-08-20 20:03:12 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.051 |  |
| 2026-08-20 20:14:17 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)