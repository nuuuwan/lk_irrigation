# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_11:15:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,934 measurements** from **39** stations.
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
| 2026-10-21 11:15:14 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:09:30 | Thalgahagoda (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.022 |  |
| 2026-10-21 11:07:14 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.013 |  |
| 2026-10-21 11:06:47 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:05:49 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:05:29 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-21 11:05:13 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-10-21 11:05:03 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 11:04:37 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-21 11:04:33 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:03:27 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.011 |  |
| 2026-10-21 11:03:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-21 11:03:26 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:03:13 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:03:12 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 11:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:02:56 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-21 11:02:56 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:02:37 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.022 |  |
| 2026-10-21 11:02:30 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 11:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.030 |  |
| 2026-10-21 11:02:18 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.022 |  |
| 2026-10-21 11:02:18 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-21 11:02:12 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-21 11:02:09 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:02:08 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 11:02:04 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 11:02:02 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:02:00 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-21 11:01:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 11:01:42 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 11:01:42 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-10-21 11:01:24 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:01:22 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.013 |  |
| 2026-10-21 11:01:22 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:01:12 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-21 11:00:26 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 11:03:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-21 11:02:12 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-21 11:02:18 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-21 11:01:12 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-21 11:01:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 11:02:30 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 11:05:03 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 11:03:12 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 11:02:04 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 11:01:42 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 11:02:08 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 11:01:24 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:06:47 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:02:02 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:03:26 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:02:09 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:02:56 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:15:14 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:04:33 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:05:49 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:03:13 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:00:26 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:01:22 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 11:02:56 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-21 11:05:29 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-21 11:01:42 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-10-21 11:04:37 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-21 10:04:43 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-21 11:03:27 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.011 |  |
| 2026-10-21 11:01:22 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.013 |  |
| 2026-10-21 11:07:14 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.013 |  |
| 2026-10-21 11:02:00 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-21 11:05:13 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-10-21 11:02:37 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.022 |  |
| 2026-10-21 11:02:18 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.022 |  |
| 2026-10-21 11:09:30 | Thalgahagoda (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.022 |  |
| 2026-10-21 10:00:23 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | -0.023 |  |
| 2026-10-21 11:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.030 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)