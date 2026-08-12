# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_07:20:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,235 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 07:20:10 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:16:16 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:12:10 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.035 |  |
| 2026-08-12 07:10:18 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-08-12 07:08:57 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.018 |  |
| 2026-08-12 07:06:57 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.099 |  |
| 2026-08-12 07:06:17 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.018 |  |
| 2026-08-12 07:05:31 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:05:09 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:04:47 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:04:18 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:04:18 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:03:36 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-08-12 07:03:34 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-12 07:03:31 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | -0.002 |  |
| 2026-08-12 07:03:28 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:03:27 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 07:03:26 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-12 07:03:09 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 07:02:46 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.065 |  |
| 2026-08-12 07:02:33 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-12 07:02:15 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:02:01 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-08-12 07:01:52 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:01:40 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:01:39 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-12 07:01:33 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 07:01:14 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:01:12 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.033 |  |
| 2026-08-12 07:01:09 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:00:21 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.025 |  |
| 2026-08-12 07:00:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:00:08 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 07:02:33 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-12 07:03:26 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-12 07:03:09 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 07:03:34 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-12 06:03:45 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 07:01:33 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 07:03:27 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 06:32:32 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.002 |  |
| 2026-08-12 07:00:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:16:16 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:01:52 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 06:00:30 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:03:28 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:01:09 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:20:10 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:01:14 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:05:09 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:04:47 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:01:40 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:04:18 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:04:18 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:05:31 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-08-12 06:05:17 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 06:04:08 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:03:31 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | -0.002 |  |
| 2026-08-12 07:10:18 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-08-12 07:01:39 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-12 07:02:01 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-08-12 07:08:57 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.018 |  |
| 2026-08-12 07:06:17 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.018 |  |
| 2026-08-12 07:03:36 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-08-12 06:03:02 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-08-12 07:00:21 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.025 |  |
| 2026-08-12 07:01:12 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.033 |  |
| 2026-08-12 07:12:10 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.035 |  |
| 2026-08-12 07:02:46 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.065 |  |
| 2026-08-12 07:00:08 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-08-12 07:06:57 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.099 |  |
| 2026-08-12 06:07:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)