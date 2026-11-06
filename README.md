# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_10:34:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,323 measurements** from **39** stations.
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
| 2026-11-06 10:34:08 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | 0.004 |  |
| 2026-11-06 10:11:08 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.034 |  |
| 2026-11-06 10:10:11 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-06 10:10:10 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.019 |  |
| 2026-11-06 10:08:32 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.029 |  |
| 2026-11-06 10:08:17 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:07:24 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-11-06 10:06:55 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.019 |  |
| 2026-11-06 10:06:53 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | -0.052 |  |
| 2026-11-06 10:06:18 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-11-06 10:06:17 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:06:14 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:06:13 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.031 |  |
| 2026-11-06 10:05:46 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.296 | 🔺 Rising |
| 2026-11-06 10:05:45 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-06 10:04:56 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:04:53 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-11-06 10:04:39 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-11-06 10:04:14 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-06 10:03:52 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.743 |  |
| 2026-11-06 10:03:34 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.031 |  |
| 2026-11-06 10:03:29 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.030 |  |
| 2026-11-06 10:03:09 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.020 |  |
| 2026-11-06 10:02:55 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:02:53 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.032 |  |
| 2026-11-06 10:02:27 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.042 |  |
| 2026-11-06 10:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | -0.052 |  |
| 2026-11-06 10:02:24 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-11-06 10:02:24 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:02:15 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:02:08 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 10:02:04 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.035 |  |
| 2026-11-06 10:01:56 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:01:43 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-11-06 10:01:41 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:01:18 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-11-06 10:01:01 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.033 |  |
| 2026-11-06 10:00:45 | Moragaswewa (Deduru Oya) | 2.92 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 10:05:46 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.296 | 🔺 Rising |
| 2026-11-06 10:04:14 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-06 10:05:45 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-06 10:10:11 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-06 10:02:08 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 10:34:08 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | 0.004 |  |
| 2026-11-06 10:02:15 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:01:41 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:08:17 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:02:24 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:06:17 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:01:56 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:02:55 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:06:14 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:04:56 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-06 10:01:43 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-11-06 10:04:39 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-11-06 10:04:53 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-11-06 10:07:24 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-11-06 10:01:18 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-11-06 10:02:24 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-11-06 10:10:10 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.019 |  |
| 2026-11-06 10:06:55 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.019 |  |
| 2026-11-06 10:03:09 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.020 |  |
| 2026-11-06 10:00:45 | Moragaswewa (Deduru Oya) | 2.92 | 🟢 Normal | -0.021 |  |
| 2026-11-06 10:06:18 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-11-06 10:08:32 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.029 |  |
| 2026-11-06 10:03:29 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.030 |  |
| 2026-11-06 10:06:13 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.031 |  |
| 2026-11-06 10:03:34 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.031 |  |
| 2026-11-06 10:02:53 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.032 |  |
| 2026-11-06 10:01:01 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.033 |  |
| 2026-11-06 10:11:08 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.034 |  |
| 2026-11-06 10:02:04 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.035 |  |
| 2026-11-06 10:02:27 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.042 |  |
| 2026-11-06 10:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | -0.052 |  |
| 2026-11-06 10:06:53 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | -0.052 |  |
| 2026-11-06 10:03:52 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.743 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)