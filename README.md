# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_12:09:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,634 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 12:09:29 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:09:10 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.176 |  |
| 2026-08-10 12:08:34 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:08:08 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:07:32 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.005 |  |
| 2026-08-10 12:07:08 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:07:07 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:07:07 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.148 |  |
| 2026-08-10 12:06:49 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-10 12:06:26 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-08-10 12:05:20 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | -0.098 |  |
| 2026-08-10 12:05:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:05:01 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 12:04:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.090 |  |
| 2026-08-10 12:04:58 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-10 12:04:56 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:04:44 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-08-10 12:04:30 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.028 |  |
| 2026-08-10 12:04:24 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:04:14 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-08-10 12:03:52 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-10 12:03:33 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:03:22 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:03:13 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.092 |  |
| 2026-08-10 12:03:06 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-08-10 12:03:02 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | -0.020 |  |
| 2026-08-10 12:02:50 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.020 |  |
| 2026-08-10 12:02:19 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:02:14 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:02:06 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:01:49 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.019 |  |
| 2026-08-10 12:01:48 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-08-10 12:01:47 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:01:47 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:01:43 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 12:01:39 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-10 12:01:30 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:00:35 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 12:04:58 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-10 12:06:49 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-10 12:01:39 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-10 12:01:43 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 12:05:01 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 12:09:29 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:03:22 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:01:30 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:08:34 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:02:06 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:04:24 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 11:10:50 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:05:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:01:47 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:08:08 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:02:14 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:04:56 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:03:33 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:00:35 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:07:08 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:01:47 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:07:07 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:07:32 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.005 |  |
| 2026-08-10 12:06:26 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-08-10 12:03:52 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-10 11:00:19 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-08-10 12:01:48 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-08-10 12:03:06 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-08-10 12:01:49 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.019 |  |
| 2026-08-10 12:04:44 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-08-10 12:03:02 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | -0.020 |  |
| 2026-08-10 12:02:50 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.020 |  |
| 2026-08-10 12:04:30 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.028 |  |
| 2026-08-10 12:04:14 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-08-10 12:04:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.090 |  |
| 2026-08-10 12:03:13 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.092 |  |
| 2026-08-10 12:05:20 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | -0.098 |  |
| 2026-08-10 12:07:07 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.148 |  |
| 2026-08-10 12:09:10 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.176 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)