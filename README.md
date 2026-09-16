# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_07:13:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,238 measurements** from **39** stations.
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
| 2026-09-16 07:13:55 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:13:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | -0.083 |  |
| 2026-09-16 07:12:49 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.037 |  |
| 2026-09-16 07:12:41 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:07:54 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-16 07:07:35 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.134 |  |
| 2026-09-16 07:07:34 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.055 |  |
| 2026-09-16 07:07:32 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-09-16 07:06:54 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.067 |  |
| 2026-09-16 07:06:25 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.022 |  |
| 2026-09-16 07:06:03 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:05:46 | Dunamale (Aththanagalu Oya) | 2.11 | 🟢 Normal | -0.071 |  |
| 2026-09-16 07:05:15 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-16 07:05:01 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | -0.041 |  |
| 2026-09-16 07:04:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.131 |  |
| 2026-09-16 07:04:24 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:04:15 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-16 07:03:25 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-16 07:03:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:03:09 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-09-16 07:02:49 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | -0.034 |  |
| 2026-09-16 07:02:38 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-09-16 07:02:36 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | 0.359 | 🔺 Rising |
| 2026-09-16 07:02:26 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:02:22 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.002 |  |
| 2026-09-16 07:02:21 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.071 |  |
| 2026-09-16 07:02:20 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 07:02:09 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:01:53 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-16 07:01:52 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-09-16 07:01:51 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:01:49 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.050 |  |
| 2026-09-16 07:01:44 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-09-16 07:01:32 | Magura (Kalu Ganga) | 2.93 | 🟢 Normal | -0.167 |  |
| 2026-09-16 07:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-16 07:00:18 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:00:16 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:00:12 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 07:02:36 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | 0.359 | 🔺 Rising |
| 2026-09-16 07:07:54 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-16 07:05:15 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-16 07:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-16 07:04:15 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-16 07:01:53 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-16 07:02:20 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 07:02:22 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.002 |  |
| 2026-09-16 07:02:26 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:00:18 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:02:09 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:01:51 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:13:55 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:06:03 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:00:16 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:03:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:04:24 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:12:41 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:03:25 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-16 07:01:52 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-09-16 07:02:38 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-09-16 07:07:32 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-09-16 07:03:09 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-09-16 07:01:44 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-09-16 07:00:12 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.022 |  |
| 2026-09-16 07:06:25 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.022 |  |
| 2026-09-16 07:02:49 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | -0.034 |  |
| 2026-09-16 07:12:49 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.037 |  |
| 2026-09-16 07:05:01 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | -0.041 |  |
| 2026-09-16 07:01:49 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.050 |  |
| 2026-09-16 07:07:34 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.055 |  |
| 2026-09-16 07:06:54 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.067 |  |
| 2026-09-16 07:02:21 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.071 |  |
| 2026-09-16 07:05:46 | Dunamale (Aththanagalu Oya) | 2.11 | 🟢 Normal | -0.071 |  |
| 2026-09-16 07:13:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | -0.083 |  |
| 2026-09-16 06:10:00 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.123 |  |
| 2026-09-16 07:04:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.131 |  |
| 2026-09-16 07:07:35 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.134 |  |
| 2026-09-16 07:01:32 | Magura (Kalu Ganga) | 2.93 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)