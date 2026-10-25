# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_12:12:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,539 measurements** from **39** stations.
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
| 2026-10-25 12:12:23 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:10:45 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-25 12:09:00 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-25 12:08:40 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-25 12:08:32 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:08:01 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 12:07:39 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 12:07:19 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:06:48 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.018 |  |
| 2026-10-25 12:06:42 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.033 |  |
| 2026-10-25 12:05:47 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-25 12:05:24 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 12:05:11 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:05:02 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-10-25 12:04:45 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:04:17 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:04:09 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-10-25 12:04:00 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-25 12:03:53 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-10-25 12:03:39 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-25 12:03:34 | Ellagawa (Kalu Ganga) | 6.62 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-25 12:03:31 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.022 |  |
| 2026-10-25 12:03:20 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:03:18 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-25 12:03:04 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:02:53 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-25 12:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 12:02:44 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-10-25 12:02:34 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-25 12:02:31 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:02:27 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-25 12:02:17 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:02:10 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-25 12:01:59 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:01:51 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | -0.020 |  |
| 2026-10-25 12:01:29 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.103 |  |
| 2026-10-25 12:01:07 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-25 12:00:42 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-25 12:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-25 12:00:32 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.125 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 12:00:32 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-10-25 12:03:34 | Ellagawa (Kalu Ganga) | 6.62 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-25 12:08:40 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-25 12:10:45 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-25 12:02:10 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-25 12:03:39 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-25 12:03:18 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-25 12:05:47 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-25 12:01:07 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-25 12:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-25 12:04:00 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-25 12:09:00 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-25 12:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 12:05:24 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 12:02:34 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-25 12:08:01 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 12:07:39 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 12:07:19 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:01:59 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:04:17 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:08:32 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:03:04 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:05:11 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:04:45 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:03:20 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:12:23 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:02:31 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-25 12:04:09 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-10-25 12:02:53 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-25 12:03:53 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-10-25 12:02:27 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-25 12:00:42 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-25 12:06:48 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.018 |  |
| 2026-10-25 12:02:44 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-10-25 12:05:02 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-10-25 12:01:51 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | -0.020 |  |
| 2026-10-25 12:03:31 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.022 |  |
| 2026-10-25 12:06:42 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.033 |  |
| 2026-10-25 12:01:29 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)