# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_11:08:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,899 measurements** from **39** stations.
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
| 2026-10-01 11:08:05 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2026-10-01 11:07:03 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:06:51 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:06:21 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.197 |  |
| 2026-10-01 11:05:57 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:05:54 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-01 11:05:48 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:05:32 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:05:25 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:05:24 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:04:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:04:25 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:04:13 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:03:43 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.059 |  |
| 2026-10-01 11:03:37 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:03:12 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.049 |  |
| 2026-10-01 11:03:03 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:02:53 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:02:39 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:02:39 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:02:29 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-01 11:02:22 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-10-01 11:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:02:18 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:02:18 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:01:55 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 11:01:33 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:01:28 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:01:14 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:01:10 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 11:01:05 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:00:45 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:55:27 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:55:26 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:55:24 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:30:27 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 11:05:54 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-01 11:02:29 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-01 11:01:55 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 11:01:10 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 11:05:24 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:06:51 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:05:32 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:04:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:03:37 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:05:48 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:24:23 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:05:57 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:02:53 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:03:03 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:04:13 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:30:27 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:07:03 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:05:25 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:01:05 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-01 11:01:33 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 10:15:25 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.009 |  |
| 2026-10-01 11:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:01:28 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:02:18 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:02:39 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:02:39 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:01:14 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:00:45 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:02:18 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-01 11:04:25 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-10-01 10:08:33 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-10-01 10:05:49 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-10-01 11:08:05 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2026-10-01 11:03:12 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.049 |  |
| 2026-10-01 11:02:22 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-10-01 10:21:53 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.057 |  |
| 2026-10-01 11:03:43 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.059 |  |
| 2026-10-01 11:06:21 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)