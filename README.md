# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_10:12:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,855 measurements** from **39** stations.
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
| 2026-08-26 10:12:37 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-26 10:12:07 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.062 |  |
| 2026-08-26 10:11:16 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:09:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-26 10:08:17 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-26 10:07:33 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.053 |  |
| 2026-08-26 10:07:17 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:07:06 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-26 10:06:54 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-26 10:06:25 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.066 |  |
| 2026-08-26 10:05:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:05:38 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.019 |  |
| 2026-08-26 10:04:56 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-08-26 10:04:21 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-08-26 10:04:16 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 10:04:11 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-26 10:03:43 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.166 |  |
| 2026-08-26 10:03:41 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-26 10:03:05 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 10:02:58 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:02:55 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:02:41 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:02:20 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-08-26 10:02:10 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 10:01:45 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-26 10:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:01:38 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:01:20 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:01:12 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.082 |  |
| 2026-08-26 10:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-08-26 10:01:07 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-08-26 10:01:02 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-08-26 10:00:55 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 10:00:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:00:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 10:01:07 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-08-26 10:04:21 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-08-26 10:03:41 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-26 10:07:06 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-26 10:09:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-26 10:01:45 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-26 10:06:54 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-26 10:04:11 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-26 10:04:16 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 10:12:37 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-26 10:02:10 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 10:00:55 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 10:03:05 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 10:01:38 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:00:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:00:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:02:58 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:02:55 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:21:29 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:03:06 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:02:41 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:05:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:11:16 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:07:17 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:06:54 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:01:20 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 10:08:17 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-26 10:01:02 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-08-26 10:04:56 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-08-26 10:02:20 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-08-26 10:05:38 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.019 |  |
| 2026-08-26 10:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-08-26 10:07:33 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.053 |  |
| 2026-08-26 09:05:11 | Rathnapura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.062 |  |
| 2026-08-26 10:12:07 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.062 |  |
| 2026-08-26 10:06:25 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.066 |  |
| 2026-08-26 10:01:12 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.082 |  |
| 2026-08-26 10:03:43 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.166 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)