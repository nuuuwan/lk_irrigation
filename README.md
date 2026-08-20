# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_07:46:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,384 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 07:46:25 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:25:30 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-20 07:14:09 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-20 07:09:05 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.096 |  |
| 2026-08-20 07:08:32 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:08:08 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.038 |  |
| 2026-08-20 07:07:38 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-20 07:07:19 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:07:00 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:06:48 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:06:32 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.019 |  |
| 2026-08-20 07:06:30 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-20 07:06:25 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:06:03 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-08-20 07:05:51 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-08-20 07:05:51 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-08-20 07:05:46 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:05:17 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:04:45 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:04:43 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 07:02:19 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-08-20 07:03:28 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-08-20 07:06:03 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-08-20 07:05:51 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-08-20 07:14:09 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-20 07:06:30 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-20 07:07:38 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-20 07:01:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-20 07:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-20 06:06:00 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-20 07:03:24 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-20 07:04:43 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 07:04:11 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 07:03:54 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 07:25:30 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-20 07:02:54 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:00:34 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:00:58 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:01:41 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:05:17 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:07:19 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:03:43 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:05:46 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:06:25 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:06:48 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:02:48 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:04:17 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:07:00 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:08:32 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:46:25 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:04:45 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:01:13 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 07:05:51 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-08-20 07:04:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-20 07:06:32 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.019 |  |
| 2026-08-20 07:08:08 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.038 |  |
| 2026-08-20 07:01:38 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.060 |  |
| 2026-08-20 07:09:05 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)