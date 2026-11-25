# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_16:26:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,464 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 16:26:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.022 |  |
| 2026-11-25 16:11:07 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-25 16:09:53 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-11-25 16:09:49 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.009 |  |
| 2026-11-25 16:09:43 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | -0.018 |  |
| 2026-11-25 16:09:02 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | -0.077 |  |
| 2026-11-25 16:07:19 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.049 |  |
| 2026-11-25 16:07:07 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.035 |  |
| 2026-11-25 16:06:54 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.046 |  |
| 2026-11-25 16:06:47 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 16:06:31 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.029 |  |
| 2026-11-25 16:06:18 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 16:06:14 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 16:06:01 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-25 16:04:50 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | -0.040 |  |
| 2026-11-25 16:04:48 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-11-25 16:04:43 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.043 |  |
| 2026-11-25 16:04:20 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.050 |  |
| 2026-11-25 16:04:19 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.120 |  |
| 2026-11-25 16:04:11 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-11-25 16:03:24 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 16:03:21 | Moraketiya (Walawe Ganga) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-11-25 16:03:01 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.090 |  |
| 2026-11-25 16:02:54 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.070 |  |
| 2026-11-25 16:02:50 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-11-25 16:02:41 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-25 16:02:35 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-25 16:02:34 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-25 16:02:20 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-25 16:02:13 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.041 |  |
| 2026-11-25 16:02:10 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-25 16:01:55 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-25 16:01:28 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-25 16:01:26 | Nawalapitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 16:01:23 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-11-25 16:01:09 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.037 |  |
| 2026-11-25 16:00:15 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 16:02:50 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-11-25 16:01:23 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-11-25 16:09:53 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-11-25 16:01:28 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-25 16:02:41 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-25 16:02:10 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-25 16:02:20 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-25 16:01:26 | Nawalapitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 16:02:35 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-25 16:03:24 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 16:06:14 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 16:06:47 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 16:06:18 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 16:01:55 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-25 16:06:01 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:01:34 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-25 16:00:15 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-25 16:09:49 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.009 |  |
| 2026-11-25 16:04:48 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-11-25 16:02:34 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-25 16:11:07 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-25 16:09:43 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | -0.018 |  |
| 2026-11-25 16:04:11 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-11-25 16:03:21 | Moraketiya (Walawe Ganga) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-11-25 16:26:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.022 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 16:06:31 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.029 |  |
| 2026-11-25 16:07:07 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.035 |  |
| 2026-11-25 16:01:09 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.037 |  |
| 2026-11-25 16:04:50 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | -0.040 |  |
| 2026-11-25 16:02:13 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.041 |  |
| 2026-11-25 16:04:43 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.043 |  |
| 2026-11-25 16:06:54 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.046 |  |
| 2026-11-25 16:07:19 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.049 |  |
| 2026-11-25 16:04:20 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.050 |  |
| 2026-11-25 16:02:54 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.070 |  |
| 2026-11-25 16:09:02 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | -0.077 |  |
| 2026-11-25 16:03:01 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.090 |  |
| 2026-11-25 16:04:19 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)