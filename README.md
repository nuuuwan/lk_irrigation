# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_07:19:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,779 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 07:19:40 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:15:58 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:14:33 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:12:49 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 07:10:31 | Galgamuwa (Mee Oya) | 1.59 | 🟢 Normal | -0.013 |  |
| 2026-10-21 07:10:00 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:08:55 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:08:27 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.029 |  |
| 2026-10-21 07:07:01 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-10-21 07:07:00 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | -0.047 |  |
| 2026-10-21 07:06:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:06:45 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-10-21 07:06:32 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-21 07:06:07 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.025 |  |
| 2026-10-21 07:06:02 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.018 |  |
| 2026-10-21 07:05:45 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-10-21 07:05:40 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.040 |  |
| 2026-10-21 07:05:30 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-21 07:05:27 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:04:32 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.019 |  |
| 2026-10-21 07:04:32 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | -0.257 |  |
| 2026-10-21 07:03:35 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:03:33 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 07:03:27 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-21 07:03:25 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-10-21 07:02:55 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-10-21 07:02:20 | Thalgahagoda (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.057 |  |
| 2026-10-21 07:02:10 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 07:02:08 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.091 |  |
| 2026-10-21 07:01:59 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-21 07:01:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:01:48 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-10-21 07:01:43 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.031 |  |
| 2026-10-21 07:01:36 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 07:01:31 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:01:12 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:00:59 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 07:00:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-10-21 07:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 07:05:30 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-21 07:01:59 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-21 07:06:32 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-21 07:00:59 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 07:01:36 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 07:03:33 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 07:02:10 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 07:12:49 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 07:03:35 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:01:31 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:19:40 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:05:27 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:15:58 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:14:33 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:08:55 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:04:32 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:10:00 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:06:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:01:12 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-21 07:07:01 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-10-21 07:03:27 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-21 07:01:48 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-10-21 07:02:55 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-10-21 07:10:31 | Galgamuwa (Mee Oya) | 1.59 | 🟢 Normal | -0.013 |  |
| 2026-10-21 07:06:02 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.018 |  |
| 2026-10-21 07:04:32 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.019 |  |
| 2026-10-21 07:05:45 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-10-21 07:06:07 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.025 |  |
| 2026-10-21 07:06:45 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-10-21 07:08:27 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.029 |  |
| 2026-10-21 07:01:43 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.031 |  |
| 2026-10-21 07:03:25 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-10-21 07:05:40 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.040 |  |
| 2026-10-21 07:07:00 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | -0.047 |  |
| 2026-10-21 07:02:20 | Thalgahagoda (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.057 |  |
| 2026-10-21 07:00:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-10-21 07:02:08 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.091 |  |
| 2026-10-21 07:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | -0.257 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)