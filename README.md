# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_08:03:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,224 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 08:03:40 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.050 |  |
| 2026-11-06 08:03:36 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:03:29 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-06 08:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.39 | 🟢 Normal | -0.040 |  |
| 2026-11-06 08:02:56 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.054 |  |
| 2026-11-06 08:02:40 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 08:02:11 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:02:08 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:02:01 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:01:59 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:01:46 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-06 08:01:21 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-11-06 08:01:20 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | -0.031 |  |
| 2026-11-06 08:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-06 08:01:09 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-11-06 08:01:04 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.071 |  |
| 2026-11-06 08:01:03 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 08:00:26 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 07:03:27 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-06 07:06:01 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-06 08:03:29 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-06 07:06:35 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-06 08:01:03 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 07:04:08 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 07:09:26 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-06 07:02:25 | Moragaswewa (Deduru Oya) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-06 08:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:09:51 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:01:22 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 08:02:40 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:07:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:10:03 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:07:45 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:02:15 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:05:28 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.005 |  |
| 2026-11-06 08:02:01 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:02:08 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:03:36 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:02:11 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:01:59 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:01:46 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-06 08:01:09 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-11-06 07:02:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.021 |  |
| 2026-11-06 07:19:08 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.026 |  |
| 2026-11-06 08:01:21 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-11-06 08:01:20 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | -0.031 |  |
| 2026-11-06 07:03:23 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | -0.032 |  |
| 2026-11-06 08:00:26 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.033 |  |
| 2026-11-06 07:07:00 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | -0.037 |  |
| 2026-11-06 08:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.39 | 🟢 Normal | -0.040 |  |
| 2026-11-06 07:15:05 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.048 |  |
| 2026-11-06 08:03:40 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.050 |  |
| 2026-11-06 08:02:56 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.054 |  |
| 2026-11-06 07:08:28 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.055 |  |
| 2026-11-06 08:01:04 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.071 |  |
| 2026-11-06 07:05:06 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | -0.086 |  |
| 2026-11-06 07:02:03 | Putupaula (Kalu Ganga) | 1.24 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)