# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_11:03:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,349 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 11:03:46 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 11:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | -0.059 |  |
| 2026-11-06 11:03:37 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-11-06 11:03:31 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.076 |  |
| 2026-11-06 11:03:24 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-11-06 11:03:08 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | 0.972 | 🔺 Rising |
| 2026-11-06 11:03:06 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-11-06 11:03:06 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-06 11:03:01 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 11:02:47 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 11:02:44 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 11:02:33 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-11-06 11:02:30 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-11-06 11:02:16 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-11-06 11:02:15 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-11-06 11:01:58 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.050 |  |
| 2026-11-06 11:01:46 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | -0.022 |  |
| 2026-11-06 11:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-11-06 11:01:35 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.059 |  |
| 2026-11-06 11:01:32 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-11-06 11:01:31 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-11-06 11:01:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-06 11:01:19 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-11-06 11:01:07 | Moragaswewa (Deduru Oya) | 2.88 | 🟢 Normal | -0.040 |  |
| 2026-11-06 11:00:47 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-06 11:00:26 | Thanthirimale (Malwathu Oya) | 1.69 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-06 10:34:08 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 11:03:08 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | 0.972 | 🔺 Rising |
| 2026-11-06 10:05:46 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.296 | 🔺 Rising |
| 2026-11-06 10:04:14 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-06 11:01:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-06 11:03:01 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 10:10:11 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-06 11:00:26 | Thanthirimale (Malwathu Oya) | 1.69 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-06 11:03:46 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 11:02:47 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 11:03:06 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-11-06 11:02:44 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 11:02:15 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:06:14 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:04:56 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-06 11:03:37 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-11-06 11:03:06 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-06 11:02:33 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-11-06 11:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-11-06 10:07:24 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-11-06 11:00:47 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-06 11:01:19 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-11-06 10:02:24 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-11-06 10:10:10 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.019 |  |
| 2026-11-06 10:06:55 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.019 |  |
| 2026-11-06 11:03:24 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-11-06 11:01:32 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-11-06 11:01:31 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-11-06 11:01:46 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | -0.022 |  |
| 2026-11-06 10:06:18 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-11-06 10:03:29 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.030 |  |
| 2026-11-06 10:02:53 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.032 |  |
| 2026-11-06 11:01:07 | Moragaswewa (Deduru Oya) | 2.88 | 🟢 Normal | -0.040 |  |
| 2026-11-06 10:02:27 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.042 |  |
| 2026-11-06 11:01:58 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.050 |  |
| 2026-11-06 10:06:53 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | -0.052 |  |
| 2026-11-06 11:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | -0.059 |  |
| 2026-11-06 11:01:35 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.059 |  |
| 2026-11-06 11:02:30 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-11-06 11:03:31 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)