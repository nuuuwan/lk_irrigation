# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_18:08:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,800 measurements** from **39** stations.
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
| 2026-11-23 18:08:41 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:08:11 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:07:20 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:06:54 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:06:21 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:04:56 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:04:08 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.019 |  |
| 2026-11-23 18:03:47 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-23 18:03:32 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.158 |  |
| 2026-11-23 18:03:27 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.042 |  |
| 2026-11-23 18:03:26 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:03:26 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-23 18:03:09 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.031 |  |
| 2026-11-23 18:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.071 |  |
| 2026-11-23 18:02:53 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-23 18:02:52 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.030 |  |
| 2026-11-23 18:02:50 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.048 |  |
| 2026-11-23 18:02:50 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.022 |  |
| 2026-11-23 18:02:43 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:02:39 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:02:25 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-23 18:02:08 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-11-23 18:02:03 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:01:55 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-23 18:01:42 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:01:36 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-11-23 18:01:35 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-11-23 18:01:34 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.064 |  |
| 2026-11-23 18:01:31 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-23 18:01:18 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.145 |  |
| 2026-11-23 18:01:16 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:00:55 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:00:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.25 | 🟢 Normal | -0.058 |  |
| 2026-11-23 18:00:53 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-23 18:00:18 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:00:06 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 18:01:36 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-11-23 18:02:25 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-23 18:03:26 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-23 18:02:53 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-23 18:01:31 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-23 18:02:03 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:00:55 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:01:16 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:01:42 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:03:26 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:00:53 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:02:43 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:02:39 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:04:56 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:08:41 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:00:18 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:07:20 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:08:11 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:00:06 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:06:21 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-11-23 18:03:47 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-23 18:04:08 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.019 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-23 18:01:55 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-23 18:01:35 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 18:02:50 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.022 |  |
| 2026-11-23 18:02:08 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-11-23 18:02:52 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.030 |  |
| 2026-11-23 18:03:09 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.031 |  |
| 2026-11-23 18:03:27 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.042 |  |
| 2026-11-23 18:02:50 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.048 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-23 18:00:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.25 | 🟢 Normal | -0.058 |  |
| 2026-11-23 18:01:34 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.064 |  |
| 2026-11-23 18:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.071 |  |
| 2026-11-23 18:01:18 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.145 |  |
| 2026-11-23 18:03:32 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)