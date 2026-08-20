# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_08:14:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,421 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 08:14:52 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:12:41 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 3.130 | 🔺 Rising |
| 2026-08-20 08:12:18 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 3.130 | 🔺 Rising |
| 2026-08-20 08:10:36 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:09:50 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-08-20 08:09:02 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-20 08:08:41 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-20 08:08:27 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-08-20 08:08:15 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:06:09 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-20 08:05:49 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:05:45 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-20 08:05:33 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-08-20 08:04:37 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.067 |  |
| 2026-08-20 08:04:28 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-08-20 08:04:13 | Rathnapura (Kalu Ganga) | 2.67 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-08-20 08:04:05 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:03:54 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.043 |  |
| 2026-08-20 08:03:51 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:03:43 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:03:28 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.042 |  |
| 2026-08-20 08:03:26 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:03:18 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.021 |  |
| 2026-08-20 08:03:17 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:03:15 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:03:06 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 08:02:39 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.408 |  |
| 2026-08-20 08:02:35 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-20 08:02:33 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-08-20 08:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 08:01:53 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.031 |  |
| 2026-08-20 08:01:52 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-20 08:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:01:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:00:56 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:00:56 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:46:25 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:25:30 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.008 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 08:12:41 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 3.130 | 🔺 Rising |
| 2026-08-20 08:09:50 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-08-20 08:04:13 | Rathnapura (Kalu Ganga) | 2.67 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-08-20 08:06:09 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-20 08:08:27 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-08-20 08:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-20 08:09:02 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-20 08:05:45 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-20 08:08:41 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-20 07:04:43 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 08:03:06 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 08:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 07:25:30 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-20 08:03:43 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:00:58 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:10:36 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:03:26 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:03:17 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:02:35 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:01:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:08:15 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:03:15 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:05:49 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:03:51 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:04:05 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:14:52 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:04:45 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:00:56 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:05:33 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-08-20 08:01:52 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-20 08:04:28 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-08-20 08:02:33 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-08-20 08:03:18 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.021 |  |
| 2026-08-20 08:01:53 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.031 |  |
| 2026-08-20 08:03:28 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.042 |  |
| 2026-08-20 08:03:54 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.043 |  |
| 2026-08-20 08:04:37 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.067 |  |
| 2026-08-20 08:02:39 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.408 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)